from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url="https://quotes.toscrape.com/js"
driver.get(url)
time.sleep(3)


with open('quotes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author'])
    
    while True:
        quotes = driver.find_elements(By.CLASS_NAME, "quote")
        
        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, "text").text
            author= quote.find_element(By.CLASS_NAME, "author").text
            print(f"{(text)} - {(author)}")
            
            writer.writerow([text, author])
            
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, 'li.next > a')
            next_button.click()
            time.sleep(3)
            
        except:
            print("All pages scraped successfully!")
            break        

        
    


    
driver.quit()