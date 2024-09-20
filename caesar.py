# caesar cipher encryption while-loops
def  main():
    s = input("Enter your message: ").lower()
    translation_degree = int(input("Enter the translation degree: "))
    alpha = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    i = 0
    while(i < len(s)):
        char = s[i]
        if char in alpha:
            ind1 = alpha.index(char)
            ind2 = (ind1 + translation_degree) % 26
            output = alpha[ind2]
        else:
            output += char
        i += 1
        print(output, end="")



# caesar cipher encryption for-loops
# def main():
#     s = input("Enter your message: ").lower()
#     translation_degree = int(input("Enter the translation degree: "))
#     alpha = "abcdefghijklmnopqrstuvwxyz"
#     output = ""
    
#     for char in s:
#         if char in alpha:
#             ind1 = alpha.index(char)
#             ind2 = (ind1 + translation_degree) % 26
#             output += alpha[ind2]
#         else:
#             output += char

#     print(output)


if __name__ == "__main__":
    main()