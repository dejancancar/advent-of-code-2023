if __name__ == '__main__':
    total = 0
    red = 12
    green = 13
    blue = 14
    with open('/Users/dejancancar/advent-of-code-2023/day_2_input.txt', 'r') as f:
        texts = f.read().split('\n')
        total = 0
        for text in texts:
            passed = True
            game = text.split(': ')
            game_number = int(game[0].split(' ')[-1])
            sets = game[1].split('; ')
            for set in sets:
                colors_count = {}
                colors = set.split(', ')
                for color in colors:
                    colors_count[color.split(' ')[-1]] = int(color.split(' ')[0])

                if int(colors_count.get('red', 0)) > red:
                    passed = False
                if int(colors_count.get('green', 0)) > green:
                    passed = False
                if int(colors_count.get('blue', 0)) > blue:
                    passed = False

            if passed:
                total += game_number

    print(total)
            