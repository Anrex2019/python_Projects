def swap_case(swap):
    string = ''
    
    for char in swap:
        if char.lower():
            string += char.upper()
        else:
            string += char.lower

    return string
