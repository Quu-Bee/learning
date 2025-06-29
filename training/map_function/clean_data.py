dirty_points = [",", ".", ";", ":", "!", "?", " ", "/"]
dirty_data = [
    "  ,,, b.im_b.im ",
    "BAM_B??AM  ??  ",
    " .....B!!!!!yM_b???!Ym   ....  . ",
]
# for data in dirty_data:
#    for char in data:
#        if char in dirty_points:
#            data =  data.replace(char, "")
# print(dirty_data)
#####################################################
# print(dirty_data)
# clean_data = list(map(lambda data: data.strip().lower(), dirty_data))
# clean_data_upper = list(map(lambda data: data.replace(data[0], data[0].upper()), clean_data))
# print(clean_data_upper)

def clean_string(s):
    cleaned = "".join(char for char in s if char not in dirty_points).lower()
    return cleaned

cleaned_data = [clean_string(s) for s in dirty_data]
cleaned_data_upper = list(
    map(lambda data: data.replace(data[0], data[0].upper()), cleaned_data)
)

#cleaned_data_upper = list(map(lambda data: data[0].upper() + data[1:], cleaned_data))
# cleaned_data_upper = [data[0].upper() + data[1:] for data in cleaned_data]
print(cleaned_data_upper)
