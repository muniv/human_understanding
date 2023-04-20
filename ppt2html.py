import pptx
from bs4 import BeautifulSoup


def ppt2html(ppt_path: str):
    prs = pptx.Presentation(ppt_path)

    output = ""
    for _, slide in enumerate(prs.slides):
        if slide.shapes.title:
            output += slide.shapes.title.text.strip()

        for shape in slide.shapes:
            if shape.has_table:
                soup = BeautifulSoup()
                html_table = soup.new_tag('table')
                for row in shape.table.rows:
                    html_row = soup.new_tag("tr")
                    for cell in row.cells:
                        html_cell = soup.new_tag("td")
                        html_cell.string = cell.text
                        html_row.append(html_cell)
                    html_table.append(html_row)
                output += str(html_table).strip() + "\n"

            if shape.has_text_frame:
                output += shape.text_frame.text.strip() + "\n"

        output += "\n"

    return output

print(ppt2html('data/test.pptx'))