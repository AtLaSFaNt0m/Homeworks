from pandas.io.formats.format import return_docstring

calls = 0




def count_calls():
    global calls
    calls+=1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, teext_to_speech):
    count_calls()
    string = string.lower()
    teext_to_speech = [item.lower() for item in teext_to_speech]
    return string in teext_to_speech




print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))
print(string_info('Capybara'))

print(calls)