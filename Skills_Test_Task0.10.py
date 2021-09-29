#Task 0.10
def compare_strings(string1,string2):
    common_list = []
    for l in string1.lower():
        for m in string2.lower():
            if l == m:
                common_list.append(l)
    print("Common Letters: " + ", ".join(set(common_list)))

compare_strings("house","computers")