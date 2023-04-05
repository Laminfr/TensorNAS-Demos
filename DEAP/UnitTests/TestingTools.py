def Compare(value1, value2):
    return value1 == value2

def get_global(var_name):
    try:
        return globals()[var_name]
    except:
        return None


def set_global(var_name, val):

    globals()[var_name] = val