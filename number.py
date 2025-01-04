import requests
from bs4 import BeautifulSoup
import json
import random
import time

# ملف لحفظ البيانات
output_file = "data.json"

# التأكد من أن البيانات غير مكررة
unique_data = set()

# دالة لجلب البيانات من صفحة محددة
def fetch_data_from_page(page_number):
    url = f"https://dalil.egyfinder.com/categories/ar/bedding?p={page_number}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to access page {page_number}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all("div", class_="_itemBox")

    data = []
    for item in items:
        entry = {}

        # استخراج الاسم
        name_tag = item.find("span", itemprop="name")
        entry["name"] = name_tag.text.strip() if name_tag else None

        # استخراج الهاتف
        phone_tag = item.find("span", itemprop="telephone")
        phone = phone_tag.text.strip() if phone_tag else None
        if phone and phone.startswith("01"):
            entry["phone"] = phone
        else:
            continue

        # استخراج العنوان
        address_tag = item.find("span", class_="text-black-50")
        entry["location"] = address_tag.text.strip() if address_tag else None

        # استخراج ا��موقع الإلكتروني
        website_tag = item.find("a", rel="nofollow")
        entry["website"] = website_tag["href"].strip() if website_tag else None

        # التحقق من أن البيانات غير مكررة
        entry_tuple = tuple(entry.items())
        if entry_tuple not in unique_data:
            unique_data.add(entry_tuple)
            data.append(entry)

    return data

# جمع البيانات من الصفحات من 1 إلى 100
def scrape_data():
    all_data = []

    for page in range(1, 9):
        print(f"جلب البيانات من الصفحة {page}...")
        page_data = fetch_data_from_page(page)
        if page_data:
            all_data.extend(page_data)

    return all_data

# حفظ البيانات في ملف JSON
def save_to_json(data, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# إرسال البيانات إلى API
# إرسال البيانات إلى API بشكل تدريجي
def send_data_to_api(data, session_id):
    url = f"http://85.17.106.209:3000/{session_id}/messages/send/bulk"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "a6bc226axxxxxxxxxxxxxxxxxxxx"
    }    
    # تحديد حجم الدفعة
    batch_size = 1  # يمكنك تعديل هذا الرقم حسب الحاجة
    delay = random.randint(1, 40)
    
    # تقسيم البيانات إلى دفعات صغيرة
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        payload = []
        
        for entry in batch:
            if entry.get("phone"):
                message = {
                    "jid": f"2{entry['phone']}@s.whatsapp.net",
                    "type": "number",
                    "delay": delay,
                    "message": {
                        "text": """
مساء الخير / صباح الخير 🌟
إزايك؟ يا رب تكون بخير!
إحنا شركة متخصصة في البرمجة وتطوير المواقع والتطبيقات، وهدفنا نساعدك تطوّر أعمالك في مجال المفروشات وتعرض منتجاتك بشكل احترافي للعملاء. سواء كنت محتاج موقع إلكتروني يعرض تشكيلتك من المفروشات أو تطبيق موبايل يسهل على عملائك التسوق وشراء منتجاتك أونلاين، إحنا هنا عشان نوفّر ليك أفضل الحلول التقنية بأعلى جودة وأسرع وقت.
كمان لو عندك فكرة أو مشروع جديد عايز تطوّره لمتجرك أو شركتك المتخصصة في المفروشات، إحنا جاهزين نساعدك ونعمل معاك على تصميم وتطوير حلول تقنية تلبي احتياجات عملائك وتسهل عليهم تجربة التسوق.
تواصل معانا دلوقتي وهنكون سعداء نقدم ليك أفضل العروض:
📞 رقم التليفون: 01001995914

مستنيينك! 😊
"""
                    }
                }
                payload.append(message)
        
        # إرسال الدفعة إلى API
        response = requests.post(url, headers=headers, json=payload, params={"sessionId": session_id})
        
        if response.status_code == 200:
            print(f"Batch {i // batch_size + 1} sent successfully")
        else:
            print(f"Error sending batch {i // batch_size + 1}: {response.status_code} - {response.text}")
        
        # إضافة تأخير عشوائي بين 1 و 6 ثواني
        time.sleep(random.randint(1, 15))

# استخدام الكود مع بياناتك
if __name__ == "__main__":
    data = scrape_data()  # جمع البيانات
    save_to_json(data, output_file)
    print(f"تم حفظ {len(data)} إدخال في الملف {output_file}.")
    
    # إرسال البيانات إلى API
    session_id = "sofa"
    send_data_to_api(data, session_id)