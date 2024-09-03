call = 0


def count_call():
    global call
    call += 1


def string_info(str_=''):
    count_call()
    tuple_ = (len(str_), str_.upper(), str_.lower())
    # print(tuple_)
    return tuple_


def is_contains(str_='', list_=['', '']):
    count_call()
    bool_ = False
    for i in range(len(list_)):
        list_[i] = list_[i].lower()
        str_ = str_.lower()
        # print(list_[i], str_)
        if list_[i] == str_:
            bool_ = True
            break
    return bool_


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(call)
