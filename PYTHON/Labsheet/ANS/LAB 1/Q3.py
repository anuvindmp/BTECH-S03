#shipping
cost = 0

weight = float(input("Enter the weight of your package : "))
distance = float(input("Enter the distance the package need to travel : "))

if weight > 10:
    cost+=20
elif weight > 2:
    cost+=10
else:
    cost += 5

if distance > 500:
    cost+=10
elif distance > 100:
    cost+=5
print("Total cost : ", cost)