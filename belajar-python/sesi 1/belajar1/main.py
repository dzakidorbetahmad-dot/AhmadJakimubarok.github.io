from libs import welcome_message, exit_program
from games import zamora
from tools import warung


def menu():
    while True:
        try:
            user_option = int(input('menu program:\n1. Games CUYPY\n2. Warung Mini\n3. keluar program\n\nsilahkan pilih: '))
        except ValueError:
            print('hanya boleh pilih angka yang tersedia di menu!')
            continue

        if user_option == 1:
            zamora.start()
        elif user_option == 2:
            warung.start()
        elif user_option == 3:
            exit_program()
            break
        else:
            print('hanya boleh pilih yang tersedia di menu!')


def main():
    welcome_message()
    menu()


if __name__ == '__main__':
    main()