def NAND(x, y):
    if x==1 and y==1:
        return 0
    else:
        return 1

def XOR(x, y):
    nand=NAND(x, y)
    return NAND(NAND(x, nand), NAND(y, nand))

def NOT(x):
    if x==0:
        return 1
    else:
        return 0

def AND(x, y):
    if x==1 and y==1:
        return 1
    else:
        return 0

def OR(x, y):
    if x==0 and y==0:
        return 0
    else:
        return 1

def truth_table(operation):
    print("\ntruth table of:", operation)
    if operation=="NOT":
        print("A | RESULT")
        print("__|________")
        for a in [0, 1]:
            print(f"{a} |   {NOT(a)}")
    else:
        print("A | B | RESULT")
        print("__|___|_________")
        for a in [0, 1]:
            for b in [0, 1]:
                if operation=="AND":
                    print(f"{a} | {b} |   {AND(a, b)}")
                elif operation=="OR":
                    print(f"{a} | {b} |   {OR(a, b)}")
                elif operation=="NAND":
                    print(f"{a} | {b} |   {NAND(a, b)}")
                elif operation=="XOR":
                    print(f"{a} | {b} |   {XOR(a, b)}")

def menu():
    print("menu: \n1.NOT \n2.OR \n3.AND \n4.NAND \n5.XOR \n6.QUIT")
    c=int(input("enter your choice: "))

    if c==1:
        a=int(input("Enter value (0 or 1): "))
        print(f"NOT({a})={NOT(a)}")
        truth_table("NOT")
        
    elif c==2:
        a=int(input("Enter value for A (0 or 1): "))
        b=int(input("Enter value for B (0 or 1): "))
        print(f"OR({a}, {b})={OR(a, b)}")
        truth_table("OR")
        
    elif c==3:  
        a=int(input("Enter value for A (0 or 1): "))
        b=int(input("Enter value for B (0 or 1): "))
        print(f"AND({a}, {b})={AND(a, b)}")
        truth_table("AND")
        
    elif c==4: 
        a=int(input("Enter value for A (0 or 1): "))
        b=int(input("Enter value for B (0 or 1): "))
        print(f"NAND({a}, {b})={NAND(a, b)}")
        truth_table("NAND")
        
    elif c==5:
        a=int(input("Enter value for A (0 or 1): "))
        b=int(input("Enter value for B (0 or 1): "))
        print(f"XOR({a}, {b})={XOR(a, b)}")
        truth_table("XOR")
        
    elif c==6:
        print("quiting")
        exit()
    else:  # Invalid Input
        print("invalid input")
        menu()

menu()
