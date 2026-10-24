def start():
    while True:
        print('ini warung apps!')
        play_again = input('kembali ke menu utama? [y/n] ').strip().lower()

        if play_again in ('y', 'yes'):
            print('kembali ke menu utama')
            return


if __name__ == '__main__':
    start()