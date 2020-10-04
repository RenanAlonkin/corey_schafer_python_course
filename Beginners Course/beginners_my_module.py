print('Importing beginner_my_module...')

test = 'Testing string'

def find_index(to_search, target):
    '''
    Find the index of a value in sequence
    '''

    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1