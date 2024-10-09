import pandas as pd
import json
import os

# تحميل ملف CSV الكبير
csv_file = 'all-vehicles-model.csv'  # استبدل هذا باسم ملف CSV الخاص بك

# قراءة ملف CSV باستخدام pandas
df = pd.read_csv(csv_file)

# تقسيم البيانات إلى أجزاء تحتوي كل جزء على 300 صف
chunk_size = 300
total_rows = len(df)
chunks = [df[i:i + chunk_size] for i in range(0, total_rows, chunk_size)]

# التأكد من وجود مجلد لتخزين ملفات JSON
output_dir = 'json_chunks'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# دالة لتحويل قيم DataFrame إلى التنسيق المطلوب
def convert_types(chunk):
    # تحويل القيم المناسبة إلى النوع المطلوب
    chunk = chunk.where(pd.notnull(chunk), None)  # استبدال القيم الفارغة بـ None لتصبح null في JSON
    return chunk.to_dict(orient='records')

# حفظ كل جزء من البيانات في ملف JSON منفصل
for i, chunk in enumerate(chunks):
    json_file = os.path.join(output_dir, f'chunk_{i + 1}.json')
    
    # تحويل البيانات للتنسيق المطلوب
    chunk_records = convert_types(chunk)
    
    # كتابة البيانات في ملف JSON
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(chunk_records, f, ensure_ascii=False, indent=4)
    
    print(f'تم إنشاء {json_file}')
