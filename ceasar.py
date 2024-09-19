def  main():
    s = input("Enter your message: ")
    translation_degree = int(input("Enter the translation degree: "))
    alpha = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    i = 0
    while(i < len(s)):
        ind1 = alpha.index(s[i])
        ind2 = (ind1 + translation_degree) % 26 + 1
        i += 1
        x = alpha[ind2]
        output += x
    print(output)
if __name__ == "__main__":
    main()