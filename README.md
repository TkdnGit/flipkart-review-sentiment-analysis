# Flipkart Review Sentiment Analysis

A Python-based web scraping and sentiment analysis project that collects customer reviews from a Flipkart product review page, cleans the review text, performs sentiment classification, and exports the results to Excel/CSV.

## Project Overview

This project uses Selenium to collect customer reviews from a Flipkart product review page and TextBlob to perform sentiment analysis.

The scraper automatically:

* Opens the Flipkart product review page
* Scrolls through the review section
* Extracts customer reviews
* Cleans unnecessary whitespace and special characters
* Removes duplicate reviews
* Performs sentiment analysis
* Classifies reviews as Positive, Negative, or Neutral
* Calculates sentiment distribution
* Calculates sentiment percentages
* Exports the results to an Excel/CSV file

## Features

* Automated browser interaction with Selenium
* Dynamic review collection
* Automatic scrolling
* Review text cleaning
* Duplicate removal
* Sentiment polarity analysis
* Positive / Negative / Neutral classification
* Sentiment percentage calculation
* Excel/CSV export
* Error handling
* Logging
* Configurable product URL
* Configurable number of scrolls

## Technologies Used

| Technology        | Purpose                             |
| ----------------- | ----------------------------------- |
| Python            | Core programming language           |
| Selenium          | Browser automation and web scraping |
| TextBlob          | Sentiment analysis                  |
| Pandas            | Data processing                     |
| OpenPyXL          | Excel file generation               |
| webdriver-manager | ChromeDriver management             |
| Chrome WebDriver  | Browser automation                  |

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/TkdnGit/flipkart-review-sentiment-analysis.git
```

### 2. Open the project

```bash
cd flipkart-review-sentiment-analysis
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the scraper:

```bash
python Flipkart_Review_Sentiment.py
```

The script will:

1. Open Chrome
2. Navigate to the configured Flipkart review page
3. Scroll through the review section
4. Extract reviews
5. Clean the data
6. Analyze sentiment
7. Display sentiment statistics
8. Save the results to Excel

## Output

The generated Excel file contains:

| Column    | Description                    |
| --------- | ------------------------------ |
| Review    | Cleaned customer review        |
| Sentiment | Positive, Negative or Neutral |

Example:

| Review                                  | Sentiment |
| --------------------------------------- | --------- |
| Excellent product and very good quality | Positive  |
| Product stopped working after two days  | Negative  |
| Product is okay                         | Neutral   |

## Sentiment Analysis

TextBlob calculates sentiment polarity between:

```text
-1.0  → Very Negative
 0.0  → Neutral
+1.0  → Very Positive
```

The project uses the following classification:

```python
if polarity > 0:
    Positive
elif polarity < 0:
    Negative
else:
    Neutral
```

## Example Output

```text
Sentiment Distribution:(Count):Total Sentiments: 50

Positive    25
Neutral      8
Negative     7

 Sentiment Percentages:(%):Total Sentiments: 50

Positive    62.50
Neutral     20.00
Negative    17.50

Sentiment Distribution Bar Chart
==================================================
Positive  ███████████████                          78.00% 

Neutral   ██                                       12.00% 

Negative  ██                                       10.00%
```

## Data Processing Pipeline

```text
Flipkart Product Reviews
          ↓
     Selenium
          ↓
    Review Extraction
          ↓
      Text Cleaning
          ↓
    Duplicate Removal
          ↓
    TextBlob Analysis
          ↓
 Positive / Negative / Neutral
          ↓
      Pandas DataFrame
          ↓
       Excel/CSV Export
```

## Project Improvements

Future versions can include:

* Aspect-Based Sentiment Analysis (ABSA) & Business Insight
* Review rating extraction
* Reviewer name extraction
* Review date extraction
* Verified Buyer detection
* Product name extraction
* Review pagination
* Sentiment polarity score
* Sentiment visualization
* SQLite database storage
* Automated reports



## Disclaimer

This project is created for educational, portfolio, and data-analysis purposes.

Users should respect the target website's Terms of Service, robots.txt, rate limits, and applicable laws when collecting publicly available data.

## Author

**Tapu Kumar Debnath**

### Skills Demonstrated

* Python
* Selenium
* Web Scraping
* Data Cleaning
* Pandas
* Sentiment Analysis
* Excel/CSV Automation
* Data Processing
* Browser Automation

## License

This project is intended for educational and portfolio purposes.
