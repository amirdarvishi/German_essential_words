import pytest
from src.quality_check import check_data_quality

def test_check_data_quality():
    sentences = ["Dies ist ein Satz.", "Dies ist ein weiterer Satz.", "Dies ist ein Satz."]
    expected_output = {
        "total_sentences": 3,
        "empty_sentences": 0,
        "repeated_sentences": 1
    }
    assert check_data_quality(sentences) == expected_output

def test_check_data_quality_with_empty():
    sentences = ["Dies ist ein Satz.", "", "Dies ist ein weiterer Satz."]
    expected_output = {
        "total_sentences": 3,
        "empty_sentences": 1,
        "repeated_sentences": 0
    }
    assert check_data_quality(sentences) == expected_output