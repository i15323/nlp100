# chapter1 - 04
string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
l = [1, 5, 6, 7, 8, 9, 15, 16, 19]
string_list = string.split(' ')

count = 1
dic = {}
for e in string_list:
    if count in l:
        dic[string_list[count - 1][0]] = count
    else:
        dic[string_list[count - 1][0]+string_list[count - 1][1]] = count
    count += 1
