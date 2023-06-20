from bs4 import BeautifulSoup

html_line = ""

with open("input.html", "r", encoding="utf-8") as input_file:
    for line in input_file:
        html_line += line

soup = BeautifulSoup(html_line, features="html.parser")

new_line = soup.prettify()

with open("output.html", "w", encoding="utf-8") as output_file:
    output_file.write(new_line)