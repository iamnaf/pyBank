#Py Bank to simulate the process of an ATM and a bank account
#adding the name is just a formal thing, it does not really affect the program
#this program was written in python 3, but it will be compatible with python 2
#the following options were successfully implemented
#Carry out deposit
#Carry out withdrawal
#Check account balance
#change pin
#there is an opening balance of N1,000,000, which you can work with through deposit and withdrawal
#THe default pin is 0000
#After running and closing of this program, it reverts back to default
#You can carry out multiple transaction from running the program just once
#all inputs are integer values except the very first input which is the name
#Any attempt to input another value other than integer will break the program because the exception is not handled
#you can work further by taking this code apart and see what you can do differently and still give same output
#you can learn more about exception handling in python to see if you can handle the input exceptions
#for any contact or enquiries, you can send me a message on WhatsApp 07033131921, i will try my best to answer asap
#Thank you for choosing NAEEES python infotech program.

name = input("Please enter your name to create an account in our bank >>> ")
print ("Welcome {}, we will give you an auto-generated account number for a one time use".format(name))

opBal = 1000000

accNum = 1234567890

defPin = 0000


class Account():

    def __init__(self, accName, accNum, defPin, opBal):
        self.accName = accName
        self.accNum = accNum
        self.defPin = defPin
        self.opBal = opBal

    def setNewPin(self, defPin, newPin):
        print ("your default pin is {}".format(self.dePin))
        print ("///You have to change your pin///")
        self.newPin = int(raw_input("Enter your new 4-digit pin >>> "))
        self.defPin = self.newPin
        return self.newPin


class Bank():


    newAcc = Account(name, accNum, defPin, opBal)

    def __init__(self, accNum, defPin):
        self.accNum = accNum
        self.defPin = defPin
        #self.newPin = newPin

    
    def depositMoney(self):
        print("How much do you want to deposit")
        print()
        print("Press")
        print("1. for N1000")
        print("2. for N5000")
        print("3. for N10000")
        print("4. for N20000")
        print("5. to enter your desired amount")
        reply = int(input(">>> "))
        print()
        if reply == 1:
            self.newAcc.opBal += 1000
        elif reply == 2:
            self.newAcc.opBal += 5000
        elif reply == 3:
            self.newAcc.opBal += 10000
        elif reply == 4:
            self.newAcc.opBal += 20000
        elif reply == 5:
            dep = int(input(">>> Enter amount "))
            self.newAcc.opBal += dep
        else:
            print("Your option is not available, please try again")
            self.depositMoney()
        print()
        print()
        print("Your new balance is now N{}\n".format(self.newAcc.opBal))
        self.checkOut()
    
    def withdrawMoney(self):
        print("How much do you want to withdraw")
        print()
        print("Press")
        print("1. for N1000")
        print("2. for N5000")
        print("3. for N10000")
        print("4. for N20000")
        print("5. to enter your desired amount")
        reply = int(input(">>> "))
        print()
        if reply ==1:
            if self.newAcc.opBal >= 1000:
                self.newAcc.opBal -= 1000
                print("You have withdrawn N1000")
                print("Your new account balance is now N{}\n".format(self.newAcc.opBal))
                print()
                self.checkOut()
            else:
                print("Insufficient amount in your account to withdraw N1000\n")
                self.startPage()
        elif reply == 2:
            if self.newAcc.opBal >= 5000:
                self.newAcc.opBal -= 5000
                print("You have withdrawn N5000")
                print("Your new  account balance is now N{}\n".format(self.newAcc.opBal))
                print()
                self.checkOut()
            else:
                print("Insufficient amount in your account to withdraw N5000\n")
                self.startPage()
        elif reply == 3:
            if self.newAcc.opBal >= 10000:
                self.newAcc.opBal -= 10000
                print("You have withdrawn N10000")
                print("Your new account balance is now N{}\n".format(self.newAcc.opBal))
                print()
                self.checkOut()
            else:
                print("Insufficient amount in your account to withdraw N10000\n")
                self.startPage()
        elif reply == 4:
            if self.newAcc.opBal >= 20000:
                self.newAcc.opBal -= 20000
                print("You have withdrawn N20000")
                print("Your new account balance is now N{}\n".format(self.newAcc.opBal))
                print()
                self.checkOut()
            else:
                print("Insufficient amount in your account to withdraw N20000\n")
                self.startPage()
        elif reply == 5:
            print("Enter your desired amount\n")
            withd = int(input(">>> "))
            if self.newAcc.opBal >= withd:
                self.newAcc.opBal -= withd
                print("You have withdrawn N{}".format(withd))
                print("Your new account balance is now N{}\n".format(self.newAcc.opBal))
                print()
                self.checkOut()
            else:
                print("insufficient amount in your account to withdraw N{}\n".format(withd))
                self.startPage()
                
        else:
            print("That option is not available, please try again\n")
            self.withdrawMoney()

    def checkBalance(self):
        print("Your account balance is N{}".format(self.newAcc.opBal))
        print()
        self.checkOut()

    def changePin(self):
        print("Please enter your old pin")
        oldpin = int(input(">>> "))
        if oldpin != self.defPin:
            print("Incorrect Pin, try again")
            print()
            self.changePin()
        else:
            print("Please enter your new 4-digit pin")
            newPin = int(input(">>> "))
            print("Please enter your new 4-digit pin again")
            newPin2 = int(input(">>> "))
            if newPin == newPin2:
                print("Your pin has been changed succesfully")
                self.defpin = newPin
                print()
                self.checkOut()
            else:
                print("Your new digit pin do not match, please try again")
                print()
                self.changePin()


    def checkOut(self):
        print("Do you want to carry out another transaction")
        print()
        print("1. to carry out another transaction")
        print("2. to end")
        rep = int(input(">>> "))
        print()
        if rep == 1:
            self.startPage()
        elif rep == 2:
            print("It is not BYE-BYE but SEE-YOU-AGAIN")
            print("Thank you for Banking with us")
            exit

    def startPage(self):
        print("Welcome to PyBank Limited")
        print()
        print("Here, Customer is KING")
        print()
        print("Please enter your pin to continue")
        pin = int(input(">>> "))
        if pin == self.defPin:
            pass
        else:
            print("You have entered a wrong pin, please try again")
            print()
            self.startPage()
        print("What would you like to do\n")
        print("1. to carry out a deposit")
        print("2. to carry out a withdrawal")
        print("3. to check account balance")
        print("4. to change your pin")
        print("5. to quit")
        reply = int(input(">>> "))
        print()
        if reply == 1:
            self.depositMoney()
        elif reply == 2:
            self.withdrawMoney()
        elif reply == 3:
            self.checkBalance()
        elif reply == 4:
            self.changePin()
        elif reply == 5:
            print("It is not BYE-BYE but SEE-YOU-AGAIN")
            print("Thank you for Banking with us")
            exit
        else:
            print("You have selected an invalid option, please try again")
            self.startPage()

newBank = Bank(accNum, defPin)
newBank.startPage() 