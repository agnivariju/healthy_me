#--------->import dependencies<-------#
import datetime


def gettime():
    return datetime.datetime.now()

#-------------->lock<--------------------#


def lock(name):
    if (name == 1):
        c = int(input('Enter 1 for excercise and 2 for food \n'))
        if c == 1:
            value = input('type here \n')
            with open('agniva-ex.txt', 'a') as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written\n")
        elif c == 2:
            value = input('Enter value: \n')
            with open('agniva-food.txt', 'a') as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written\n")
    elif (name == 2):
        c = int(input('Enter 1 for excercise and 2 for food \n'))
        if c == 1:
            value = input('Enter value: \n')
            with open('pallab-ex.txt', 'a') as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written\n")
        if c == 2:
            value = input('Enter value: \n')
            with open('pallab-food.txt', 'a') as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written\n")
    elif (name == 3):
        c = int(input('Enter 1 for excercise and 2 for food\n'))
        if c == 1:
            value = input('Enter value: \n')
            with open('rima-ex.txt', 'a') as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written\n")
        if c == 2:
            value = input('Enter value: \n')
            with open('rima-food.txt', 'a') as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written\n")
    else:
        print(
            "Please enter a valid input ---> (1) for Agniva (2) for Pallab and (3) for Rima\n")

#--------> retreive <-------------#


def retrieve(name):
    if (name == 1):
        c = int(input('Enter 1 for excercise and 2 for food\n'))
        if c == 1:
            with open('agniva-ex.txt') as op:
                for i in op:
                    print(i, end="")

        if c == 2:
            with open('agniva-food.txt') as op:
                for i in op:
                    print(i, end="")

    if (name == 2):
        c = int(input('Enter 1 for excercise and 2 for food\n'))
        if c == 1:
            with open('pallab-ex.txt') as op:
                for i in op:
                    print(i, end="")

        if c == 2:
            with open('pallab-food.txt') as op:
                for i in op:
                    print(i, end="")

    if (name == 3):
        c = int(input('Enter 1 for excercise and 2 for food\n'))
        if c == 1:
            with open('rima-ex.txt') as op:
                for i in op:
                    print(i, end="")

        if c == 2:
            with open('rima-food.txt') as op:
                for i in op:
                    print(i, end="")


#--------->main<------------------#
print('Fittness Management Program ')
a = int(input('Enter 1 for lock and 2 for retrieve\n'))
if a == 1:
    b = int(input('Press 1 for agniva, 2 for pallab and 3 for rima \n'))
    lock(b)
else:
    b = int(input('Enter 1 for agniva, 2 for pallab and 3 for rima \n'))
    retrieve(b)
