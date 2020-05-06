def ticket():
    name = input("enter your name: ")
    contact = int(input("enter your contact no: "))
    time = input("enter the time : ")
    start = input("enter the starting place ")
    destination = input("enter the destination ")
    rate_per_Seat = 250
    seats = int(input(" Enter no of seats: "))
    total_price = rate_per_Seat * seats
    return [{'ticketData': [name, contact, time, start + " " "to" " " + destination, total_price]}]


def book():
    ticketData = []
    ticketData.extend(ticket())
    savedata(ticketData)
    return ticketData


def savedata(ticketData):
    fopen = open('book.txt', 'a')
    fopen.write(str(ticketData) + '\n')
    fopen.close()


def fetchData(): 
    fopen = open('book.txt', 'r')
    data = fopen.read()
    fopen.close()
    return data


print("------Bus Ticket Management System----------")
ticketBook = []
clear = ""
flag = True
print("welcome please choose from the options given ")
while flag:
    print("for booking  press 'b' or 'B'")
    print("to view your ticket press 'v' or 'V'")
    print("for canceling ticket press 'c' or 'C'")

    print("******************************************")

    userinput = input("enter your choice: ")
    if userinput == 'b' or userinput == 'B':
        ticketBook.extend([book()])
        # print(ticketBook)
        print("**************************************")
    elif userinput == 'v' or userinput == 'V':
        viewData = fetchData()
        print(viewData)

    elif userinput == 'c' or userinput == 'C':
        fopen = open('book.txt', 'r')
        clear = fopen.read()
        del clear
        print("deleted")
        fopen.close()

    else:
        print("Invalid Option!!!")
