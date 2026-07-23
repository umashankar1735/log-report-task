import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.exists(), "report.json was not created"
    with REPORT_PATH.open() as f:
        return json.load(f)


def test_output_is_valid_json():
    """Success Criterion 4: The output must be valid JSON written to /app/report.json."""
    report = load_report()
    assert isinstance(report, dict)


def test_total_requests():
    """Success Criterion 1: Include total_requests."""
    report = load_report()
    assert report.get("total_requests") == 6


def test_unique_ips():
    """Success Criterion 2: Include unique_ips."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Success Criterion 3: Include top_path."""
    report = load_report()
    assert report["top_path"] == "/index.html"