def duplikat(huruf):
    temp = []
    list_huruf = list(huruf)
    for abjad in list_huruf:
        if abjad in temp:
            continue
        else:
            temp.append(abjad)
    return "".join(temp)
print(duplikat("ccbabacc"))