import re
# Пока только закрывает <p>. Направление выбрано правельно?
with open('tag_search.html', 'r', encoding='utf-8') as file:
    list_html = file.readlines()

flag = True
html_line = ""
list_of_all_tags = []
pattern = '<(\S*?)[^>]*>.*?|<.*?/>'

with open("tag_search.html", "r") as input_file:
    for line in input_file:
        html_line += line

all_tags = re.finditer(pattern, html_line)

try:
    while flag:
        item = next(all_tags)
        list_of_all_tags.append(item.group())
except StopIteration:
    flag = False

set_tag = set(list_of_all_tags)

new_list_html = []
for i in set_tag :
    if '/' in i:
        continue
    else:
        n1 = list_of_all_tags.count(i)
        n2 = list_of_all_tags.count(i[0]+'/'+i[1:])
        if n1 != n2:
            for j in list_html:
                if i in j and j[-2] != '>':
                    new_list_html.append(j[:-1]+'<'+'/'+i[1:]+j[-1])
                else:
                    new_list_html.append(j)

with open('output.html', 'w', encoding='utf-8') as file:
    for i in new_list_html:
        file.write(i)



