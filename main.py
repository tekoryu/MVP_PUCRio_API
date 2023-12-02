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

def convert_pdf_to_text(pdf_file: str,
                        footer: float,
                        header: float,
                        line_overlap: float,
                        line_margin: float,
                        char_margin: float,
                        ):
    """
    :param pdf_file:
        Path to the pdf file
    :param footer:
        from a x, y perspective, where starts the footer to be ignored
    :param header:
        from a x, y perspective, where starts the header to be ignored
    :param line_overlap:
        If two characters have more overlap than this they are considered to be on the same line.
        The overlap is specified relative to the minimum height of both characters.
    :param line_margin:
        If two lines are are close together they are considered to be part of the
        same paragraph. The margin is specified relative to the height of a line.
    :param char_margin:
        If two characters are closer together than this margin they are considered part of the same line.
        The margin is specified relative to the width of the character.
    :return:
        str:
        Arquivo convertido
    """

    output_list = []
    output_string = ""

    # Parâmetros de leitura do layout da página: line_overlap: float = 0.5, char_margin: float = 2.0, line_margin:
    # float = 0.5, word_margin: float = 0.1, boxes_flow: Optional[float] = 0.5, detect_vertical: bool = False,
    # all_texts: bool = False
    laparams = LAParams(line_overlap=line_overlap, line_margin=line_margin, char_margin=char_margin )

    # Extrai as variáveis de trabalho
    for page_layout in extract_pages(pdf_file, laparams=laparams):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                if footer < element.y0 < header:
                    output_list.append(element)
                    output_string = output_string + element.get_text()

    return output_string, output_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    texto, lista = convert_pdf_to_text("training_files/Projeto de Lei.pdf",
                                       70,
                                       800,
                                       0.001,
                                       1.35,
                                       3.0
                                       )

    timestamp = datetime.datetime.timestamp(datetime.datetime.now())

    # output to file
    text_file = open(f"outputs/data{timestamp}.txt", "w")
    text_file.write(texto)
    text_file.close()

    #Lista
    print(len(lista))
    print(lista[36])
