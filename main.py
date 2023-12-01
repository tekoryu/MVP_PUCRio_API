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
from pdfminer.high_level import extract_text, extract_pages
from pdfminer.layout import LTTextContainer, LAParams


def box_analyzer(element: LTTextContainer):
    texticulo = element.get_text()
    artigos

def convert_pdf_to_text(pdf_file: str, footer: float, header: float):
    #   Lê um arquivo PDF e retorna texto cru

    output_string = []
    laparams = LAParams(line_overlap=0.1)
    for page_layout in extract_pages(pdf_file, laparams=laparams):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                if footer < element.y0 < header:
                    output_string.append(element)
                    # output_string = output_string + element.get_text()

    return output_string

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    convert_pdf_to_text("training_files/Projeto de Lei.pdf", 70, 800)
