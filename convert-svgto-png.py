import os
import cairosvg

def convert_svg_to_png(directory):
    # الحصول على المسار الكامل للسكربت
    script_path = os.path.dirname(os.path.realpath(__file__))

    # التحرك في جميع الملفات في المجلد
    for filename in os.listdir(script_path):
        if filename.endswith('.svg'):
            # إنشاء المسار الكامل لملف SVG
            svg_path = os.path.join(script_path, filename)
            # إنشاء اسم الملف الجديد مع الامتداد PNG
            png_filename = os.path.splitext(filename)[0] + '.png'
            png_path = os.path.join(script_path, png_filename)

            # تحويل الملف من SVG إلى PNG
            cairosvg.svg2png(url=svg_path, write_to=png_path)
            print(f"تم تحويل {filename} إلى {png_filename}")

if __name__ == "__main__":
    convert_svg_to_png(os.getcwd())
