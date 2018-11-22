# -*- coding: utf-8 -*

################################
# Programme Python3
# Auteur : Hans CERIL
# Date creation : 17/11/2018
################################

#-------- Import packages --------
from personne import *
import sys
import os
import collections
from ihm import *
import json
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout





class Lab :
    """ Lab class who manage personal employers into the lab """

    def __init__(self) :
        self.__laboratory = {}
        self.rootDir = {}

        self.__dict_acess = {
            1: self.record_entry,
            2: self.record_leave,
            3: self.correct_office,
            4: self.correct_name,
            5: self.is_member_lab,
            6: self.which_is_office,
            7: self.listing_occuped_office,
            8: self.quit
        }

        self.menu = (
            [
                (1, "1- Register the arrival of a new person", "record_entry(name: str, office:int)"),
                (2, "2- Record the departure of a person", "record_leave(name: str)"),
                (3, "3- Change the office occupied by a person", "office_modification(name: str, new_office:int)"),
                (4, "4- Correct the name of the person", "correct_name(name: str, new_name: str)"),
                (5, "5- Knowing if a person is a member of the lab", "is_member_lab(name: str)"),
                (6, "6- Knowing the office's person", "which_is_office(name: str)"),
                (7, "7- Listing of all staff with busy office", "listing_occuped_office()"),
                (8, "8- Saving the lab's information into file.txt", "save_info_file()"),
                (9, "9- Quit", "quit()")

            ], self.__dict_acess)

    def affiche_menu(self):
        for menu in self.menu[0] :
            print(menu[1], " ===> ", menu[2])


    def record_entry(self) :
        """
        Fonction that allow to register the arrival of a new person.
        The name of the person and the office they occupy are specified.

        :params :name:str  :office:str
        :returns None
        """
        name_p = input(" Give the name of the person : ")
        office_p = input(" Give the office of the person : ")
        numberPhone_p = input(" Give the number phone of the person : ")
        status_p = input(" Give the status of the person : ")
        arrivalDate_p = input(" What is the arrival date : ")
        departureDate_p = input(" What is the departure date : ")

        pers = Person(name_p, office_p, numberPhone_p, status_p,
                        arrivalDate_p, departureDate_p)

        self.__laboratory[pers.name] = {
                                    "bureau" : pers.office,
                                    "tel_number" : pers.numberPhone,
                                    "status" : pers.status,
                                    "arrival_date" : pers.arrivalDate,
                                    "departure_date" : pers.departureDate
                                    }

    def record_leave(self, name) :
        """
        Fonction that allow to record the departure of a person.

        :params :name:str
        :returns None
        """
        if name in self.__laboratory.keys() :
            del self.__laboratory[name]
        else :
            print("This person is not working into this lab")

    def is_member_lab(self, name) :
        """
        Function that allows to know if a person is a member of the laboratory

        :params :name:str
        :returns None
        """
        if name in self.__laboratory.keys() :
            print(" Yes !!! This person is working in this lab ")
        else :
            print(" No !!! This person is not working in this lab")

    def affichage(self) :
        for key, value in self.__laboratory.items() :
            print("---------",key, "------------")
            if isinstance(value,dict):
                for key_i, value_i in value.items() :
                    print(key_i, " : ", value_i)

    def which_is_office(self, name) :
        """
        Function that allow to know the office's person

        :params :name:str
        :returns None
        """
        if name in self.__laboratory.keys() :
            print(self.__laboratory[name]["bureau"])
        else :
            raise InconnuException(LaboException)


    def listing_occuped_office(self) :
        """
        Function that allows to produce listing of all staff with busy office

        :params None
        :returns None
        """
        rep = input (" Display office occupancy in a lexicographic order of offices Y/N ? ")

        office_listing = {}
        for person, info in self.__laboratory.items() :
            if isinstance(info, dict) :
                bureau = info["bureau"]
                if bureau not in office_listing.keys() :
                    office_listing[bureau] = []
                    if person not in office_listing[bureau]:
                        office_listing[bureau].append(person)
                    else :
                        pass
                else :
                    pass

        if rep == "y" :
            od = collections.OrderedDict(sorted(office_listing.items()))

            for key, value in office_listing.items() :
                print(key, value)

        elif rep == "n" :
            for key, value in office_listing.items()  :
                print(key, value)

    def correct_name (self, name, new_name) : #pas bon a modifier
        if name in self.__laboratory.keys() :
            self.__laboratory[new_name] = self.__laboratory.pop(name)
        else :
            print("this person is not working on the lab")

    def correct_office(self, name, new_office) :
        if name in self.__laboratory.keys() :
            for value in self.__laboratory.values() :
                value["bureau"] = new_office
        else :
            print("this office do not exist")

    def save_from_file (self, file) :
        """
        Take information from file

        :params None
        : return None
        """

        def read(file) :
            with open("input.txt", "r", encoding="utf-8") as f :
                return [line.strip() for line in f.readlines()]

        list_file = read(file)
        key_elt = list_file[0].split("|")
        value_elt = [value.split("|") for value in list_file[1:]]

        dict_lab = dict()
        for element in value_elt :
            dict_lab[element[0]] = dict(zip(key_elt[1:], element[1:]))

        with open("./json_format/input.json", "w") as js:
            json.dump(dict_lab, js)


    def plotting_data(self, json_file) :
        with open(json_file, "r") as js:
            data = json.loads(js.read())

        list_name = [n for n in data.keys()]
        info_val = [i.values() for i in data.values()]
        list_information = [list(i) for i in info_val]

        i=0
        for i in range (len(list_name)) :
            df = pd.DataFrame({ 'from': list_name[i], 'to': list_information[i]})
            G=nx.from_pandas_edgelist(df, 'from', 'to')
            plt.figure(figsize=(4,3))
        # Plot it
            nx.draw(G,
                    node_size=15,
                    with_labels=True)
            i+=1

        plt.savefig("./images/json_picture" + "_" + i + "-%s.pdf" %i, format="pdf",
            transparent=True)

    def quit(self) :
        """
        Function that allow to Quit our program.

        :params None
        :returns None
        """
        print("================== EXIT ======================= ")
        sys.exit(0)
