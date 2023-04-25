import pypdfium2 as pdfium


def pdf2html(pdf_path: str, debug: bool = False):
    output = ""

    all_pages = pdfium.PdfDocument(pdf_path)

    for page in all_pages:
        textpage = page.get_textpage()
        text = textpage.get_text_range().strip()

        output += text + "\n\n"

        if debug:
            print(text)

    return output


if __name__ == "__main__":
    file_path = "data/test.pdf"

    print(pdf2html(file_path))
