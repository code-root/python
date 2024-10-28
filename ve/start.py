import os
from moviepy.editor import VideoFileClip

def compress_video(input_video_path, output_video_path, target_resolution=(1280, 720), bitrate="500k"):
    # قراءة الفيديو الأصلي
    video = VideoFileClip(input_video_path)

    # تغيير الدقة (يمكن ضبط target_resolution حسب الحاجة)
    video_resized = video.resize(target_resolution)

    # حفظ الفيديو الجديد مع تعديل الجودة (bitrate)
    video_resized.write_videofile(output_video_path, bitrate=bitrate, codec='libx264')

def compress_videos_in_folder(input_folder, output_folder, target_resolution=(1280, 720), bitrate="500k"):
    # التأكد من أن المجلد الناتج موجود، إذا لم يكن موجودًا يتم إنشاؤه
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # المرور على جميع الملفات في المجلد
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mov"):  # أنواع الفيديوهات التي نريد ضغطها
            input_video_path = os.path.join(input_folder, filename)
            output_video_path = os.path.join(output_folder, "compressed_" + filename)

            print(f"ضغط الفيديو: {filename}")
            compress_video(input_video_path, output_video_path, target_resolution, bitrate)

# مثال للاستخدام
input_folder = "/Users/macstoreegypt/Documents/Projects/python/ve/videos"  # مسار المجلد الذي يحتوي على الفيديوهات
output_folder = "/Users/macstoreegypt/Documents/Projects/python/ve/compressed_videos"  # مسار المجلد الذي سيتم حفظ الفيديوهات المضغوطة فيه
compress_videos_in_folder(input_folder, output_folder, target_resolution=(1280, 720), bitrate="500k")
