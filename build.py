top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()


index = open('content/index.html').read()
index = top + index + bottom
open('docs/index.html', 'w+').write(index)

contact = open('content/contact.html').read()
contact = top + contact + bottom
open('docs/contact.html', 'w+').write(contact)

education = open('content/education.html').read()
education = top + education + bottom
open('docs/education.html', 'w+').write(education)

experience = open('content/experience.html').read()
experience = top + experience + bottom
open('docs/experience.html', 'w+').write(experience)




