import random


class Library:
    # lend = 0
    def __init__(self, bookname, nameofbuyer, id):
        self.bookname = bookname
        self.nameofbuyer = nameofbuyer
        self.id = id

    def displaydetails(self):
        return "name {} has lent a book {} having id {}.".format(self.nameofbuyer , self.bookname , self.id)

    def displayname(self):
        return (self.bookname)

    def lendbook(self, lend):
        lender = lend + 1
        print("book having name {} has been taken on lent".format(self.bookname))
        return lender - 1
''
    def addbook(self, newbook, copies):
        self.newbook = newbook
        self.copies = copies
        return {newbook: copies}

    def returnbook(self, lend):
        lend -= 1
        print("now he have to return ", lend)
        print("You have returned the {}".format(self.bookname))

    def forfile(self):
        return self.bookname , self.nameofbuyer , self.id


'''
rohan = Library("zozo", "rakesh", 23)
print(rohan.displayname())
print(rohan.lendbook(3))
print(rohan.addbook("hola", 2))
print(rohan.returnbook(2))
'''

if __name__ == "__main__":
    while (True):
        ch = input("Do You Want To Enter Into Library?: yes/no\n")
        if ch == 'yes':
            print("Enter what do you want to do in LIBRARY by Selecting Numbers as per given choices:\n")
            cho = input(
                " 1.Display All Details\n 2.Display Name Of Book\n 3.Lend Book From Library\n 4.Donate/Add book to library\n 5.Return book to Library\n 6.Details in file\n")
            if cho == "1":
                chh = input("enter the name of book you want: ")
                chh1 = input("enter the name of you: ")
                chh2 = random.randint(1, 10)
                chh3 = Library(chh, chh1, chh2)
                print(chh3.displaydetails())

            elif cho == "2":
                 jj = input("did you fill details yes/no\n")
                 if jj == 'yes':
                    print(chh3.displayname())
                 else:
                     print("Fill detail first man\n")
                     chh = input("enter the name of book you want: ")
                     chh1 = input("enter the name of you: ")
                     chh2 = random.randint(1, 10)
                     chh3 = Library(chh, chh1, chh2)
                     print(chh3.displaydetails())

            elif cho == "3":
                jj = input("did you fill details yes/no\n")
                if jj == 'yes':
                    print(chh3.lendbook(1))
                else:
                    print("Fill detail first man\n")
                    chh = input("enter the name of book you want: ")
                    chh1 = input("enter the name of you: ")
                    chh2 = random.randint(1, 10)
                    chh3 = Library(chh, chh1, chh2)
                    print(chh3.lendbook(1))

            elif cho == "4":
                cm = input("give name of book want to add: ")
                vv = input("Give me your name: ")
                chh2 = random.randint(1, 10)
                chh3 = Library(0,vv,chh2)
                print(chh3.addbook(cm , vv))

            elif cho == "5":
                cn = input("Book You want to return: ")
                chh1 = input("enter the name of you: ")
                chh2 = random.randint(1, 10)
                chh3 = Library(ch, chh1, chh2)
                print(chh3.returnbook(1))

            elif cho == "6":
                cj = input("did you fill details: yes/no?\n")
                if cj == 'yes':
                    filee = open("LMF.txt","r+")
                    db = filee.write("-------LIBRARY MANAGEMENT SYSTEM------- \n\n name of book which you lent is {}\n Your name is {}\n Your Id is {}".format(chh,chh1,chh2))
                    print(db)
                    filee.close()
                else:
                    print("Try Next Time Brother")





        cc = input("Want to continue? yes/no\n")
        if cc == "no":
             break