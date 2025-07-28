import os
import time
import random

def reg_and_login():
    while True:
        registered_user = input("You are not registered yet, please enter your username:")
        if(registered_user == ''):
            print("Error: you didn't enter any characters. Please retry.")
            continue
        else:
           print("Registration is complete!")
           break

    while True:
        global set_root_password
        set_root_password = input("Please enter your superuser's password:")
        if(set_root_password == ''):
            print("Error: you didn't enter any characters. Please retry.")
            continue
        else:
            print("The setup was successful!")
            print("Because of privacy issues, the screen will be cleared next.")
            time.sleep(1.5)
            os.system("cls")
            break

    login_user = input("You have completed the registration, please enter the username you want to log in to (super user is root):")
    if(login_user == registered_user):
        print(f"You are logged in {login_user}. Not a superuser.")
    else:
        while True:
            password = input("Please enter the password of the superuser:")
            if(password == set_root_password):
                print("You're logged in to Superuser!")
                print("Because of privacy issues, the screen will be cleared next.")
                time.sleep(1)
                os.system("cls")
                break
            else:
                print("Error: password error. Please retry.")
                continue

def main():
    num = random.randint(1, 100)
    reg_and_login()
    while True:
        code = input("POT-DOS$>")
        if(code == "version"):
            print("*******           *****         *******                  *******           *****")
            print("*       *        *     *           *                     *      *         *     *         ****")
            print("*       *       *       *          *                     *      *        *       *       *    *")
            print("*       *       *       *          *                     *      *        *       *       *")
            print("*******         *       *          *       *******       *      *        *       *        ****")
            print("*               *       *          *                     *      *        *       *            *")
            print("*               *       *          *                     *      *        *       *       *    *")
            print("*                *     *           *                     *      *         *     *         ****")
            print("*                 *****            *                     *******           *****")
            print("                                          V alpha1.0")
        elif(code == "exit"):
            print("logout")
            ifexit = input()
            exit()
        elif(code == "cls"):
            os.system("cls")
            print("Successfully cleared the screen.")
        elif(code == "help"):
            print("help:")
            print("1.version -- Check the version.")
            print("2.exit -- Logout and exit.")
            print("3.cls -- Clear screen.")
            print("4.rp -- View superuser passwords. But you need to enter it first.")
            print("5.gtn -- Guess the numbers game.")
        elif(code == "rp"):
            password = input("Please enter the password of the superuser:")
            print(f"The password for the superuser is {set_root_password}.")
            print("Because of privacy issues, the screen will be cleared next.")
            time.sleep(1)
            os.system("cls")
        elif(code == "gtn"):
            os.system("cls")
            print("Welcome to Guess the Numbers v1.0!")
            while True:
                gnm = input("Please guess a number from 1-100:")
                if(num == int(gnm)):
                    print("Congratulations on guessing right!")
                    ifcontinue = input("Do you want to play another game? Y/N")
                    if(ifcontinue == "Y"):
                        os.system("cls")
                        continue
                    else:
                        break
                elif(num != int(gnm)):
                    if(int(gnm) > num):
                        print("Sorry, you guessed too much. Guess again!")
                    else:
                        print("Sorry, you guessed too little. Guess again!")
                    continue
                else:
                    print("Input error. Please retry.")
        else:
            print("Error: the instructions you entered are invalid. Please retry.")

if __name__ == '__main__':
    main()