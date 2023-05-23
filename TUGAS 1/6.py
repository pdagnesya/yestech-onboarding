def convert_to_24h(time):
    if time[-2:] == "AM" and time[:2] == "12":
        return "00" + time[2:-2]
    elif time[-2:] == "AM":
        return time[:-2]
    elif time[-2:] == "PM" and time[:2] == "12":
        return time[:-2]
    else:
        hour = int(time[:2]) + 12
        return str(hour) + time[2:-2]

print(convert_to_24h("12:05:00AM"))
print(convert_to_24h("12:05:00PM"))
print(convert_to_24h("03:05:00AM"))
print(convert_to_24h("03:05:00PM"))