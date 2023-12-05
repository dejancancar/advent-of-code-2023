if __name__ == '__main__':
    with open('/Users/dejancancar/advent-of-code-2023/day_1_input.txt', 'r') as f:
        texts = f.read().split('\n')
    total = 0
    for text in texts:
        numbers = ''.join(char for char in text if char.isdigit())
        first_int = numbers[0]
        last_int = numbers[-1]
        result = int(first_int + last_int)
        total += result 

print(total)