import PyPDF2

# rb是指可以讀然後轉成binary
with open("dummy.pdf", "rb") as file:
    print(file)
    # PdfFileReader只能讀binary mode
    reader = PyPDF2.PdfFileReader(file)
    # 有幾頁
    print(reader.numPages)
    # return pdf object
    print(reader.getPage(0))
    # 先取得頁面object，才能操作
    page_one = reader.getPage(0)
    # 跟課程不一樣，rotate也可以用
    print(page_one.rotate(90))
    print(page_one.rotateCounterClockwise(90))
    page_one.rotateCounterClockwise(90)

    # 創造writer object
    writer = PyPDF2.PdfFileWriter()
    # 把旋轉過的page_one加到writer object裡面
    writer.addPage(page_one)
    # 把writer object寫入open的dummy_rotated.pdf裡
    with open("dummy_rotated.pdf", "wb") as new_file:
        writer.write(new_file)
