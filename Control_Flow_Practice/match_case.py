# Match Case simplifies checking for specific values
# It is similar to switch-case statements in other languages

day = "saturday"  #  assign one value at a time
match day:
    case "monday":
        print("Ugh, Mondays...")
    case "tuesday":
        print("Just another workday...")
    case "wednesday":
        print("Hump day!")
    case "thursday":
        print("Almost there...")
    case "friday":
        print("TGIF!")
    case "saturday" | "sunday":  # Match multiple values with pipe (|)
        print("Weekend vibes!")
    case _:
        print("Invalid day entered.")
