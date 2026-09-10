#Write a python program to detect whether a comment is spam or not .A Comment should be tretead as spam if it contains any of these keywords 
# "make a lot of money","buynow""subcribe this","click this"
comment = input("Enter the Comment ")
if "make a lot of money" in comment or "buy now" in comment or "subscribe this" in comment == "click this":
    print("Comment is spam")
else:
    print("Comment is not spam")