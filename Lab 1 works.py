#python problem 1

km = int(input("Insert Traveling Distance: "))
total_fare = 0

if(km <= 12):
  total_fare = 100
elif(km > 12 and km <= 16):
  total_fare = 100 + (km-12)*8
elif(km > 16 and km <= 20):
  total_fare = 100 + (4*8) + (km-16)*6
elif(km > 20):
  total_fare = 100 + (4*8) + (4*6) + (km-20)*5

print("Total Fare is : "+str(total_fare))

#25 - 181
#5 - 100
#13 - 108
#15 - 124
#17 - 138
#30 - 206

#problem 2

mass_earth = 5.972 * (10**24)
mass_moon =  7.35 * (10**22)
radius_earth = 6361 * 1000
radius_moon = 1737 * 1000
Newton_G = 6.67408/(10**11)

gravity_earth = Newton_G * mass_earth / radius_earth**2
gravity_moon = Newton_G * mass_moon / radius_moon**2

print("Gravity of Earth is : "+str(gravity_earth))
print("Gravity of Moon is : "+str(gravity_moon))

# Gravity of Earth is : 9.850548553554306
# Gravity of Moon is : 1.6258448896962683


#problem 3

n = int(input("Insert value on n : "))
r = -1/3
sum = (1-r**(n+1))/(1-r)

print("Sum of series for first "+str(n+1)+" is : "+ str(sum))

# Insert value on n : 5
# Sum of series for first 6 is : 0.7489711934156379
