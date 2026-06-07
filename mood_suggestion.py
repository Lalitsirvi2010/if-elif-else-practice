mood = input("Enter your mood (happy, sad, angry, tired, focused, bored): ").lower()
category = input("Do you want music or activity?: ").lower()

if category == 'music':
    if mood == "happy":
        print("Play dance/pop music")
    elif mood == "sad":
        print("Play slow/soft music")
    elif mood == "angry":
        print("Play heavy/rock music")
    elif mood == "tired":
        print("Play calm/relaxing music")
    elif mood == "focused":
        print("Play instrumental music")
    elif mood == "bored":
        print("Play upbeat/energetic music")
    else:
        print("Invalid mood entered.")
elif category == 'activity':
    if mood == "happy":
        print("Go for a walk or dance")
    elif mood == "sad":
        print("Watch a comedy or talk to a friend")
    elif mood == "angry":
        print("Try deep breathing or physical exercise")
    elif mood == "tired":
        print("Take a nap or do some light stretching")
    elif mood == "focused":
        print("Work on a project or read a book")
    elif mood == "bored":
        print("Try a new hobby or explore a new place")
    else:
        print("Invalid mood entered.")
else:
    print("Invalid category entered.")
