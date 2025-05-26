
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
    