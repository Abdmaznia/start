#The complex() method returns a complex number 
# when real and imaginary parts are provided, or it 
# converts a string to a complex number.

a = int (input("Enter real part:"))
b = int (input("Enter image part:"))
complex1 = complex(a,b)
    # 
print(complex1)


z= complex(2,3)
print(z)
z1 = complex(1)
print(z1)
z2 = complex()
print(z2)
z3 = complex("5-9j")
print(z3) 

a = 2+3j
print("a=",a)
print("type a is:",type(a))
b = -2j
print("b=",b)
print("type a is :",type(b))
 
c = 0j
print("c=",c)
print("type of c:",type(c))

d = (1+2j) + (3+2j)
print(d) # (4+4j)

str = complex("4")
print(str) # (4+0j)

A = complex (1 , 1)
print(A)  #  (1+1j)

c = complex (1.5,-2.1)
print(c)  # (1.5-2.1j)

c= complex(0xF)   # hexadecimal
print(c)  #(15+0j)

c= complex(0b1010, -1) # binary
print(c) # (10-1j)

x = 1.0
y = 2.0
z = complex(x,y)
print(z)  # (1+2j)