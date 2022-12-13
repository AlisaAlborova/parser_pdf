from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
import re
import csv

txt = 0


# -----------Функция нормализации текста---------------------------------
def get_tokens(line):
    line = re.sub(r'[^\w\s]+|[\d]+', r'', line).strip()
    line = line.replace('.', '').replace(';', '').replace('\n', '').replace(':','').replace(',', '').lower()
    return line


# -----------Функция для записи из пдф файла в txt---------------------------------
def pdf_to_text(input_file, output):
    global txt
    i_f = open(input_file, 'rb')
    resMgr = PDFResourceManager()
    retData = io.StringIO()
    TxtConverter = TextConverter(resMgr, retData, laparams=LAParams())
    interpreter = PDFPageInterpreter(resMgr, TxtConverter)
    for page in PDFPage.get_pages(i_f):
        interpreter.process_page(page)
    txt = retData.getvalue()
    txt = get_tokens(txt)
    with open(output, 'w') as of:
        of.write(txt)


sp = []  # список текстов


# -----------Функция для записи из txt файла в csv---------------------------------
def export_as_csv(csv_path):
    global input_pdf
    global output_txt
    with open(csv_path, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=' ', lineterminator='\n')
        for i in range(len(input_pdf)):  # Запись в txt файл
            pdf_to_text(input_pdf[i], output_txt[i])
            writer.writerow([''.join(txt)])




input_pdf = ['1.pdf', '2.pdf', '3.pdf', '5.pdf', '6.pdf', '7.pdf', '8.pdf', '9.pdf',
                 '10.pdf', '11.pdf', '12.pdf', '13.pdf', '14.pdf', '15.pdf', '16.pdf',
                 '17.pdf',
                 '18.pdf', '19.pdf', '20.pdf', '21.pdf', '22.pdf', '23.pdf', '24.pdf',
                 '25.pdf',
                 '26.pdf', '27.pdf', '28.pdf', '29.pdf', '30.pdf']

output_txt = ['1.txt', '2.txt', '3.txt', '5.txt', '6.txt', '7.txt', '8.txt', '9.txt',
                  '10.txt', '11.txt', '12.txt', '13.txt', '14.txt', '15.txt', '16.txt',
                  '17.txt',
                  '18.txt', '19.txt', '20.txt', '21.txt', '22.txt', '23.txt', '24.txt',
                  '25.txt',
                  '26.txt', '27.txt', '28.txt', '29.txt', '30.txt']

# -------------------Запись в csv файл--------------------
csv_path = 'w9.csv'
export_as_csv(csv_path)
