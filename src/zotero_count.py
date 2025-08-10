from bs4 import BeautifulSoup

path = "/Users/ula/code/PhD/actionability_addendum/src/actionability_export.html"

with open(path, encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

count = len(soup.find_all("h1", string="Paper Summary"))
print(f"{count} documents were merged.")