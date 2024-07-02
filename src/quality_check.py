def check_data_quality(sentences):
    """
    Check the data quality of the sentences.
    
    Parameters:
    sentences (list of str): List of sentences.
    
    Returns:
    dict: Dictionary with quality metrics.
    """
    total_sentences = len(sentences)
    empty_sentences = sum(1 for sentence in sentences if not sentence.strip())
    repeated_sentences = len(sentences) - len(set(sentences))

    quality_metrics = {
        "total_sentences": total_sentences,
        "empty_sentences": empty_sentences,
        "repeated_sentences": repeated_sentences,
    }
    return quality_metrics
