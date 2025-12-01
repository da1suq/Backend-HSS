def main():
    numbers = list(map(int, input('Введите последовательность чисел:').split()))
    while len(numbers) == 1:
        print('Вы ввели только одно число, введите хотя бы 2 ')
        numbers = list(map(int, input('Введите последовательность чисел:').split()))
    answer = []
    for i in range(len(numbers)):
        minDifference = max(abs(10**18 - numbers[i]), abs(-10**18 - numbers[i]))
        ansNum = 0
        for j in range(len(numbers)):
            if i != j:
                if abs(numbers[j] - numbers[i]) < minDifference:
                    minDifference = abs(numbers[j] - numbers[i])
                    ansNum = numbers[j]
        answer.append(ansNum)
    print(" ".join(map(str, answer)))
        
if __name__ == "__main__":
    main()
