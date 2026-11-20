#!/usr/bin/env python3
"""Generate original, royalty-free background music beds (no samples, no third-party audio).

  ~/.cache/pricewhy/venv/bin/python tools/video/music.py <out.wav> --key A --mood minor --bpm 84 --seconds 120 --seed 3

A calm documentary bed: soft detuned pad chords + a gentle plucked arpeggio + a
quiet sub note, with a slow fade so it loops cleanly. Different key/mood/bpm/seed
give audibly different tracks, which keeps videos from sounding templated
(docs/11 rule 3). Mixed at about -23 dB under the voice by assemble.py.
"""
import argparse

import numpy as np
import soundfile as sf

SR = 44100
NOTE = {"C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11}
PROGRESSIONS = {  # scale degrees as semitone offsets of chord roots + chord quality
    "minor": [(0, "m"), (8, "M"), (3, "M"), (10, "M")],      # i – VI – III – VII
    "major": [(0, "M"), (9, "m"), (5, "M"), (7, "M")],       # I – vi – IV – V
    "dorian": [(0, "m"), (5, "M"), (10, "M"), (5, "M")],     # i – IV – VII – IV
}


def freq(semitone_from_a4):
    return 440.0 * 2 ** (semitone_from_a4 / 12)


def chord(root, quality):
    third = 3 if quality == "m" else 4
    return [root, root + third, root + 7, root + 12]


def env(n, attack, release):
    e = np.ones(n)
    a, r = min(int(attack * SR), n // 2), min(int(release * SR), n // 2)
    if a:
        e[:a] = np.linspace(0, 1, a)
    if r:
        e[-r:] = np.linspace(1, 0, r)
    return e


def lowpass(x, taps=24):
    k = np.hanning(taps)  # short smoothing window = gentle low-pass, vectorised
    return np.convolve(x, k / k.sum(), mode="same")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--key", default="A")
    ap.add_argument("--mood", default="minor", choices=PROGRESSIONS)
    ap.add_argument("--bpm", type=float, default=84)
    ap.add_argument("--seconds", type=float, default=120)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)

    beat = 60 / a.bpm
    bar = 4 * beat
    total = int(a.seconds * SR)
    t_bar = np.arange(int(bar * SR)) / SR
    base = NOTE[a.key] - 9 - 12          # key root, one octave below A4 range
    out = np.zeros(total)
    prog = PROGRESSIONS[a.mood]
    pattern = rng.permutation([0, 1, 2, 3, 2, 1, 3, 0])  # arpeggio order, varies with seed

    pos, i = 0, 0
    while pos < total:
        root, q = prog[i % len(prog)]
        notes = chord(base + root, q)
        n = min(len(t_bar), total - pos)
        t = t_bar[:n]
        pad = np.zeros(n)
        for s in notes:
            f = freq(s)
            for det in (-0.12, 0.0, 0.12):  # detuned voices = warm pad
                pad += np.sin(2 * np.pi * f * (1 + det / 100) * t)
        pad *= env(n, bar * 0.35, bar * 0.35) / 12
        arp = np.zeros(n)
        step = beat / 2
        for k in range(8):
            st = int(k * step * SR)
            if st >= n:
                break
            f = freq(notes[pattern[k] % 4] + 12)
            m = min(int(step * 2 * SR), n - st)
            tt = np.arange(m) / SR
            arp[st:st + m] += np.sin(2 * np.pi * f * tt) * np.exp(-tt * 5.5) * 0.10
        sub = np.sin(2 * np.pi * freq(base + root - 12) * t) * env(n, 0.3, 0.6) * 0.10
        out[pos:pos + n] += pad + arp + sub
        pos += n
        i += 1

    out = lowpass(out)
    delay = int(beat * 0.75 * SR)                  # simple echo for space
    echo = np.zeros_like(out)
    echo[delay:] = out[:-delay] * 0.28
    out = out + echo
    fade = int(2 * SR)
    out[:fade] *= np.linspace(0, 1, fade)
    out[-fade:] *= np.linspace(1, 0, fade)
    out = out / (np.max(np.abs(out)) or 1) * 0.8
    sf.write(a.out, np.stack([out, out], axis=1).astype(np.float32), SR)
    print(f"wrote {a.out}: {a.seconds:.0f}s, {a.key} {a.mood}, {a.bpm} bpm, seed {a.seed}")


if __name__ == "__main__":
    main()
