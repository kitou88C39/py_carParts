from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
print(soup)
print(soup.prettify())