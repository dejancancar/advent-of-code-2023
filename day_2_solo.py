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
        total_sets = len(sets)
        while total_sets >= 0:
            green_count = 0
            red_count = 0
            blue_count = 0
            total_sets -= 1
            cubes = sets[total_sets]
            count_and_colors = cubes.split(', ')
            for count_and_color in count_and_colors:
                count, color = count_and_color.split()
                count = int(count)
                if color == 'green':
                    green_count += count
                elif color == 'red':
                     red_count += count
                elif color == 'blue':
                    blue_count += count
            if green_count >= green_cubes or blue_count >= blue_cubes or red_count >= red_cubes:
                continue

            if green_count <= green_cubes and blue_count <= blue_cubes and red_count <= red_cubes and total_sets == 0:
                total += game_number

print(total)