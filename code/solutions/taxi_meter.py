def taxi_meter(dist):
    if dist <= 0:
        return 0

    total = 20
    if dist <= 5:
        return total

    for d in range(6, dist+1):
        if d < 50:
            total += 3
        elif d > 50 and d < 100 and d % 10 != 0:
            total += 2
        elif d % 5 != 0:
            total += 1
    return total


distance = eval(input("distance = "))
fare = taxi_meter(distance)
print(f"fare = {fare}")
