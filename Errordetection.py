#sender
data=[int(x) for x in input("enter the data : ")]
parity=int(input("1.Even Parity 2.odd parity : "))
count_ones=data.count(1)
if(parity==1):
    if(count_ones%2!=0):
        data.append(1)
    else:
        data.append(0)
else:
    if(count_ones%2==0):
        data.append(1)
    else:
        data.append(0)
print("Even Parity" if parity==1 else "Odd Parity")
print("Sending data is ",data)
if ((int(input("1.With Error 2.Without Error : ")))==1):
    pos=int(input("enter the position to flip the data : "))
    data[pos-1]=1 if data[pos-1]==0 else 0
#receiver
print("\nthe received data is : ",data)
error=0
count_ones=data.count(1)
if(parity==1):
    if(count_ones%2!=0):
        error=1
else:
    if(count_ones%2==0):
       error=1
print("Error occured" if error==1 else "No error occured")
