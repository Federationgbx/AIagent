#!/usr/bin/env python3
"""Tests for review.py using SAMPLE (fictional) data.

The fixture in fixtures/SAMPLE_table_data.csv is invented on purpose — it only
checks that parsing, averages and the A/B/C rules work. It is NOT channel data.

Run: python3 tools/analytics/test_review.py
"""
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import review  # noqa: E402

FIXTURE = HERE / "fixtures" / "SAMPLE_table_data.csv"


class ReviewTests(unittest.TestCase):
    def setUp(self):
        self.videos = review.load_export(FIXTURE)
        self.avg = review.classify(self.videos)
        self.by_title = {v.title: v for v in self.videos}

    def test_total_row_skipped(self):
        self.assertEqual(len(self.videos), 5)

    def test_duration_parsing(self):
        self.assertEqual(review._duration("0:05:36"), 336)
        self.assertEqual(review._duration("4:12"), 252)
        self.assertIsNone(review._duration(""))

    def test_channel_average_ignores_too_new(self):
        # (10 + 5 + 1.7 + 5) / 4 ; the 400-impression video is excluded
        self.assertAlmostEqual(self.avg["ctr"], 5.425)

    def test_groups(self):
        self.assertEqual(self.by_title["SAMPLE Strong video"].group, "A")
        self.assertEqual(self.by_title["SAMPLE Average video"].group, "B")
        self.assertEqual(self.by_title["SAMPLE Weak thumbnail"].group, "C")
        self.assertEqual(self.by_title["SAMPLE Weak hook"].group, "C")
        self.assertEqual(self.by_title["SAMPLE Too new"].group, "too early")

    def test_diagnosis_points_to_the_right_fix(self):
        thumb_notes = " ".join(self.by_title["SAMPLE Weak thumbnail"].notes)
        hook_notes = " ".join(self.by_title["SAMPLE Weak hook"].notes)
        self.assertIn("Packaging problem", thumb_notes)
        self.assertIn("hook mismatch", hook_notes)
        self.assertIn("Few subscribers", hook_notes)

    def test_tag_breakdown_with_log(self):
        with tempfile.TemporaryDirectory() as tmp:
            log = Path(tmp) / "log.csv"
            log.write_text(
                "id,title,youtube_id,pillar,structure,hook_type,title_formula,thumb_template\n"
                "1,SAMPLE Strong video,SAMPLE001,Cost Autopsy,Autopsy,1,1,B\n"
                "2,SAMPLE Weak thumbnail,SAMPLE003,Cost Autopsy,Autopsy,2,4,A\n",
                encoding="utf-8",
            )
            review.attach_tags(self.videos, log)
            tags = review.tag_breakdown(self.videos)
        self.assertEqual(tags["pillar"]["Cost Autopsy"]["n"], 2)
        self.assertEqual(set(tags["thumb_template"]), {"A", "B"})

    def test_report_renders(self):
        text = review.render(self.videos, self.avg, {}, "fixture")
        self.assertIn("## Channel averages", text)
        self.assertIn("SAMPLE Weak hook", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
