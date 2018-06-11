import glob
import os
from jinja2 import Template
import markdown


md = markdown.Markdown(extensions = ["markdown.extensions.meta"])

def create_files():
    #creates a varaible with a list of filenames in the content folder
    all_html_files = glob.glob('content/*.md')

    #creates a variable containing the text of the base template
    template_html = open('templates/base.html').read()

    #uses the Template function to recognize the template syntax
    template = Template(template_html)

    #goes through each page and
    for items in all_html_files:
        file_name = os.path.basename(items)
        name_only, extension = os.path.splitext(file_name)
        updated_content = open(items).read()
        html = md.convert(updated_content)
        title = str(md.Meta["title"][0])
        path = 'docs/' + name_only + '.html'
        pages=template.render(
            content = html,
            title = title,            
        )
        open(path, "w+").write(pages)





if __name__ == '__main__':
  create_files()
