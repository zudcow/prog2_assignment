import string
try:
    f_in = open('input.txt', 'r')
except FileNotFoundError:
    print('A bemeneti fájl nem található')

mely = ('a', 'á', 'o', 'ó', 'u', 'ú')
magas = ('e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű')
def vowelscale(input_file):
    words = ()
    for line in input_file:
        temp = ''
        line = line.rstrip()
        for ch in line:
            if ch not in string.punctuation:
                temp += ch.lower()
        words = temp.split(' ')
        for word in words:
            if is_mely(word) and is_magas(word):
                out_vegyes.write(word+'\n')
            elif is_magas(word):
                out_magas.write(word + '\n')
            else:
                out_mely.write(word + '\n')

def is_mely(word):
    for ch in word:
        if ch in mely:
            return True
    return False

def is_magas(word):
    for ch in word:
        if ch in magas:
            return True
    return False

out_mely = open('mely.txt', 'w')
out_magas = open('magas.txt', 'w')
out_vegyes = open('vegyes.txt', 'w')

vowelscale(f_in)

f_in.close()
out_mely.close()
out_magas.close()
out_vegyes.close()