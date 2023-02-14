from pypdf import PdfWriter
import os

# pdfpages = PdfReader("questionbank.pdf")
merger = PdfWriter()
for pdf in ["question.pdf", "questionbank.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
