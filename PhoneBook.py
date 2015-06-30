import pickle
Data = {}
Phonebook = [Data]
book_file = 'D:\\book.pb'

def read_from_file(path_to_file):
    try:
        return pickle.load(open(path_to_file, 'r'))
    except:
        pass

def dump_to_file(path_to_file, data):
    try:
        data_from_file = read_from_file(path_to_file)
        print data_from_file
        if data_from_file:
            new_data = data_from_file[0].update(data[0])
            pickle.dump(new_data, open(path_to_file, 'w'))
        else:
            pickle.dump(data, open(path_to_file, 'w'))
    except:
        print 'Can not write to file'


def add_note():
    name = raw_input('Write your name: ')
    telephone = raw_input('Write you phone: ')
    Data[name] = telephone
    dump_to_file(book_file, Phonebook)

def search():
    d = read_from_file(book_file)
    data_dictionary = d[0]
    searched = raw_input("What's your criteria for search?")
    flags = [False, False]
    for i in data_dictionary.keys():
        if i == searched:
            print data_dictionary[i]
            break
    else:
        flags[0] = True
    #     unpack cortege and set the key and value
    for key, value in data_dictionary:
        if value == searched:
            print key
            break
    else:
        flags[1] = True
    if all(flags):
        print "Can not find this item!"


def menu():
    print 'This is PhoneBook. Please input your choice?'
    while True:
        print """
        1. Add note
        2. Search item
        3. Exit
        """
        choice = str(raw_input('Your choice: '))
        if choice == '1':
            add_note()
        elif choice == '2':
            search()
        elif choice == '3':
            exit()
        else:
            print 'Wrong choice try again'
            continue


menu()
