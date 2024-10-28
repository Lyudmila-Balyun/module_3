def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if len(i) <= len(root_word):
            if i.lower() in root_word.lower():
                same_words.append(i)
        else:
            if root_word.lower() in i.lower():
                same_words.append(i)
    return same_words


result1 = single_root_words('пноэ', 'Диспноэ', 'ТАХИПНОЭ', 'Апноэ', 'Одышка')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
