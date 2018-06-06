import glob
import os
from jinja2 import Template
# import markdown

def create_files():
    all_html_files = glob.glob('content/*.md')
    template_html = open('templates/base.html').read()
    template = Template(template_html)
    for items in all_html_files:
            file_name = os.path.basename(items)
            name_only, extension = os.path.splitext(file_name)
            updated_content = open(items).read()
            page=template.render(
                content = updated_content,
                title = name_only
            )
            # name = items.replace('content', 'docs')
            open('docs/' + name_only + '.html', "w+").write(page)



if __name__ == '__main__':
  create_files()
