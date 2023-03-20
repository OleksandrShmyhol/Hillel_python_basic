import codecs


def delete_html_tags(html_file, result_file='cleanedd.txt'):
    html = codecs.open(html_file, 'r', 'utf-8').read()
    result_file = open(result_file, 'w')
    while '<' in html and '>' in html:
        html = html.replace(str(html[html.index('<'):html.index('>') + 1]), '')
    result_file.write(html)
    result_file.close()


delete_html_tags('draft.html')

