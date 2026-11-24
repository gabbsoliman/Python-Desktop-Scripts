from PyPDF2 import PdfFileReader, PdfFileWriter

PDF1_FILENAME = list(range(0,7))
PDF2_FILENAME = [4, 7]
PDF3_FILENAME = [8, 9]

with open("PDF_FILENAME.pdf", "wb") as f:
    reader = PdfFileReader(f)

    pdf1writer = PdfFileWriter()
    pdf2writer = PdfFileWriter()
    pdf3writer = PdfFileWriter()

    for page in range(len(reader.pages)):
        if page in pdf1writer:
            pdf1writer.addPage(reader.getPage(page))
        elif page in pdf2writer:
            pdf2writer.addPage(reader.getPage(page))
        else:
            pdf3writer.addPage(reader.getPage(page))

    with open("PDF1_FILENAME.pdf", "wb") as f2:
        pdf1writer.write(f2)
    with open("PDF2_FILENAME", "wb") as f2:
        pdf2writer.write(f2)
    with open("PDF3_FILENAME.pdf", "wb") as f2:
        pdf3writer.write(f2)