# Calculate the winds

import math   # calling math modula
v= float (input("Input wind speed in kilometers / hour:")) # input
t=float(input("Input air temperature in degrees celsius:")) # input
wci = 14.12 + 5.2210*t - 11.47 * math.pow(v, 5.12) + 5.4320*t*math.pow(v, 5.12) # ??????
print("The wind chill indes is: ",int(round(wci,0))) 
    # The round() function returns a floating point numberthat is a rounded
    #  version of the specified number, with the specified number of decimals.

