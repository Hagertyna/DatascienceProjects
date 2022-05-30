# Get the address in RAM
x = 5

print("id(5) =", id(5))
print("id(x) =", id(x))
x = x+2
id(x)

x = 10

def outer():
    print(x) #10
    def inner():
        x = 5
        print(x) #5
    inner()
#outer code prints 
# 10 5
outer()
