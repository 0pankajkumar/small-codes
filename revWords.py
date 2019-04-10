# My answer for Quasix

stri = "apple banana orange"
# rev = "elppa ananab egnaro"

# str = "abc def"
# rev = "cba fed"

def reverse_words(stri):
    rev = ""
    word = stri.split(" ")
    for i in word:  #going into individual word
        temp2 = []
        temp = list(i) #split a single word in alphabets
        print(temp)
        for j in temp: #going into each alphabet
            m = temp.pop()
            print(m)
            temp2.append(m) #add popped
        print(temp2)
        temp2 = ''.join(temp2)

        #rev = ' '.join(temp2)
        rev += str(temp2)
        rev += " "

    return (rev)
    
print(reverse_words(stri))

    # str + 
    