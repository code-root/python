from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# إعداد المتصفح
options = webdriver.FirefoxOptions()
# يمكنك إلغاء تفعيل headless إذا كنت ترغب في مشاهدة ما يحدث في المتصفح
options.headless = False  
driver = webdriver.Firefox(options=options)

try:
    # فتح موقع Google Maps
    driver.get('https://www.google.com/maps/')
    time.sleep(5)  # الانتظار حتى يتم تحميل الصفحة بالكامل

    # العثور على صندوق البحث وإدخال الاستعلام
    search_box = driver.find_element(By.ID, 'searchboxinput')
    query = 'مطعم طنطا'
    search_box.send_keys(query)
    
    # الضغط على زر البحث
    search_button = driver.find_element(By.ID, 'searchbox-searchbutton')
    search_button.click()
    time.sleep(5)  # الانتظار حتى يتم تحميل النتائج

    # التمرير داخل العنصر الذي يحتوي على الكلاس "aIFcqe" لجلب المزيد من النتائج
    for _ in range(10):  # يمكنك تعديل العدد هنا للتحكم في كمية التمرير
        scrollable_element = driver.find_element(By.CLASS_NAME, 'aIFcqe')
        driver.execute_script('arguments[0].scrollBy(0, 500);', scrollable_element)
        time.sleep(1)  # الانتظار قليلاً بين عمليات التمرير

    # استخراج البيانات من النتائج
    results = []
    elements = driver.find_elements(By.CSS_SELECTOR, 'div.Nv2PK.THOPZb.CpccDe')
    for element in elements:
        name = element.find_element(By.CSS_SELECTOR, '.qBF1Pd.fontHeadlineSmall').text if element.find_elements(By.CSS_SELECTOR, '.qBF1Pd.fontHeadlineSmall') else 'N/A'
        link = element.find_element(By.CSS_SELECTOR, 'a.hfpxzc').get_attribute('href') if element.find_elements(By.CSS_SELECTOR, 'a.hfpxzc') else 'N/A'
        reviews = element.find_element(By.CSS_SELECTOR, '.e4rVHe').text if element.find_elements(By.CSS_SELECTOR, '.e4rVHe') else 'N/A'
        results.append({'name': name, 'link': link, 'reviews': reviews})

    # طباعة النتائج
    for result in results:
        print(result)

finally:
    # إغلاق المتصفح
    driver.quit()
