#Use the walrus operator to read input until the user enters "quit". Print each input as it is entered

while((text:=input("Enter your string:")))!="quit":
    print(f"You Entered {text}")
    # if a=="quit":
    #     break
    # else:
    #     print(a)    