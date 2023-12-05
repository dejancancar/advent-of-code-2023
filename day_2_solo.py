if __name__ == '__main__':
    with open('/Users/dejancancar/advent-of-code-2023/day_2_input.txt', 'r') as f:
        games = f.read().split('\n')
    total = 0
    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14
    for game in games:
        game_set = game.split(': ')
        game_number = int(game_set[0].split(' ')[-1])

        all_cubes = game_set[1]
        sets = all_cubes.split('; ')
        add_to_total = True

        for set in sets:
            green_count = 0
            red_count = 0
            blue_count = 0
            count_and_colors = set.split(', ')
            for count_and_color in count_and_colors:
                count, color = count_and_color.split()
                count = int(count)
                if color == 'green':
                    green_count += count
                elif color == 'red':
                     red_count += count
                elif color == 'blue':
                    blue_count += count
                if green_count > green_cubes or blue_count > blue_cubes or red_count > red_cubes:
                    add_to_total = False

        if add_to_total:
            total += game_number

    print(f'Part 1 = {total}')

    with open('/Users/dejancancar/advent-of-code-2023/day_2_input.txt', 'r') as f:
        games = f.read().split('\n')
    total = 0
    for game in games:
        red_cubes = 0
        green_cubes = 0
        blue_cubes = 0
        game_set = game.split(': ')
        game_number = int(game_set[0].split(' ')[-1])

        all_cubes = game_set[1]
        sets = all_cubes.split('; ')

        for set in sets:
            green_count = 0
            red_count = 0
            blue_count = 0
            count_and_colors = set.split(', ')
            for count_and_color in count_and_colors:
                count, color = count_and_color.split()
                count = int(count)
                if color == 'green':
                    green_count += count
                    if green_count > green_cubes:
                        green_cubes = green_count
                elif color == 'red':
                     red_count += count
                     if red_count > red_cubes:
                        red_cubes = red_count
                elif color == 'blue':
                    blue_count += count
                    if blue_count > blue_cubes:
                        blue_cubes = blue_count

        total += (red_cubes * blue_cubes * green_cubes)

    print(f'Part 2 = {total}')