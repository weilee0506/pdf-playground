import PyPDF2

template = PyPDF2.PdfFileReader(open("super.pdf", "rb"))

watermark = PyPDF2.PdfFileReader(open("wtr.pdf", "rb"))

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    # 建立template每一頁的object
    page = template.getPage(i)
    # 使用PdfFileWriter的mergePage是把兩頁合併到一頁
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open("watermarked_output", "wb") as file:
    output.write(file)
