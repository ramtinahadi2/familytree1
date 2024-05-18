from tkinter import *
import time


class family:

    def _init_(self,name,gender):# Entering information for instance variables. Questions depends on gender.
        self.name=input(f"Enter the {name}s name:")
        self.surname=input(f"Enter the {name}s surname:")
        self.age=int(input(f"Enter the {name}s age:"))
        if gender=="M" or gender=="m":
            y=input("Does he have wife? (Y/N)")
            if y=="Y" or y=="y":
                self.partner=input(f"Enter the {name}s wifes name:")
                z=input("Does he have any child? (Y/N)")
                if z=="Y" or z=="y":
                    self.kid=True
                elif z=="N" or z=="n":
                    self.kid=None
            elif y=="N" or y=="n":
                self.partner=None
                self.kid=None

        if gender == "F" or gender == "f":
            y = input("Does she have husband? (Y/N)")
            if y == "Y" or y == "y":
                self.partner = input(f"Enter the {name}s husbands name:")
                z = input("Does she have any child? (Y/N)")
                if z == "Y" or z == "y":
                    self.kid = True
                elif z == "N" or z == "n":
                    self.kid = None
            elif y == "N" or y == "n":
                self.partner = None
                self.kid = None


def gender_variable_former():
    gender=input("Enter the formers gender:(M/F)")
    return gender
                                                    #Creating two gender functions. Former one is created for formers
def gender_variable():
    gender=input("Enter his/her kids gender:(M/F)")
    return gender


class grandmother(family):
    pass

class grandfather(family):
    pass

class mother(family):
    pass

class father(family):
    pass

class kid(family):
    pass

members=[] # An empty list named members is created to store persons.


while True: #When a person has no wife-husband or kid, The other persons code won't be executed in block of while
            #Each persons code depends on their genders
    i=gender_variable_former()

    if i=="M" or i=="m":
        grand_father=grandfather("grandfather",i)
        members.append(grand_father)

        if grand_father.partner == None or grand_father.kid == None:
            break

        elif grand_father.partner != None and grand_father.kid == True:
            i = gender_variable()

            if i == "M" or i == "m":
                father_ = father("father",i)
                members.append(father_)

                if father_.partner == None or father_.kid == None:
                    break

                elif father_.partner != None and father_.kid == True:
                    i = gender_variable()
                    kid_=kid("kid",i)
                    members.append(kid_)
                    break

            if i == "F" or i == "f":
                mother_ = mother("mother", i)
                members.append(mother_)

                if mother_.partner == None or mother_.kid == None:
                    break

                elif mother_.partner != None and mother_.kid == True:
                    i = gender_variable()
                    kid_ = kid("kid", i)
                    members.append(kid_)
                    break

    if i == "F" or i == "f":
        grand_mother = grandmother("grandmother", i)
        members.append(grand_mother)

        if grand_mother.partner == None or grand_mother.kid == None:
            break

        elif grand_mother.partner != None and grand_mother.kid == True:
            i = gender_variable()

            if i == "M" or i == "m":
                father_ = father("father", i)
                members.append(father_)

                if father_.partner == None or father_.kid == None:
                    break

                elif father_.partner != None and father_.kid == True:
                    i = gender_variable()
                    kid_ = kid("kid", i)
                    members.append(kid_)
                    break

            if i == "F" or i == "f":
                mother_ = mother("mother", i)
                members.append(mother_)

                if mother_.partner == None or mother_.kid == None:
                    break

                elif mother_.partner != None and mother_.kid == True:
                    i = gender_variable()
                    kid_ = kid("kid", i)
                    members.append(kid_)
                    break

# members list is completed.

window = Tk() #Creating a widget for output

window.title("Family Tree")

lst_tree = Listbox(window, width=70, height=10)

lst_tree.grid(padx=100, pady=100)

spacebar=0

for x in members: #Output section with widgets
    lst_tree.insert(END, " "*spacebar+f"Name: {x.name} -- Surname: {x.surname} -- Age: {x.age} -- Partner: {x.partner}")
    lst_tree.insert(END, "")
    spacebar+=5

window.mainloop()


time.sleep(15)