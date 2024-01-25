from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
print(soup)
print(soup.prettify())

print(soup.html.head.title)
print(soup.title)

print(soup.find_all("a"))

for tag_a in soup.find_all("a"):
    print(tag_a, end="¥n¥n")

or tag_a in soup.find_all("a"):
    print(tag_a.string)
    print(tag_a["href"], end="¥n¥n")