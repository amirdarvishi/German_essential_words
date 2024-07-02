import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def clean_text(text):
    """
    Clean the input text by removing punctuation, converting to lowercase, and removing stopwords.
    
    Parameters:
    text (str): The input text to be cleaned.
    
    Returns:
    str: The cleaned text.
    """
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
     # Remove numbers
    text = re.sub(r'\b\d+\b', '', text)
    # Convert to lowercase
    text = text.lower()
    # Remove stopwords
    stop_words = set(stopwords.words('german'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text
