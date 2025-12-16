import argparse
from decimal import Decimal
import re

def main():
    accounts = {}
    users = {}
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename, encoding='utf-8') as file:
        for line in file:
            parsedLine = re.search(r'"(.+)"\s*-\s*(\d+):\s*([+-])(\d+(\.\d+)?)', line)
            name = parsedLine.group(1)
            id = parsedLine.group(2)
            sign = parsedLine.group(3)
            sum = Decimal(parsedLine.group(4))
            if sign == '-':
                sum = -sum
            if id not in accounts:
                accounts[id] = 0
            accounts[id] += sum
            if name not in users:
                users[name] = set()
            users[name].add(id)
    for name in users:
       parts = []
       for acc in sorted(users[name]):
           balance = accounts[acc]
           parts.append(f"{acc}: {balance}") 
       print(f"\"{name}\" - {', '.join(parts)}")

if __name__ == "__main__":
    main()
