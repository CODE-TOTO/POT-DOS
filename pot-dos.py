import os
import time

def reg_and_login():
    registered_user = input("You are not registered yet, please enter your username:")

    while True:
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
        else:
            print("Error: the instructions you entered are invalid. Please retry.")

if __name__ == '__main__':
    main()