if __name__ == '__main__':
    n = int(input())
    # 0 <= i <= 20
    for i in range(21):
        if i < n:
            print(i ** 2)
