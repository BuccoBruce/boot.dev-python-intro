def join_strings(strings: list[str]) -> str:
    new_string = ""
    if len(strings) == 0 or not strings:
        return ""
    else:
        for string in strings:
            if string == strings[-1]:
                new_string += string
            else:
                new_string += (string + ",")
        return new_string