import random
import main

def start():
    while True:
        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 4

        cuypy_position = random.randint(1, 4)

        goa = goa_kosong.copy()
        goa[cuypy_position - 1] = "|0_0|"

        goa_kosong = ' '.join(goa_kosong)
        goa = ' '.join(goa)

        print(f'Coba perhatikan goa dibawah ini\n\n{goa_kosong}\n')

        pilihan_user = int(input('Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: '))

        if pilihan_user == cuypy_position:
            print(f'\n{goa}\n\nSelamat Kamu Menang 🏆')
        else:
            print(f'\n{goa}\n\nUncchhh kamu kalah 🙊')

        play_again = input('\n\napakah ingin melanjutkan gamenya lagi? [y/n] ').lower()
        if play_again != 'y':
            break


if __name__ == '__main__':
    start()