from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import tempfile
import os


def pdf_2_image():
    with tempfile.TemporaryDirectory() as path:
        file_path, output_path = os.path.abspath('pdf_file/BW.pdf'), os.path.abspath('images_from_pdf_demo')

        images_from_path = convert_from_path(file_path,
                                             output_folder=output_path)
