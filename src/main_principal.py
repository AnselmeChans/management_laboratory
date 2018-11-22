# -*- coding: utf-8 -*

################################
# Programme Python3
# Auteur : Hans CERIL
# Date creation : 17/11/2018
################################
import pygraphviz as pgv


from laboratoire import *

if __name__ == "__main__" :

    lab1 = Lab()

    ans = True
    while ans :
        lab1.affiche_menu()
        print("\n")
        ans = input("What would you like to do? ")

        if ans == "1" :
            lab1.record_entry()
        elif ans == "2" :
            name = input("Give the name of the person who leave : ")
            lab1.record_leave(name)
        elif ans == "3" :
            name = input("Give the name of the person who want to change the office : ")
            new_office = input("Give the new_office : ")
            lab1.correct_office(name, new_office)
        elif ans == "4" :
            name = input("which person do you want to change the name ? ")
            new_name = input("which name do you want to give ? ")
            lab1.correct_name(name, new_name)
        elif ans == "5" :
            name = input(" Give the name ? ")
            lab1.is_member_lab(name)
        elif ans == "6" :
            name = input(" Give the name ? ")
            lab1.which_is_office(name)
        elif ans == "7" :
            lab1.listing_occuped_office()
        elif ans == "8" :
            lab1.save_from_file("input.txt")
        elif ans == "9" :
            lab1.quit()
