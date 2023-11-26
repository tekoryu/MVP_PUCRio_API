"""
File: main.py
Author: Anderson Monteiro
Date: 26-11-2023
Description: Reads a PDF file, try to recover original format
and structures data contained in the file

Additional Information:
- The main public is Legislative Assessment bodies in Brazil.
"""
from pdfquery import PDFQuery
from PyPDF2 import PdfReader
from pdfminer.high_level import extract_text, extract_pages


def read_pdfquery(pdf_file):
    # Lê um arquivo PDF e retorna texto cru
    pdf = PDFQuery(pdf_file)
    pdf.load()

    # Use CSS-like selectors to locate the elements
    text_elements = pdf.pq('LTTextLineHorizontal')

    # Extract the text from the elements
    text = [t.text for t in text_elements]
    pdf.tree.write('pdfXML.txt', pretty_print=True)
    print(text)

def read_py2pdf(pdf_file):
    # Lê um arquivo PDF e retorna texto cru
    reader = PdfReader(pdf_file)
    page = reader.pages[1]
    print(page.extract_text())

def read_pdfminersix(pdf_file):
    # Lê um arquivo PDF e retorna texto cru
    for page_layout in extract_pages(pdf_file):
        for element in page_layout:
            print(element)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #read_pdfquery("training_files/Projeto de Lei.pdf")
    #read_py2pdf("training_files/Projeto de Lei.pdf")
    read_pdfminersix("training_files/Projeto de Lei.pdf")
