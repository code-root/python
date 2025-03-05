    public function viewCoverImage(Request $request)
    {
        try {
            $coverImage = CoverImage::where('book_ISBN', $request->isdn)->first()['cover_image_path'] ?? 'default.png';

            if (!Storage::exists($coverImage)) {
                $coverImage = $this->path_covers.'default.png';
            }

            $filePath = Storage::path($coverImage);
            if (file_exists($filePath)) {
                return response()->file($filePath, [
                    'Content-Type' => mime_content_type($filePath), // تحديد نوع المحتوى ديناميكيًا
                    'Content-Disposition' => 'inline', // عرض الملف في المتصفح
                ]);
            } else {
                return response()->json(['error' => 'Default image not found'], 404);
            }
        } catch (\Exception $e) {
            return response()->json(['error' => 'Default image not found'], 404);

        }
    } 