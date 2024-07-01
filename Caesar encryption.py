#Cessaer Encryption

alph = { 'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, }
letter = { 1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z', }



print("\n\nCaesar encryption is a type of encryption were you move a letter X \namount of times to the left in the Alphabet. Exmaple, encrypting ' Dog ' \nby moving it 5 letter to the left which would make it ' YJB '. ")
print("\n\n  Try out your self\n\n")

word_input = input("Enter a word: ")
word = word_input.upper()

shift = int(input("Enter the ammount of steps you want to shift: "))

encrypted = ""

for x in word:
    no = alph[x]
    no = no - shift
    while no <= 0:
        no += 26
    encrypted += letter[no]

print("\nEncrypted Output: " + encrypted)
print(f"\nEach letter in '{word_input}' was moved {str(shift)} letters to the left which makes it '{encrypted}'!\n\n")
input("Press Enter to continue to Decyrption")
print("\nTo deycrpt a Caesar encryption message you must do the revses process,\ninstead moving the letters X letters to the left you move them X letters to the right.\n")
input()
print(f" Thus decrypting '{encrypted}' by moving it {str(shift)} letters to the right, you will get '{word_input}'" )
input()
print("\n That's all to know about Caesar encryption. \n\n               THANK YOU!")
input()




