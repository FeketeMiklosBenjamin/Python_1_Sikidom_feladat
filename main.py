def main() -> None:
    print('A téglalap kerületét kiszámoló függvény!')
    a : float = float(input('a (oldal) = '))
    b : float = float(input('b (oldal) = '))
    if a < 1 or b < 1:
        print('A megadott adatokkal nem lehet számolni!')
    else:
        téglalap_kerület: float = 2 * (a + b)
        print(f'A téglalap kerülete: {téglalap_kerület}')


if __name__ == "__main__":
    main()