cost = input()
customers = input()

if customers >= 8:
    print('A 20% tip is automatically added to parties of 8 or more. Your bill is $', cost * 1.2)
else:
    print('Your tip options are:\n15%: $',cost * 1.15,'\n20%: $',cost * 1.2,'\n25%: $',cost * 1.25)
