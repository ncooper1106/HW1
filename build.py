
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
  'filename': ' content/experience.html',
  'title': 'experience',
  },
]
  
def main():
  #read in the entire template
  template = open('templates/base.html').read() 
  
  #for loop to create pages
  for items in pages:
    content = open(pages['filename'].read()
    finished_content = template.replace('{{content}}'), content)
    page_name = str('docs/' + page['title'] + '.html')
    open(page_name, 'w+').write(finished_content)
 
  #create the index HTML page
  #index_content = open('content/index.html').read()
  #finished_index_page = template.replace('{{content}}', index_content)
  #open('docs/index.html', 'w+').write(finished_index_page)

  #create the contact HTML page
  #contact_content = open('content/contact.html').read()
  #finished_contact_page = template.replace('{{content}}', contact_content)
  #open('docs/contact.html', 'w+').write(finished_contact_page)

  #create the education HTML page
  #education_content = open('content/education.html').read()
  #finished_education_page = template.replace('{{content}}', education_content)
  #open('docs/education.html', 'w+').write(finished_education_page)

  #create the experience HTML page
  #experience_content = open('content/experience.html').read()
  #finished_experience_page = template.replace('{{content}}', experience_content)  
  #open('docs/experience.html', 'w+').write(finished_experience_page)  
  
if __name__ == '__main__':
  main()




