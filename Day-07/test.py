import sys
type= sys.argv[1]

if type=="t2.micro":
    print("charges are 2 dollar/tb data transfer")
elif type=="t2.medium":
    print("charges are 8 dollar/tb data transfer")
elif type=="t2.xlarge":
    print("charges are 10 dollar/tb data transfer")
else:
    print("wrong type of instance provided")