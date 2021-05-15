def reverseWord(s):

    #your code here

    i = 0

    j =len(s)-1

    a = list(s)

    while (i<j):

        a[i], a[j] = a[j], a[i]

        i+=1

        j-=1

    

    return ''.join(a)


print(reverseWord("Geeks") )

