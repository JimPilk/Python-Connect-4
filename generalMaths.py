def convert_to_number(boolean):
    if boolean:
        return 0
    return 1

def convert_to_boolean(number):
    if number == 0:
        return True
    return False

def get_wins(width, height):
    area = width * height
    wins = []
    for i in range(area):

        if i // width >= 3:
            #veritcal
            temp = []
            for j in range(4):
                temp.append(i - width * j)
            wins.append(temp)

            if i % width >= 3:
                #top left
                temp = []
                for j in range(4):
                    temp.append(i - width * j - j)
                wins.append(temp)

            if i % width <= width - 4:
                #top right
                temp = []
                for j in range(4):
                    temp.append(i - width * j + j)
                wins.append(temp)

        if i % width <= width - 4:
            #right
            temp = []
            for j in range(4):
                temp.append(i + j)
            wins.append(temp)

    return wins
