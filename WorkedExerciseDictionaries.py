fname=input("Enter File: ")
in len(fname) < 1: fname= 'Clown.rtf'
hand=open(fname)

di=dict()
for lin in hand:
    lin=lin.rstrip()
    print(lin)
    wds=lin.split
    print(wds)

    for w in wds:
        if w in di:
            di[w]=di[w]+1
        else:
            di[w]=1
            print('**NEW**')
        print(w, di[w])
