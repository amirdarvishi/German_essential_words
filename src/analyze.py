from collections import Counter
import pandas as pd

def get_word_frequencies(texts):
    """
    Get the frequency of each word in the input texts.
    
    Parameters:
    texts (list of str): List of cleaned sentences.
    
    Returns:
    pandas.DataFrame: DataFrame with words and their frequencies.
    """
    word_list = ' '.join(texts).split()
    word_counts = Counter(word_list)
    word_freq_df = pd.DataFrame(word_counts.items(), columns=['word', 'frequency'])
    word_freq_df = word_freq_df.sort_values(by='frequency', ascending=False).reset_index(drop=True)
    return word_freq_df