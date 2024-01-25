from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
print(soup)
print(soup.prettify())

print(soup.html.head.title)
print(soup.title)