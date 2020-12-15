# day 4: passport processing
# need to insert two empty lines after last line in file
def passport_processing_one():
    input_file = open('input/passport_processing', 'r')

    passport = ''
    valid = 0

    for line in input_file:
        if line == '\n':
            if 'byr:' in passport and 'iyr:' in passport and 'eyr:' in passport \
                    and 'hgt:' in passport and 'hcl:' in passport and 'ecl:' in passport and 'pid:' in passport:
                valid += 1
            passport = ''
        else:
            passport += line
    print(valid)


def passport_processing_two():
    input_file = open('input/passport_processing', 'r')

    passport = ''
    valid = 0

    for line in input_file:
        if line == '\n':
            if valid_passport(passport):
                valid += 1
            passport = ''
        else:
            passport += ' ' + line.strip()
    print(valid)


def valid_passport(passport):
    if 'byr:' not in passport or 'iyr:' not in passport or 'eyr:' not in passport \
            or 'hgt:' not in passport or 'hcl:' not in passport or 'ecl:' not in passport or 'pid:' not in passport:
        return False
    parts = passport.strip().split(' ')
    for field in parts:
        key = field.split(':')[0]
        value = field.split(':')[1]
        if key == 'byr' and (int(value) < 1920 or int(value) > 2002):
            return False
        if key == 'iyr' and (int(value) < 2010 or int(value) > 2020):
            return False
        if key == 'eyr' and (int(value) < 2020 or int(value) > 2030):
            return False
        if key == 'hgt':
            measure = value[len(value) - 2:]
            height = value[:len(value) - 2]
            if measure != 'in' and measure != 'cm':
                return False
            if measure == 'in' and (int(height) > 76 or int(height) < 59):
                return False
            if measure == 'cm' and (int(height) > 193 or int(height) < 150):
                return False
        if key == 'hcl' and (value[0] != '#' or not re.match('^[1234567890abcdef]+$', value[1:])):
            return False
        if key == 'ecl' and value != 'amb' and value != 'blu' and value != 'brn' and \
                value != 'gry' and value != 'grn' and value != 'hzl' and value != 'oth':
            return False
        if key == 'pid' and (len(value) != 9 or not value.isnumeric()):
            return False
    return True
