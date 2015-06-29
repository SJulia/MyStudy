import pickle

Telephones = []
Names = []
Phonebook = [Names, Telephones]
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
            new_data = data_from_file[0] + data[0], data_from_file[1] + data[1]
            pickle.dump(new_data, open(path_to_file, 'w'))
        else:
            pickle.dump(data, open(path_to_file, 'w'))
    except:
        print 'Can not write to file'


def add_note():
    name = raw_input('Write your name: ')
    telephone = raw_input('Write you phone: ')
    Names.append(name)
    Telephones.append(telephone)
    dump_to_file(book_file, Phonebook)

def search():
    d = read_from_file(book_file)
    Names = d[0]
    Telephones = d[1]
    searched = raw_input("What's your criteria for search?")
    flags = [False, False]
    for i in Names:
        if i == searched:
            print Telephones[Names.index(i)]
            break
    else:
        flags[0] = True
    for i in Telephones:
        if i == searched:
            print Names[Telephones.index(i)]
            break
    else:
        flags[1] = True
    if all(flags):
        print "Can not find this item!"


def menu():
    while True:
        print 'This is PhoneBook. Please input your choice?'
        print '1. Add note\n2. Search item\n3. Exit'
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
