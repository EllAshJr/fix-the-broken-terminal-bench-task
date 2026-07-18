import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")
REQUIRED_KEYS = {"total_requests", "unique_ips", "top_path"}


def _load_report():
    assert REPORT_PATH.is_file(), "/app/report.json was not created"
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    assert isinstance(report, dict), "report.json must contain a JSON object"
    return report


def test_success_criterion_1_output_format():
    """Success criterion 1: the report is a JSON object with exactly the required keys and value types."""
    report = _load_report()
    assert set(report) == REQUIRED_KEYS
    assert type(report["total_requests"]) is int
    assert type(report["unique_ips"]) is int
    assert type(report["top_path"]) is str


def test_success_criterion_2_total_requests():
    """Success criterion 2: total_requests equals the number of non-empty log records."""
    assert _load_report()["total_requests"] == 6


def test_success_criterion_3_unique_ips():
    """Success criterion 3: unique_ips equals the number of distinct client IP addresses."""
    assert _load_report()["unique_ips"] == 3


def test_success_criterion_4_top_path():
    """Success criterion 4: top_path equals the most frequently requested request-target."""
    assert _load_report()["top_path"] == "/index.html"
