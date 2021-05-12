def palindrome_counter(string):
    counter = 0
    if len(string) == 0:
        return counter
    for n in range(1, len(string)+1):
        for i in range(len(string)):
            fwd = string[i:n+i:]
            if fwd == fwd[::-1]:
                counter += 1
            if n+i == len(string):
                break
    print("A sztringben található palindrómok száma:")
    return counter
word = input("Adjon meg egy sztringet: ")
print(palindrome_counter(word))