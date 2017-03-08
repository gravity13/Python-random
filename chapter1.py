

def sum(number_1, number_2):
    number_1 = convert_integer(number_1)
    number_2 = convert_integer(number_2)

    result = number_1 + number_2

    return result

def convert_integer(number_string):

    converted_integer = int(number_string)
    return converted_integer

answer = sum("2","3")

print answer