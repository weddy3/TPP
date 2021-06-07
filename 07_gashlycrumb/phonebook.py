#!/usr/bin/env python3


from pprint import pprint as pp 


def main():

    my_phonebook = {}
    with open('phonebook.txt') as fh:
        for line in fh:
            my_phonebook.update({line.split(', ')[0]: line.split(', ')[1]})

    pp(my_phonebook)

            

if __name__ == '__main__':
    main()