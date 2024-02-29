import os
from docx2pdf import convert

class ConvertMe:
    def __init__(self, input_file, output_file):
        self.inf = f"Word_file_here/{input_file}"
        self.of = f"Converted_files/{output_file}"
        self.convert_docx_to_pdf()

    @staticmethod
    def make_necessary_folders():
        main_dir = os.listdir()
        if ('Word_file_here' not in main_dir) or ('Word_file_here' not in main_dir):
            try:
                os.mkdir('Word_file_here')
            except FileExistsError:
                print('Folder Exists')
            try:
                os.mkdir('Converted_files')
            except FileExistsError:
                print('Folder Exists')
        return

    def convert_docx_to_pdf(self):
        self.make_necessary_folders()
        convert(self.inf, self.of)



# Usage
ConvertMe("Scripting.docx", "Scripting_pdf.pdf")

