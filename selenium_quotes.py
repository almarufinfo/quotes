import mysql.connector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

db = mysql.connector.connect(
    host ="localhost",
    user="root",
    password="",
    database="quotes_db"
)

cursor = db.cursor()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://quotes.toscrape.com/js')
time.sleep(3)


    
while True:
    
     quotes = driver.find_elements(By.CLASS_NAME, "quote")
        
     for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, "text").text
        author= quote.find_element(By.CLASS_NAME, "author").text
        print(f"{(text)} - {(author)}")
            
        # writer.writerow([text, author])
            
            
        sql = "INSERT INTO quotes (quote, author) VALUES (%s, %s)"
        val =(text, author)
        cursor.execute(sql, val)
        db.commit()
            
     try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'li.next > a')
        next_button.click()
        time.sleep(3)
            
     except:
        print("All pages scraped successfully!")
        break        

        
    


    
driver.quit()
cursor.close()
db.close()
