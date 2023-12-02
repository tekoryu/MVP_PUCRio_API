"""
File: main.py
Author: Anderson Monteiro
Date: 26-11-2023
Description: Reads a PDF file, try to recover original format
and structures data contained in the file

Additional Information:
- The goal public is Legislative Assessment bodies in Brazil. This version
is refined only to Senate propositions.
"""
import datetime

from pdfminer.high_level import extract_text, extract_pages
from pdfminer.layout import LTTextContainer, LAParams

from convert_pdf import convert_pdf


def convert_pdf_to_text(pdf_file: str, footer: float, header: float):
    #   Lê um arquivo PDF e retorna texto cru

    output_list = []
    output_string = ""

    laparams = LAParams(line_overlap=0.1)
    for page_layout in extract_pages(pdf_file, laparams=laparams):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                if footer < element.y0 < header:
                    output_list.append(element)
                    output_string = output_string + element.get_text()

    return output_string


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    texto = convert_pdf_to_text("training_files/Projeto de Lei.pdf", 70, 800)
    timestamp = datetime.datetime.timestamp(datetime.datetime.now())

    # output to file
    text_file = open(f"outputs/data{timestamp}.txt", "w+")
    text_file.write(texto)
    text_file.close()
