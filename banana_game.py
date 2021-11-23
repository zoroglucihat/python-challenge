def banana_game(string):

    david = 0
    roger = 0
    strlen = len(string)

    for i in range(strlen):
        for vowc in "AEIOU":
            if string[i].find(vowc) >= 0:
                roger = roger + strlen - i

    david = int(strlen*(strlen+1)/2) - roger

    if david > roger:
        print("david " + str(david))
    if roger > david:
        print("roger " + str(roger))
    if roger == david:
        print("Draw")

    return 0



if __name__ == '__main__':
    s = raw_input()
    banana_game(s)

