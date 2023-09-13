m1= int(input("marks1 "))
m2= int(input("marks2 "))
m3= int(input("marks3 "))
minin = min(m1,m2,m3)
sum2 = m1 + m2 + m3 - minin
avg = sum2 / 2
print(avg)