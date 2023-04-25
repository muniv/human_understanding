from core.xlsx2html_core import xlsx2html, get_sheetnames_xlsx, xlsx2body


def excel2html(excel_path: str, debug: bool = False):
    output = ""

    for sheet_name in get_sheetnames_xlsx(excel_path):
        output += sheet_name + "\n"
        output += xlsx2body(file_path, sheet=sheet_name).replace("&nbsp;", "") + "\n\n"

    if debug:
        print(output)
    return output


if __name__ == "__main__":
    file_path = "data/test.xlsx"

    print(excel2html(file_path))
