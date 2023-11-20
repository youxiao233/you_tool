from PyPDF2 import *
# 输入路径
pdf1_path = 'test.pdf'
#输出路径
pdf2_path = 'demo.pdf'

reader1 = PdfReader(pdf1_path)
reader2 = PdfReader(pdf2_path)

writer = PdfWriter()

for page in reader1.pages:

    writer.add_page(page)

for page in reader2.pages:
    writer.add_page(page)

merged_pdf_path = 'merged.pdf'

# 将合并后的 PDF 写入文件
with open(merged_pdf_path, 'wb') as out:
    writer.write(out)

print(f"PDF files merged successfully into {merged_pdf_path}")