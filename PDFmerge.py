import sys
# 需要在pycharm之外自己另外pip install PyPDF2
import PyPDF2


# 從第[1]開始拿可以拿到所有input
inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    # merger不需要用with open去開啟pdf也可以操作
    # 在append時是把一頁加到一頁後面
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write("super.pdf")


pdf_combiner(inputs)
