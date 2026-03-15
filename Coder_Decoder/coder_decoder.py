try:
    import random
    import string
    all_letters = (string.ascii_letters + string.digits + string.punctuation)
    l= list(all_letters)
    menu = 0
    while menu == 0:
        want= input("u wanna code or decode? (c/d)(type nothing to leave) :")
        if want.lower() == "c" or want.lower() == "code":
            cloop = 0
            while cloop == 0:
                text = input("enter the text you wanna code :")
                if len(text) == 2:
                    print(text[-1]+text[0])
                elif len(text) == 1:
                    print(text)
                elif len(text) == 0:
                    print("you entered nothing")
                else:
                    new_text = text[1:]+text[0]
                    k= random.choices(l,k=3)
                    k= "".join(k)
                    y= random.choices(l,k=3)
                    y= "".join(y)
                    print(k+new_text+y)
                ask= input("do u wanna code another text(write code) or go back to menu(write menu)? :")
                if ask.lower() == "code":
                    cloop = 0
                else:
                    cloop = 1
                    menu=0
        elif want.lower() == "d" or want.lower() == "decode":
            dloop = 0
            while dloop == 0:
                text = input("enter the text you wanna decode :")
                if len(text) == 2:
                    print(text[-1]+text[0])
                elif len(text) == 1:
                    print(text)
                elif len(text) == 0:
                    print("you entered nothing")
                else:
                    new_text = text[3:-3]
                    new_text = new_text[-1]+new_text[:-1]
                    print(new_text)
                ask= input("do u wanna decode another text(write decode) or go back to menu(write menu)? :")
                if ask.lower() == "decode":
                    dloop = 0
                else:
                    dloop = 1
                    menu=0
        else:
            menu = 1
            print("good bye :)")
            break
except:
    print("an error occurred")