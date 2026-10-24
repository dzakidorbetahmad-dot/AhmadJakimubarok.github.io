import random


def start():
    while True:
        bentuk_goa = "[-]"
        goa_kosong = [bentuk_goa] * 4

        zamorapy_position = random.randint(1, 4)

        goa = goa_kosong.copy()
        goa[zamorapy_position - 1] = "[0-0]"

        goa_kosong = ' '.join(goa_kosong)
        goa = ' '.join(goa)

        print(f'coba perhatikan goa di bawah ini \n\n {goa_kosong}\n')

        pilihan_user = int(input('menurut kamu di goa berap zamorapy berada [1/2/3/4]: '))

        if pilihan_user == zamorapy_position:
            print(f'{goa} selamat kamu menang')
        else:
            print(f'{goa} maaf kamu kalah')

        play_again = input('\napakah kamu mau mulai gamenya lagi [y/n]: ').strip().lower()
        if play_again not in ('y', 'yes'):
            print('program game selesai')
            return


if __name__ == '__main__':
    start()