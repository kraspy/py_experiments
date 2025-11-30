def traffic_sign(n):
    if n > 0:
        traffic_sign(n - 1)
        print('Не парковаться')


def main():
    traffic_sign(5)


if __name__ == '__main__':
    main()
