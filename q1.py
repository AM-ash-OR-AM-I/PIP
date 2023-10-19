globalVar = 10
def test():
    localVar = 20
    print("globalVar in test():", globalVar)
    print("localVar in test():", localVar)
test()
print("globalVar in main:", globalVar)
print("localVar in main:", localVar)

#Error localVar not defined in main