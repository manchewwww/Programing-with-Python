def is_valid_last_digit(ucn):
    sum = 0
    weights = [2, 4, 8, 5, 10, 9, 7, 3, 6]
    for i in range(9):
        sum += (int(ucn[i]) * weights[i])
  
    control_digit = sum % 11
    if(control_digit < 10):
        return control_digit == int(ucn[9])
    else:
        return int(ucn[9]) == 0

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def is_valid_UCN(ucn, *, bypass_checksum=False):
    if len(ucn) != 10:
        return False

    year = int(ucn[0:2])
    month = int(ucn[2:4])
    day = int(ucn[4:6])

    if 1 <= month <= 12 :
        year += 1900
    elif 21 <= month <= 32:
        year += 1800
        month -= 20
    elif 41 <= month <= 52:
        year += 2000
        month -= 40
    else:
        return False

    if 31 < day  or day <= 0:
        return False
    elif month in [4,6,9,11] and day > 30:
        return False
    elif month == 2:
        if day > 29:
            return False 
        elif is_leap_year(year) == False and day > 28:
            return False
        
    if bypass_checksum is True:
        return True
    elif is_valid_last_digit(ucn):
        return True
    else:
        return False

print(is_valid_UCN("6101057509") == True)
print(is_valid_UCN("6101057500", bypass_checksum=True) == True)
print(is_valid_UCN("6101057500") == False)
print(is_valid_UCN("6913136669") == False)