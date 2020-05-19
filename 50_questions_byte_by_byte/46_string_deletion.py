'''
Question​ : Given a string and a dictionary HashSet, write a function to determine the
minimum number of characters to delete to make a word.
'''

def stringDeletion(sou, dictionary):
    if sou in dictionary:
        return 0
    ans = []
    for i in range(len(sou)):
        t = sou[:i] + sou[i+1:]
        t2 = stringDeletion(t, dictionary) + 1
        ans.append(t2)

    if len(ans) == 0:
    	return 9999
    else:
    	return min(ans)


# ab
# bc
# ac 



dictionary = ["a", "aa", "aaa"]
ans = stringDeletion("abc", dictionary)
print(ans)
