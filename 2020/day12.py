# day 12: rain risk
def rain_risk_one():
    directions = {'north': (0, 1), 'east': (1, 0), 'south': (0, -1), 'west': (-1, 0)}
    compass = ['north', 'east', 'south', 'west']
    facing = 1
    x, y, = 0, 0

    input_file = open('input/rain_risk', 'r')
    for line in input_file:
        if line[0] == 'N': y += int(line[1:])
        elif line[0] == 'S': y -= int(line[1:])
        elif line[0] == 'E': x += int(line[1:])
        elif line[0] == 'W': x -= int(line[1:])
        elif line[0] == 'L': facing = int(facing + 4 - int(line[1:]) / 90) % 4
        elif line[0] == 'R': facing = int(facing + int(line[1:]) / 90) % 4
        elif line[0] == 'F':
            cords = directions.get(compass[facing])
            x += cords[0] * int(line[1:])
            y += cords[1] * int(line[1:])
    print(abs(x) + abs(y))

def rain_risk_two():
    waypoint = [10, 1]
    x, y, = 0, 0

    input_file = open('input/rain_risk', 'r')
    for line in input_file:
        if line[0] == 'N': waypoint[1] += int(line[1:])
        elif line[0] == 'S': waypoint[1] -= int(line[1:])
        elif line[0] == 'E': waypoint[0] += int(line[1:])
        elif line[0] == 'W': waypoint[0] -= int(line[1:])
        elif line[0] == 'F':
            x += waypoint[0] * int(line[1:])
            y += waypoint[1] * int(line[1:])
        # either L or R commands left, so we turn waypoint
        elif int(line[1:]) == 180:
            waypoint[0] = waypoint[0] * -1
            waypoint[1] = waypoint[1] * -1
        else:
            temp = waypoint[0]
            waypoint[0] = waypoint[1]
            waypoint[1] = temp
            if line.rstrip() == 'L270' or line.rstrip() == 'R90':
                waypoint[1] *= -1
            else: waypoint[0] *= -1

    print(abs(x) + abs(y))
