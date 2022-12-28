def is_playing_banjo(name):
    upper_case=name.upper()
    if upper_case.startswith("R"):
        print(name+" "+"plays banjo")
    else:
        print(name+" "+"does not play banjo")
is_playing_banjo("Ramkumar")        