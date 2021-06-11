with open("src.txt") as f:
    lines = f.read().split("\n")

import os.path
root = "books/cuentas_y_leyendas"
assert os.path.exists(root)

def is_html(line):
    import re
    return re.match('^<.*>.*</.*>$', line.strip())

assert is_html(' <div class="center"> **** </div>')
assert not is_html("> blah blah blah")

def case(line):
    ln = line.split()
    txt = ""
    for i in range(len(ln)):
        a = ln[i]
        a = a.lower()
        if not a:
            continue
        if a[0] == '"':
            a = a[1:]
            txt += '"'
        if not a:
            continue
        if a not in ("de","a","y","o") or i == 0:
            a = a[0].upper() + a[1:]
        txt += a + " "
    return txt.strip()

lns = {}
names = {}
image = {}

for line in lines:
    if not line:
        continue
    if line[0] != "\t":
        a = line.split("=")
        tag = a[0].strip()
        names[tag] = a[1].strip()
        lns[tag] = []
        img = root + "/" + tag + ".png"
        if os.path.exists(img):
            image[tag] = tag + ".png"
        else:
            image[tag] = "DELETEME"

    else:
        line = line.strip() #remove tab
        if is_html(line):
            lns[tag].append(line)
        else:
            lns[tag].append("<p>{}</p>".format(line))

with open("template.html") as f:
    temp = f.read()

for tag in names:
    txt = temp.format(title=names[tag], case = case(names[tag]), img=image[tag], body = "\n    ".join(lns[tag]))
    with open("build/test" + "/" + tag + ".html", 'w') as f:
        f.write(txt)
