import pypdfium2 as pdfium

all_pages = pdfium.PdfDocument("data/test.pdf")

for page in all_pages:
    textpage = page.get_textpage()
    text = textpage.get_text_range()

    print(text)