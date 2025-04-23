import fitz  # PyMuPDF

def resize_pdf(input_path, output_path, scale_percent=91.48):
    # Buka dokumen sumber
    src_doc = fitz.open(input_path)
    # Buat dokumen hasil
    new_doc = fitz.open()

    scale = scale_percent / 100.0

    for page_num in range(len(src_doc)):
        page = src_doc.load_page(page_num)
        rect = page.rect
        new_width = rect.width * scale
        new_height = rect.height * scale

        # Buat halaman baru di dokumen hasil
        new_page = new_doc.new_page(width=new_width, height=new_height)

        # Tempelkan isi halaman dari dokumen sumber
        new_page.show_pdf_page(
            fitz.Rect(0, 0, new_width, new_height),
            src_doc,        # sumber dari dokumen asli
            page_num,       # nomor halaman sumber
            fitz.Matrix(scale, scale)
        )

    # Simpan dokumen hasil
    new_doc.save(output_path)
    new_doc.close()
    src_doc.close()

    print(f"✅ PDF diskalakan ke {scale_percent}% dan disimpan ke:\n{output_path}")

# Contoh pemanggilan
input_pdf_path = r"C:\Users\izanm\Downloads\bb 300 otw.pdf"
output_pdf_path = r"C:\Users\izanm\Downloads\bb_300_insyaAllah_fix.pdf"

resize_pdf(input_pdf_path, output_pdf_path)
