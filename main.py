# the calculator is going to ask for your name, your department then ask for the total courses and also the credit
# unit per each course then, it'll ask for your grades in each. At the end, it's going to display your GPA
# IT HAS BEEN SUCCESSFULLY DONE!!!
# Note: WHEN USING "WHILE TRUE", YOU MUST PUT BREAK STATEMENT AT THE ENDING!!!
import sys

print("A GPA CALCULATOR....\nPress (q) at any time to QUIT")
print()
def theClass(decideclass):

    # this function checks the class of the user

    if decideclass >= 4.50:
        print("You are a FIRST class candidate!! \nEXCELLENT⭐⭐⭐⭐⭐")
    elif decideclass > 3.49 and decideclass < 4.49:
        print("You are a second class UPPER candidate!! \nVERY GOOD BUT PUT IN MORE EFFORT⭐⭐⭐⭐")
    elif decideclass > 2.49 and decideclass < 3.49:
        print("You are a second class LOWER candidate!! \nGOOD BUT INCLINE MORE TOWARDS YOUR STUDIES⭐⭐⭐")
    else:
        print("You are a THIRD CLASS candidate! \nVERY POOR, PRAY FOR GRACE⭐")

def script():
    names = []
    each = []
    grade = []
    new_grade = []
    total_score = [] # this is the main sum for each of the courses

    def check(lst):
    # this is a function to assign the
    # corresponding number from a letter

        for i in range(len(lst)):
            if lst[i] == 'a':
                new_grade.append(5)
            elif lst[i] == 'b':
                new_grade.append(4)
            elif lst[i] == 'c':
                new_grade.append(3)
            elif lst[i] == 'd':
                new_grade.append(2)
            elif lst[i] == 'e':
                new_grade.append(1)
            else:
                new_grade.append(0)

    while True: 
        name = input("What's your NAME? ").lower()
        if name == 'q':
            take = input("Are you sure you want to quit? (y)es or (n)o: ").lower()
            if take == 'y':
                print()
                print("Oops! you just pressed (q)uit...ByeBye👋!!!")
                sys.exit()
            if take == 'n':
                print()
                continue
            if take != 'y' and take != 'n':
                print("please enter (y)es or (n)o to quit...")
                print()
                continue
        break      

    while True:
        dep = input("Which DEPARTMENT are you in? ").lower()
        if dep == 'q':
            taken = input("Are you sure you want to quit? (y)es or (n)o: ").lower()
            if taken == 'y':
                print()
                print("Oops! you just pressed (q)uit...ByeBye👋!!!")
                sys.exit()
            if taken == 'n':
                print()
                continue
            if taken != 'y' and taken != 'n':
                print("please enter (y)es or (n)o to quit...")
                print()
                continue
        break
    while True:
        try:
            okay = input("How many courses did you offer? ").lower()
            if okay == 'q':
                correct = input("Are you sure you want to quit? (y)es or (n)o: ").lower()
                if correct == 'y':
                    print()
                    print("Oops! you just pressed (q)uit...ByeBye👋!!!")
                    sys.exit()
                elif correct == 'n':
                    print()
                    continue
                else:
                    print("please enter (y)es or (n)o to quit...")
                    print()
                    continue
                
            tot = int(okay)
            if tot < 0:
                print("Please enter a positive number!!!")
                print()
                continue
        except ValueError:
            print("Please enter a valid whole number!!!")
            print()
            continue
        break

    print()

    for i in range(tot):
        while True:
            n = input("What's the number " + str(i + 1) + ' course name? ').lower()
            if n == 'q':
                tak = input("Are you sure you want to quit? (y)es or (n)o: ").lower()
                if tak == 'y':
                    print()
                    print("Oops! you just pressed (q)uit...ByeBye👋!!!")
                    sys.exit()
                if tak == 'n':
                    print()
                    continue
                if tak != 'y' and  tak != 'n':
                    print("please enter (y)es or (n)o to quit...")
                    print()
                    continue
            break
        names.append(n)
    print()

    z = 0
    while z < tot:
        try:
            first_e = input(f"What's {names[z].title()} total credit unit? ").lower()
            if first_e == 'q':
                corr = input("Are you sure you want to quit? (y)es or (n)o: ").lower()
                if corr == 'y':
                    print()
                    print("Oops! you just pressed (q)uit...ByeBye👋!!!")
                    sys.exit()
                elif corr == 'n':
                    print()
                    continue
                else:
                    print("please enter (y)es or (n)o to quit...")
                    print()
                    continue

            e = int(first_e)
            if e < 0:
                print("Please enter a positive number!!!")
                print()
                continue
            each.append(e)
        except ValueError:
            print("Please enter a valid whole number!!!")
            print()
            continue
        z += 1

    total_units = sum(each) # if this doesn't work, I'll just ask for it from the user
    print()

    print("Please enter any of the following letters: (a), (b), (c), (d), (e), (f) or (s)kip below...")
    print()
    p = 0
    while p < tot:  # this loop is very important.
        the_inp = input(f"What's your grade in {names[p].title()}? ").lower()
        if the_inp == 'q':
            ta = input("Are you sure you want to quit? (y)es or (n)o: ").lower()
            if ta == 'y':
                print()
                print("Oops! you just pressed (q)uit...ByeBye👋!!!")
                sys.exit()
            if ta == 'n':
                print()
                continue
            if ta != 'y' and ta != 'n':
                print("please enter (y)es or (n)o to quit...")
                print()
                continue
        if the_inp != 'a' and the_inp != 'b' and the_inp != 'c' and the_inp != 'd' and the_inp != 's' and the_inp != 'e' and the_inp != 'f':
            print("Please enter any of the following letters: (a), (b), (c), (d), (e), (f) or (s)kip")
            print()
            continue
        grade.append(the_inp)
        p += 1
    check(grade)

    for i in range(tot):
        now = new_grade[i] * each[i]
        total_score.append(now)
    for i in range(tot):
        if grade[i] == 'f':
            pass
        if grade[i] == 's':
            total_units -= each[i]
    print()
    try:
        gpa = (sum(total_score)) / total_units

        print(f"Hello {name.title()}! Your GPA is {gpa.__round__(2)}")
        theClass(gpa)
        print()
    except Exception: # This is to handle cases where all the courses were skipped and other unknown causes of errors.
        print(f"Hello {name.title()}! Your GPA is 0.0")
        print("You are a THIRD CLASS candidate! \nVERY POOR, PRAY FOR GRACE⭐")
        print()

    while True: # There's no need for a break statement here because (n)o must be pressed at the end.
        choice = input(f"Hey {name.upper()}! Do you want to RESTART? (y)es or (n)o: ").lower()

        if choice == 'y':
            print()
            script() # The function calls itself so t5hat everything can be repeated again.
        elif choice == 'n':
            print()
            print("Thank you for calculating your GPA with us❤")
            sys.exit()
        else:
            print("Please enter (y)es or (n)o...")
            print()
            continue


script() # This is very important as the restart option cannot work without this calling.
