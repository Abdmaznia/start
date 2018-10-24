# Birth Date
byy = int(input("Enter birth Date(year):"))     # b birth Date
bmm = int(input("Enter birth Date(month):"))    # b birth Date  
bdd = int(input("Enter birth Date(day):"))      # b birth Date
# input current Date
cyy = int(input("Enter current Date (year)"))   # c current Date
cmm = int(input("Enter current Date (month)"))  # c current Date
cdd = int(input("Enter current Date (day)"))    # c current Date
if cdd < bdd: 
    cmm -= 1
    cdd += 30clear
    
day = cdd - bdd    
if cmm < bmm:
    cyy -= 1
    cmm += 12
month = cmm - bmm
year = cyy - byy
days = day + month * 30 + year * 36
hh = days * 24
mm = hh * 60
ss = mm * 60
print("old is:{0}/{1}/{2}",year,month,day)
print("Hour is (hh:mm:ss):{0}:{1}:{2}",hh,mm,ss)
