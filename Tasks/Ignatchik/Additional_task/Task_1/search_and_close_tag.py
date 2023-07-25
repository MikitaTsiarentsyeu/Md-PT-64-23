import re

with open("input.html", 'r', encoding='utf-8') as file:
    list_html = file.readlines()

flag = True
html_line = ""
list_of_all_tags = []
pattern = '<(\S*?)[^>]*>.*?|<.*?/>'

with open("input.html", "r") as input_file:
    for line in input_file:
        html_line += line
    
all_tags = re.finditer(pattern, html_line)

try:
    while flag:
        item = next(all_tags)
        list_of_all_tags.append(item.group())
except StopIteration:
    flag = False

single_HTML_tags = ('!DOCTYPE', 'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr')

def remove_text(l):
    c_tags = []
    for tag in l:
        new_tag = tag.split(" ")
        if len(new_tag) > 1:
            c_tags.append(f"{new_tag[0]}>")
        else:
            c_tags.append(new_tag[0])
    return c_tags

def remove_single_tags(l1, l2):
    res = []
    for i in l1:
        count = 0
        for j in l2:
            if j not in i:
                count += 1
        if count == len(single_HTML_tags):
            res.append(i)
    return res

def remove_closed_tags(l):
    result = []
    for i in l:
        if '/' in i:
            continue
        else:
            result.append(i)
    return result

def looking_for_an_open_tag(l1,l2):
    for i in l1:
        n1 = l2.count(i)
        n2 = l2.count(i[0]+'/'+i[1:])
        if n1 != n2:
            return  i

new_list_html = []
def close_html(l):
    new_list_html = l[:] + ['</html>']
    return new_list_html

def close_head(l):
    for i in l:
        if 'body' in i:
            ind1 = l.index(i)
            new_list_html = l[:ind1] + ["</head>\n"] + l[ind1:]
            break
    return new_list_html

def close_body(l):
    new_list_html = l[:-1] + ["</body>\n"] + l[-1:]
    return new_list_html

def close_div(l):
    list_div = []
    open_tag = []
    tag_before_which_you_need_to_close_the_tag = []
    for index, k  in enumerate(l):
        if 'div' in k:
            ind3 = k.index('<')
            srez1 = k[:ind3]
            num1 = len(srez1)
            list_div.append([k, index, num1])
    for i in list_div:
        if len(open_tag) == 0:
            open_tag.append(i)
        else:
            if '/div' in i[0]:
                for j in reversed(range(0, len(open_tag))):
                    if open_tag[j][-1] == i[-1]:
                        del open_tag[j]
                        break
            else:
                open_tag.append(i)
    if list_div[-1] == open_tag[-1]:
        for bd in l:
            if '/body' in bd:
                ind1 = l.index(bd)
                new_list_html = l[:ind1] + ["    </div>\n"] + l[ind1:]
                break
    else:
        for i in list_div:
            if '/div' not in i[0] and i[-1] == open_tag[0][-1]  and i != open_tag[0] and i[1] > open_tag[0][1]:
                i.append(1)
                tag_before_which_you_need_to_close_the_tag = i
                break
            elif '/div' in i[0] and i[-1] == open_tag[0][-1] -4:
                i.append(2)
                tag_before_which_you_need_to_close_the_tag = i
                break
        index = tag_before_which_you_need_to_close_the_tag[1]
        if tag_before_which_you_need_to_close_the_tag[-1] == 1:
            tab = tag_before_which_you_need_to_close_the_tag[2]
            new_list_html = l[:index] + [' '*tab + '</div>\n'] + l[index:]
        else:
            tab = tag_before_which_you_need_to_close_the_tag[2]+4
            new_list_html = l[:index] + [' '*tab + '</div>\n'] + l[index:]
    return new_list_html

def close_other_tags(l, tag):
    for i in l:
        if tag in i and i[-2] != '>':
            res = (i[:-1]+'</'+tag[1:]+i[-1])
            ind = l.index(i)
            l[ind] = res
            break
    return l

if __name__ == "__main__":
    clean_tags = remove_text(list_of_all_tags)
    tags_1 =remove_single_tags(clean_tags, single_HTML_tags)
    set_tags = set(tags_1)
    tags_2 = remove_closed_tags(set_tags)
    open_tag = looking_for_an_open_tag(tags_2,tags_1)
    if open_tag == '<html>':
        result = close_html(list_html)
    elif open_tag == '<head>':
        result = close_head(list_html)
    elif open_tag == '<body>':
        result = close_body(list_html)
    elif open_tag == '<div>':
        result = close_div(list_html)
    else:
        result = close_other_tags(list_html, open_tag)

    with open('output.html', 'w', encoding='utf-8') as file:
        for i in result:
            file.write(i)


