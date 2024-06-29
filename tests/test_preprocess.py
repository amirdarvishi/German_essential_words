import pytest
from src.preprocess import clean_text

def test_clean_text():
    input_text = "Das ist ein Beispieltext, um die Funktion zu testen!"
    expected_output = "beispieltext funktion testen"
    assert clean_text(input_text) == expected_output

def test_clean_text_with_stopwords():
    input_text = "Das ist ein weiterer Test für die Funktion!"
    expected_output = "weiterer test funktion"
    assert clean_text(input_text) == expected_output

def test_clean_text_empty():
    input_text = ""
    expected_output = ""
    assert clean_text(input_text) == expected_output
