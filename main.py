import pandas as pd
from src.preprocess import clean_text
from src.analyze import get_word_frequencies
from src.quality_check import check_data_quality

#source 
def main():
    # Load the data
    with open('data/deu_news_2015_3M-sentences.txt', 'r', encoding='utf-8') as file:
        sentences = file.readlines()

    # Check data quality
    quality_metrics = check_data_quality(sentences)
    print("Data Quality Metrics:", quality_metrics)
    
    # Preprocess the data
    cleaned_sentences = [clean_text(sentence) for sentence in sentences]
    
    # Analyze word frequencies
    
    # Save the results to a CSV file
    return 0

if __name__ == "__main__":
    main()