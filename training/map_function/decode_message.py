secret_message = [83, 30, 97, 110, 121, 97, 32, 74, 20, 117, 114, 97, 118, 108]
clean_char_list = []
secret_letter = ""
char_list = list(map(chr, secret_message))
for i in range(len(char_list)):
    if char_list[i].isalpha() or char_list[i] == " ":
        clean_char_list.append(char_list[i])

#for char in char_list:
#   if not char.isalpha or char != " ":
#        char_list.remove(char)
print(char_list)
print(clean_char_list)
secret_letter = "".join(clean_char_list)
print(secret_letter)