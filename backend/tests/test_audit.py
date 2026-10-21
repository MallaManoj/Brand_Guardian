"""
Unit tests for Brand Guardian AI data models and graph state schemas.
"""
import unittest
from backend.src.graph.state import VideoAuditState, ComplianceIssue


class TestBrandGuardianState(unittest.TestCase):
    def test_compliance_issue_structure(self):
        issue: ComplianceIssue = {
            "category": "FTC_DISCLOSURE",
            "description": "Missing clear and conspicuous disclosure in video opening.",
            "severity": "CRITICAL",
            "timestamp": "00:00:15"
        }
        self.assertEqual(issue["category"], "FTC_DISCLOSURE")
        self.assertEqual(issue["severity"], "CRITICAL")
        self.assertIsNotNone(issue["timestamp"])

    def test_state_initialization(self):
        state: VideoAuditState = {
            "video_url": "https://youtu.be/test_sample_123",
            "video_id": "vid_test123",
            "local_file_path": None,
            "video_metadata": {"duration": 45, "platform": "youtube"},
            "transcript": "Check out this guaranteed return product!",
            "ocr_text": ["Guaranteed Results"],
            "compliance_results": [],
            "final_status": "PENDING",
            "final_report": "",
            "errors": []
        }
        self.assertEqual(state["video_id"], "vid_test123")
        self.assertIn("duration", state["video_metadata"])
        self.assertEqual(len(state["compliance_results"]), 0)


if __name__ == "__main__":
    unittest.main()
