def main():
    # First Step: Getting input of user
    time = input("time: ")
    # Second Step: Setting up convert(time) function
    c_time = convert(time)
    # Fifth Step: Defining when to output if breakfast, lunch or dinner time
    if c_time >= 7 and c_time <= 8:
        print("breakfast time")
    elif c_time >= 12 and c_time <= 13:
        print("lunch time")
    elif c_time >= 18 and c_time <= 19:
        print("dinner time")


def convert(time):
    # Third Step: hours & minutes = time with : split
    hours, minutes = time.split(":")
    # Fourth Step: Inputs shall returned to floating values & within the 60minute = 1hour range (time range)
    hours = float(hours) + (float(minutes) / 60)
    return hours

    


if __name__ == "__main__":
    main()