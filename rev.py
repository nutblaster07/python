num=int(input("enter a no."))
chk=num
rev=0
while(num!=0):
    digit=num%10
    rev=rev*10+digit
    num//=10

if(chk==rev):
    print("palindrome")
else:
    print("not palindrome")
