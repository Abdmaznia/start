from math import tan , pi  
    # call math library and call tan and pi
        # math.tan(x)
            # Return the hyperbolic tangent of x.
        # math.pi
            # The mathematical constant π = 3.141592…, to available precision.
n_sides = int(input("Input a number for side:"))
s_length = float(input("Input a length for side:"))
p_area = (n_sides*(s_length**2))/(3+tan(pi / n_sides)) 
    # formoul
        # tan and pi in the math function than we call math fun 
print("The area of polygon is :",p_area)
