import pdfkit
from jinja2 import Environment, FileSystemLoader
import os
from pathlib import Path

context = {"title": "New title"}

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
template_loader = FileSystemLoader('./')
template_env = Environment(loader=template_loader)
html_template = 'tender_create.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

print(output_text)
