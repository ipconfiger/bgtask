from service import do_add


def main():
    do_add.delay(1, 2)


if __name__ == "__main__":
    main()
