def main():
  #load header and footer of website
  top = open('templates/top.html').read()
  bottom = open('templates/bottom.html').read()
  
  #creates the index page
  index = open('content/index.html').read()
  index = top + index + bottom
  open('docs/index.html', 'w+').write(index)

  #creates the contact page
  contact = open('content/contact.html').read()
  contact = top + contact + bottom
  open('docs/contact.html', 'w+').write(contact)

  #creates the education page
  education = open('content/education.html').read()
  education = top + education + bottom
  open('docs/education.html', 'w+').write(education)

  #creates the experience page
  experience = open('content/experience.html').read()
  experience = top + experience + bottom
  open('docs/experience.html', 'w+').write(experience)
  
if __name__ == '__main__':
  main()




