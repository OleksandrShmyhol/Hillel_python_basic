def popular_words(text, words):
    list_text = text.lower().split(' ')
    result = {}
    for el in words:
        if el in list_text:
            result.update({el: list_text.count(el)})
        else:
            result.update({el: 0})
    return result


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}
print('OK')
