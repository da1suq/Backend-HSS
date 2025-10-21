# main.py
import rich


def main():
    rich.print('Hello World from "2025"')
    print('Labuda')
    n = int(input())
    k = 1
    for i in range(1, n+1, 1):
        k *= i;
        print(k)
    
if __name__ == "__main__":
    main()
    
