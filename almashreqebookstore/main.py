import pandas as pd
import json
import os

def excel_to_json(excel_file_path, output_dir, rows_per_file=100):
    # قراءة ملف الإكسيل وتخطي أول صفين
    df = pd.read_excel(excel_file_path, skiprows=2)

    # التأكد من وجود المجلد، وإنشاؤه إذا لم يكن موجوداً
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # تقسيم البيانات إلى أجزاء كل منها يحتوي على rows_per_file صف
    for i in range(0, len(df), rows_per_file):
        chunk = df.iloc[i:i+rows_per_file]
        json_data = chunk.to_json(orient='records', force_ascii=False)
        
        json_file_path = os.path.join(output_dir, f"part_{i//rows_per_file + 1}.json")
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json_file.write(json_data)

        print(f"تم تحويل الجزء {i//rows_per_file + 1} بنجاح إلى {json_file_path}")

# احصل على المجلد الحالي حيث يوجد السكربت
current_directory = os.path.dirname(os.path.abspath(__file__))

# البحث عن جميع ملفات الإكسيل في المجلد الحالي
for file_name in os.listdir(current_directory):
    if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
        excel_file_path = os.path.join(current_directory, file_name)
        base_name = file_name.rsplit('.', 1)[0]
        output_dir = os.path.join(current_directory, base_name)

        # تحويل ملف الإكسيل إلى JSON مجزأ ووضع الملفات في المجلد الجديد
        excel_to_json(excel_file_path, output_dir, rows_per_file=100)
