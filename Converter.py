import re

# 1. read file
with open('input.txt', 'r', encoding='utf-8') as inputt:
    content = inputt.read() # Прочитали весь текст в переменную content

# 2. dictionary
words_in_file = content.split() 

dictionary = {
    "html5": "<!DOCTYPE html>",
    "main[": "<html>",
    "head[": "<head>",
    "title[": "<title>",
    "]title": "</title>",
    "]head": "</head>",
    "body[": "<body>",
    "]body": "</body>",
    "]main": "</html>"
}


# 3. find words
pattern = r'"([^"]*)"|\S+'
items = re.findall(pattern, content)

new_content = []

# 4. findall
for quoted, word in re.findall(r'"([^"]*)"|(\S+)', content):
    if quoted:
        # remove ""
        new_content.append(quoted)
    elif word in dictionary:
        # check dictionary
        new_content.append(dictionary[word])

# 5. write results in index.html
with open('main/index.html', 'w', encoding='utf-8') as outputt:
    outputt.write("\n".join(new_content))