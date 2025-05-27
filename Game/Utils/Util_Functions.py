<<<<<<< HEAD

def check_if_int(value, callback=None):
    try:
        int(value)
        return True
    except ValueError:
        return False
        print("That's not a int.")
        callback()

    
def check_if_float(value, callback=None):
    try:
        float(value)
        return True
    except ValueError:
        return False
        print("That's not a float.")
        callback()


def check_if_str(value, callback=None):
    try:
        str(value)
        return True
    except ValueError:
        return False
        print("That's not a string.")
        callback()
    
=======
import tabulate


def create_map(length, width):
    grid = []
    for i in range(length):
        grid.append([])

        for j in range(width):
            grid[i].append(None)
    return grid
#print(tabulate.tabulate(create_map(5,5), tablefmt='rounded_grid'))
b
>>>>>>> 445bfd8204a086ab722345e14602541ede91baaf
