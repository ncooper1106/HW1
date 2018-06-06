pages = [
  {
    'filename': 'content/index.html',
    'title': 'index',
  },
  {
    'filename': 'content/contact.html',
    'title': 'contact',
  },
  {
    'filename': 'content/education.html',
    'title': 'education',
  },
  {
    'filename': 'content/experience.html',
    'title': 'experience',
  },
]
  
  
def generate():
  #read in the base template
  template = open('templates/base.html').read()
  
  
  for items in pages:
    #print(items['filename'])
    #print(items['title'])
    content = open(items['filename']).read()
    title = items['title']
    
    #replace the placeholder tags with real infomation
    finished_content = template.replace('{{ content }}', content).replace('{{ title }}', title)  
    
    #create new path names for html pages
    page_name = str('docs/' + items['title'] + '.html')
    
    #write the new pages
    open(page_name, 'w+').write(finished_content)
    
   
if __name__ == '__main__':
  generate()




