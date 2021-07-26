from watchdog.events import FileCreatedEvent
from PyPDF2 import PdfFileMerger, PdfFileReader
import os


class OnChange():
    def dispatch(self, event):
        if isinstance(event, FileCreatedEvent):

            print("New File Detected")

            file_name = None

            if "Cover" in os.path.basename(event.src_path):
                file_name = os.path.basename(event.src_path).replace("Cover Letter for ", "")
            else:
                file_name = os.path.basename(event.src_path).replace("への送付状", "")

            name_of_company = file_name.replace(".pdf", "")
            merged_letter_dir = f"C:/Users/russ1/Documents/Important Documents/Resume/Software Engineer/Resume w Cover Letter/{name_of_company}/"
            print(f"Creating directory for {name_of_company}")
            os.mkdir(merged_letter_dir)
            merged_letter_path = f"C:/Users/russ1/Documents/Important Documents/Resume/Software Engineer/Resume w Cover Letter/{name_of_company}/Russell_Pacheco_resume_w_cover_letter.pdf"

            cover_letter = PdfFileReader(event.src_path)
            resume = f"C:/Users/russ1/Documents/Important Documents/Resume/Software Engineer/Russell_Pacheco_resume.pdf"

            output = PdfFileMerger()
            output.append(cover_letter)
            output.append(resume)

            print("Inserting merged Resume and PDF")
            with open(merged_letter_path, "wb") as output_stream:
                output.write(output_stream)
