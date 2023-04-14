import base64

import mammoth

def convert_image(image):
    with image.open() as image_bytes:
        encoded_src = base64.b64encode(image_bytes.read()).decode("ascii")

    return {
        "src": "data:{0};base64,{1}".format(image.content_type, encoded_src)
    }

def docx2html(input_file_path: str, output_file_path: str=None):
    with open(input_file_path, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file, convert_image=mammoth.images.img_element(convert_image))
        html = result.value # The generated HTML
        messages = result.messages # Any messages, such as warnings during conversion
    if output_file_path:
        writer = open(output_file_path, 'w')
        writer.write(html.replace("<p>","").replace("</p>"," "))
        writer.close()
    return html
