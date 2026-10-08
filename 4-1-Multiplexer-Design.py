print("===== 4:1 Multiplexer =====")

I0 = int(input("Enter Input I0: "))
I1 = int(input("Enter Input I1: "))
I2 = int(input("Enter Input I2: "))
I3 = int(input("Enter Input I3: "))

S1 = int(input("Enter Select S1: "))
S0 = int(input("Enter Select S0: "))

if S1 == 0 and S0 == 0:
    Y = I0
elif S1 == 0 and S0 == 1:
    Y = I1
elif S1 == 1 and S0 == 0:
    Y = I2
elif S1 == 1 and S0 == 1:
    Y = I3
else:
    print("Invalid input!")
    exit()

print("Output Y =", Y)
