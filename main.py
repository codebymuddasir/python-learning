sc = (input("Enter the message:"))
words = sc.split(" ")

coding = input("1 for coding or 0 for decoding")
coding = True if  (coding=="1") else False
print(coding)
if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            m1 = "asd"
            m2 = "fgh"
            scnew = m1= word[1:] + word[0] + m2
            nwords.append(scnew)
        else:
            nwords.append(word[::-1])
            print(" ".join(nwords))



            

            
