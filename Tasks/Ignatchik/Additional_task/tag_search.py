with open('tag_search.html', 'r', encoding='utf-8') as file:
    list_html = file.readlines()

# single_HTML_tags = ['<!DOCTYPE html>', '<area>', '<base>', '<br>', '<col>', '<embed>', '<hr>', '<img>',
#                     '<input>', '<keygen>', '<link>', '<meta>', '<param>', '<source>', '<track>', '<wbr>']

new_list_html = []

for i in list_html:
    if '<body>' in i: # or '<head>' in i or '<html>' in i
        new_list_html.append(i)
    elif '<div>' in i:
        new_list_html.append([i])
    elif '</div>' in i:
        new_list_html[-1].append(i)
    else:
        new_list_html[-1].append(i)

for j in new_list_html:
    for k in j:
        if '<div>' in k:
            if j[-1] == '    </div>':
                j[-1] = '    </div>\n'
            elif j[-1] != '    </div>\n':
                j.append('    </div>\n')
        if '<p>' in k:
            if k[-5:-1] != '</p>':
                ind = j.index(k)
                j[ind] = k[:-1]+'</p>'+k[-1]

if new_list_html[-1] != '</body>':
    new_list_html.append('</body>')

with open('output.html', 'w', encoding='utf-8') as file:
    for i in new_list_html:
        for j in i:
            file.write(j)