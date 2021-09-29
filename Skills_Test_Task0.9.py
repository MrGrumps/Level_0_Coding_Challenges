#Task 0.9
def vowel_check(x):
    vowels = ['a','e','i','o','u']
    vowel_list = []
    x = x.lower()
    for char in x:
        if char in vowels:
            vowel_list.append(char)
    print("Vowels: " + ", ".join(set(vowel_list)))

vowel_check("Umuzi")