#x = str(input("Provide the text: "))

def method1(text):
    ListOfWords = text.split(' ')
    for chr in ListOfWords[-1]:
        i = text.count(chr)
        print(chr, i)
            

text = "hasta la vista"
subtext = 'vista'

for i in subtext:
    letter_counts = {}
    print(i)
    if i in letter_counts:
        letter_counts[i] += 1
    else:
        letter_counts[i] = 1

print(letter_counts)
