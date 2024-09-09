def pangram(sentance):
    letters = "abcdefghijklmnopqrstuvwxyz"
    for ch in letters:
        if ch not in sentance.lower() :
            return False
    return True

helooooooooooooooooooooooooooooooooooooooo = input("Helooooooooooooooooooooooooooooooooooooooo, Please Enter A sentance Please :) ")
if pangram(helooooooooooooooooooooooooooooooooooooooo):
    print("Helooooooooooooooooooooooooooooooooooooooo, It's A Pangram! :) )")
else:
    print("Helooooooooooooooooooooooooooooooooooooooo, It's Not A Pangram! :( )")
