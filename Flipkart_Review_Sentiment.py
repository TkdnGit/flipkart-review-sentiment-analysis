from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains
from textblob import TextBlob

from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.chrome.options import Options
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
options = Options()


time.sleep(random.uniform(1.5,4.5))
options.add_argument("--lang=en-US")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches",["enable-logging"])
options.add_argument("--disable-info-bars")
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver,100)
all_profile_list = []
all_data_urls = []
all_data = []
driver.get("https://www.flipkart.com/myxes-new-tws-m19-gaming-earbuds-bluetooth-5-0-wireless-led-digital-display-n8/product-reviews/itmf139fdf9c0e1c?pid=ACCGHHZ9VG3JNAUV&lid=&sortOrder=MOST_HELPFUL&certifiedBuyer=false&aid=overall&pageUID=1788883357332")
def auto_scroll():
        actions =ActionChains(driver)
        time.sleep(random.uniform(1.5, 3))
        actions.move_by_offset(120,100).click().perform()
        for i in range(30):
            # actions.scroll_by_amount(0,300).perform()
            actions.send_keys(Keys.PAGE_DOWN).perform()   
            time.sleep(random.uniform(1.5, 3)) 
            
               
time.sleep(random.uniform(1.5, 3))
auto_scroll()
time.sleep(10)
data = []
reviews = driver.find_elements(By.XPATH, "//div[contains(text(),'Review for:')]//following-sibling::div[1]")
for review in reviews:
    review_text = review.text.strip()
    cleaned_review = re.sub(r'\s+', ' ', review_text)
    Final_review = re.sub(r'[^\w\s]', '', cleaned_review)
    data.append(Final_review)

df = pd.DataFrame(data, columns=['Review'])

df['Sentiment'] = df['Review'].apply(lambda x: TextBlob(x).sentiment.polarity)
df["Sentiment"] = df["Sentiment"].apply(lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Neutral"))

df.to_excel('Output_flipkart_reviews_sentiment.xlsx', index=False)
df.to_csv('Output_flipkart_reviews_sentiment.csv', index=False)

print(f"\n Sentiment Distribution:(Count):Total Sentiments: {df['Sentiment'].value_counts().sum()}\n", df['Sentiment'].value_counts())
sentiment_percentages = (df['Sentiment'].value_counts(normalize=True).mul(100).round(2))

print(f"\n Sentiment Percentages:(%):Total Sentiments: {df['Sentiment'].value_counts().sum()}\n", sentiment_percentages)
print("\nSentiment Distribution Bar Chart")
print("=" * 50)
for sentiment in ["Positive", "Neutral", "Negative"]:    
    percentage = sentiment_percentages.get(sentiment, 0)    
    bar_length = int(percentage/5)    
    bar = "█" * bar_length    
    print(f"{sentiment:<9} {bar:<40} {percentage:.2f}% \n")
driver.quit()



