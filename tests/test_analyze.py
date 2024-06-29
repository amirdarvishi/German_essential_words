import pandas as pd
from src.analyze import get_word_frequencies

def test_get_word_frequencies():
    texts = ["beispieltext funktion testen", "funktion testen"]
    result_df = get_word_frequencies(texts)
    expected_data = {'word': ['funktion', 'testen', 'beispieltext'], 'frequency': [2, 2, 1]}
    expected_df = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_get_word_frequencies_empty():
    texts = []
    result_df = get_word_frequencies(texts)
    expected_df = pd.DataFrame(columns=['word', 'frequency'])
    pd.testing.assert_frame_equal(result_df, expected_df)
