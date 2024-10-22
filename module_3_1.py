calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info (string):
    count_calls()
    a = (len(string), string.upper(), string.lower())
    return a

def is_contains (string, list_to_search):
    count_calls()
    list_to_search_lower = []
    for i in list_to_search:
        list_to_search_lower.append(i.lower())

    return string.lower() in list_to_search_lower


print(string_info('Курятина'))
print(string_info('Экстрамедуллярный гемопоэз'))
print(is_contains('ПрЕвЕдД1!', ['Привет', 'Превед', 'преведд1!']))
print(is_contains('Новичок', ['дЖОН нОЛАН', 'The Rookie']))
print(calls)
