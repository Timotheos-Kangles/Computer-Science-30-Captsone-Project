#import tabulate


def create_map(length, width):
    grid = []
    for i in range(length):
        grid.append([])

        for j in range(width):
            grid[i].append(None)
    return grid
#print(tabulate.tabulate(create_map(5,5), tablefmt='rounded_grid'))

def debug_player_data():
    pass