# Счетчик вызовов
calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
        word = string
        result = (len(word), word.upper(), word.lower())
        count_calls()
        return result
def is_contains(string, list_to_search):
        string = string
        list_to_search = list_to_search
        count_calls()
        result = False
        for element in list_to_search:
            if  element.lower() == string.lower():
                result = True
                break
        return result
print(string_info('World'))
print(string_info('House'))
print(is_contains('Glass', ['glASS', 'wINe', 'WAter']))
print(is_contains('book', ['sheet', 'pade']))
print(calls)
