from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

def search_google_cse(query, cse_url):
    """
    البحث في محرك بحث Google CSE واستخراج عناوين المواقع من نتائج البحث.
    """
    try:
        # إعداد المتصفح
        options = webdriver.FirefoxOptions()
        options.headless = False  # اجعلها True إذا كنت لا تريد عرض المتصفح
        driver = webdriver.Firefox(options=options)
        
        # فتح صفحة محرك البحث المخصص
        driver.get(cse_url)
        
        # انتظار ظهور مربع البحث
        wait = WebDriverWait(driver, 10)
        search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.gsc-input")))
        # إدخال استعلام البحث
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        
        # الانتظار لتحميل النتائج
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.gsc-result")))
        
        # استخراج عناوين المواقع
        results = []
        for item in driver.find_elements(By.CSS_SELECTOR, "div.gsc-result"):
            try:
                title = item.find_element(By.CSS_SELECTOR, "a.gs-title").text
                link = item.find_element(By.CSS_SELECTOR, "a.gs-title").get_attribute("href")
                results.append({"title": title, "link": link})
            except Exception as e:
                print(f"Error extracting result: {e}")
        
        driver.quit()
        return results
    except Exception as e:
        print(f"Error during search: {e}")
        driver.quit()
        return []

# البحث باستخدام محرك البحث المخصص
cse_url = "https://cse.google.com/cse?cx=7326e907b1a7f42cd"
search_query = "Cosmetic number Cairo"
results = search_google_cse(search_query, cse_url)

# عرض النتائج
if results:
    print(f"Found {len(results)} results:")
    for result in results:
        print(f"Title: {result['title']}")
        print(f"URL: {result['link']}")
        print("-" * 50)
else:
    print("No results found.")
