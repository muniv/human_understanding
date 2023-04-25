from core.xlsx2html_core import xlsx2html,get_sheetnames_xlsx


file_path = "[DRM해제]위플젝 메뉴얼_텍스트_v 0.02_20230327.xlsx"

for sheet_name in get_sheetnames_xlsx(file_path):
    xlsx2html(file_path, f'output_sheet({sheet_name}).html', sheet=sheet_name)
