
# -*- coding: utf-8 -*

################################
# Programme Python3
# Auteur : Hans CERIL
# Date creation : 17/11/2018
################################

class Person :
    """ Personal caracteristics of an emplyer """

    def __init__(self, name, office, numberPhone, status, arrivalDate, departureDate) :
        self.__name = name
        self.__office = office
        self.__numberPhone = numberPhone
        self.__status = status
        self.__arrivalDate = arrivalDate
        self.__departureDate = departureDate

    #---------------- Guetters ---------------------------
    @property
    def name (self) :
        return self.__name

    @property
    def office(self) :
        return self.__office

    @property
    def numberPhone (self) :
        return self.__numberPhone

    @property
    def status (self) :
        return self.__status

    @property
    def arrivalDate (self) :
        return self.__arrivalDate

    @property
    def departureDate (self) :
        return self.__departureDate

    #------------------------- Setters --------------------------
    @name.setter
    def name(self, name) :
        """
        Function that allow to correct the name of the person
        (in case of a bad spelling, etc.)

        :params :name:str new_name:str
        :returns None
        """
        self.__name = name

    @office.setter
    def office(self, office) :
        """
        Fonction that allows to change the office occupied by a person

        :params :name;str, new_office:str
        :returns None
        """
        self.__office = office
