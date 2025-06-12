you = int(input("Choice/Right:1, Left:others"))
com = int(random() * 2 + 1)
if you == 1:
    print("you:Right<BR>")
    if com == 1:
        print("com:Right<BR>")
    else:
        print("com:Left<BR>")
else:
    print("you:Left<BR>")
    if com == 1:
        print("com:Right<BR>")
    else:
        print("com:Left<BR>")