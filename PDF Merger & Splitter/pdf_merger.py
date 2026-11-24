from PyPDF2 import PdfMerger, PdfFileMerger

merger = PdfFileMerger()

#Input PDF Files Here                    #Input PDF Selected Pages
merger.append("PDF1_FILENAME.pdf", pages=(0,0))
merger.append("PDF2_FILENAME.pdf", pages=(0,0))
merger.append("PDF3_FILENAME.pdf", pages=(0,0))
merger.append("PDF4_FILENAME.pdf", pages=(0,0))

merger.write("MERGED_PDF_FILENAME.pdf")
merger.close()