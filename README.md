# German Words Analysis

## Project Overview

This project aims to identify the most important words in the German language using a dataset of 3 million sentences. The main objectives are to preprocess the data, analyze word frequencies, and determine key words for learning German. Additionally, the project includes data quality checks to ensure the dataset's integrity.

## Directory Structure

- `data/`: Contains the dataset file `german_sentences_sample.txt`.
- `src/`: Contains the source code for preprocessing, analyzing, and quality checking the data.
  - `preprocess.py`: Preprocessing functions for cleaning the text data.
  - `analyze.py`: Functions for analyzing word frequencies.
  - `quality_check.py`: Functions for checking data quality.
- `tests/`: Contains test cases for the source code.
  - `test_preprocess.py`: Tests for preprocessing functions.
  - `test_analyze.py`: Tests for analysis functions.
  - `test_quality_check.py`: Tests for data quality check functions.
- `requirements.txt`: Required Python packages.
- `README.md`: Project documentation.
- `main.py`: Main script to run the project.

## Setup Instructions

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/german-words-analysis.git
   cd german-words-analysis
2. Download the dataset from this link and place it in the data/ directory.

3. Install the required packages:
   ```sh
   pip install -r requirements.txt

4. Run the main script:
   ```sh
   python main.py

## Data Quality Checks
The data quality check function provides metrics on:

Total number of sentences
Number of empty sentences
Number of repeated sentences
These metrics help in understanding the quality and cleanliness of the dataset.