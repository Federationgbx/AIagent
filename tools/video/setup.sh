#!/usr/bin/env bash
# One-time setup for the video pipeline (voice + assembly), idempotent.
# Installs Kokoro TTS (Apache-2.0 open-weight model, commercial use allowed) in a
# private venv and downloads the model + voices from Hugging Face.
# Nothing here goes into the repository (model ≈ 325 MB).
set -euo pipefail
HOME_DIR="${PRICEWHY_HOME:-$HOME/.cache/pricewhy}"
VENV="$HOME_DIR/venv"
KDIR="$HOME_DIR/kokoro"
HF="https://huggingface.co/onnx-community/Kokoro-82M-v1.0-ONNX/resolve/main"
VOICES="af_heart af_bella am_michael bm_george"

mkdir -p "$KDIR"
if [ ! -x "$VENV/bin/python" ]; then
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install -q kokoro-onnx soundfile
fi
[ -s "$KDIR/model.onnx" ] || curl -sSL -o "$KDIR/model.onnx" "$HF/onnx/model.onnx"
for v in $VOICES; do
  [ -s "$KDIR/$v.raw" ] || curl -sSL -o "$KDIR/$v.raw" "$HF/voices/$v.bin"
done
if [ ! -s "$KDIR/voices.bin" ]; then
  KDIR="$KDIR" VOICES="$VOICES" "$VENV/bin/python" - <<'EOF'
import os, numpy as np
d = os.environ["KDIR"]
voices = {v: np.fromfile(f"{d}/{v}.raw", dtype=np.float32).reshape(-1, 1, 256)
          for v in os.environ["VOICES"].split()}
with open(f"{d}/voices.bin", "wb") as fh:
    np.savez(fh, **voices)
EOF
fi
command -v ffmpeg >/dev/null || { echo "ffmpeg is required"; exit 1; }
echo "ready: $VENV  $KDIR"
