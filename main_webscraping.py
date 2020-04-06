from bs4 import BeautifulSoup

#Create an example html to play with
#We type it as a list because it is too long to type it as one sentence.
#Afterwards we will combine all words in the list as one string
html = ['<html><heading> style="font-size:20px"><i>This is the title<br><br></i><heading',
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
print(soup.html.name)
print(soup.body.name)

#Text attribute will mush together all the text in all the children of the tag
print(soup.body.text)

#Contents is a list of the children of that tag
#Here, the html has only one child, the body has 4 children

print(soup.html.contents)
print(soup.body.contents)

#Parents and sibling reference helps to navigate the parse tree
print(soup.body.parent.name)
print(soup.b.nextSibling)
print(soup.b.previousSibling)

#FindAll, fire are methods to search the tree for specific tags or tages with certain attributes
bold - soup.findAll('b') #Finds all the tags which have the text in bold <b></b> and return a list
print(bold)
# stopped at 11:00