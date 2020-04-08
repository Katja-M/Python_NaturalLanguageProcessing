from bs4 import BeautifulSoup

#Create an example html to play with
#We type it as a list because it is too long to type it as one sentence.
#Afterwards we will combine all words in the list as one string
html = ['<html><heading> style="font-size:20px"><i>This is the title<br><br></i></heading>',
    '<body><b>This is the body</b><p id= "para1">This is paral<a href="wwww.google.com">Google</a></p>',
    '<p id="para2">This is para 2</p></body></html>']
#More about the join method https://www.programiz.com/python-programming/methods/string/join
html = ''.join(html)
#Instantiate a soup object.
#This automatically identifies a structure in the html and creates a parse three. 
#You can navigate the structure/tree in the soup and extract pieces that you are interested in
soup = BeautifulSoup(html)

#The following functions allows you to print the HTML in a readable and formatted manner
#That means you can see the structure of the parse tree visually
print(soup.prettify())
#You should see that 
# at the top of the hierarchy in the parse tree is the <html></html> tag
#Then comes the <body></body> tag
#Within the body, the heading and paragraphs are 'siblings'.
#The body is the parent of these tags and the html tag is the parent of the body
#Each tag has attributes - name, contents ( a list), text, parent and siblings

#Name attribute is just the name of the tag
print('Tag name of html: ' + soup.html.name)
print('Tag name of body: ' + soup.body.name)

#Text attribute will mush together all the text in all the children of the tag
print(soup.body.text)

#Contents is a list of the children of that tag
#Here, the html has only one child, the body has 4 children
print(soup.html.contents)
print(soup.body.contents)

#Parents and sibling reference helps to navigate the parse tree
print("Body's parent name: " + soup.body.parent.name)
print("Body's next sibling: " + str(soup.b.nextSibling))
print("Paragraph's previous sibling: " + str(soup.p.previousSibling))

#FindAll, fire are methods to search the tree for specific tags or tages with certain attributes
bold = soup.findAll('b') #Finds all the tags which have the text in bold <b></b> and return a list
print(bold[0].text)

#Getting all the text that is in the paragraphs (enclose in <p></p> tags) as a single string
paras = ' '.join([p.text for p in soup.findAll('p')])
print(paras)

#The findAll-method cannot only be used to find specific tags, but also specific attributes
#The following code lines will find the paragraph with id 'para2'
print('Looking for paragraph with id "para2" '+ soup.findAll(id = 'para2')[0].text)
#Find any text with font size 20
font20 = ' '.join([p.text for p in soup.findAll(style = "font-size:20px")])
print('Print everything with font size 20: ')
print(font20)
#The method findAll also takes in list or dictionaries of tag names to search for
print('List as input: ')
print(soup.findAll(['b','p']))
print('Dictionary as input: ')
print(soup.findAll({'b': True, 'p': True}))

#Finding links in the HTML
#a tags generally refer to links. Links are generally of the form <a href = 'link'>'link-text'</a>
links = soup.find('a')
print('The first link found in the HTML: ')
print(links)
#We used find instead of findAll - this will just give us the first tag that matches the search,
#in this case we have only 1 link on our page. soup.findAll will return a list of links and you can limit
#the number of results suing the limit keyword soup.findAll('a', limit = 9)

#Extracting the url and the text separately
#Accessing the url by creating href as a key
print(links['href'] +" is the url and " + links.text + " is the text.")

#find can navigate the parse tree as well. findParents, findNextSiblings, findPreviousSiblings all work
#similar to findAll, but will search only within those branches of the tree
#findNext, findPrevious and findAllNext and findAllPrevious can be used to find matches starting from a specified point

#Let's say you want the text of the first paragraph after the first occurence of the text 'Google'
print('Text after the word Google in the first paragraph: ' + soup.find(text = 'Google').findNext('p').text)

# a little shortcut to using findAll: Call the tag itself and it can be used in place of findAll with the same arguments
soup.body('p')
soup.findAll('p')

#Takeaway: BeautifulSoup makes parsing html or xml very intuitive and elegant.