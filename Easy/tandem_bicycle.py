# Tandem bicycle problem 

def tandemBicycle(blue_shirts, red_shirts, fastest):
    
    #(1) Sort the arrays according fastest is true or not
    blue_shirts.sort()
    if fastest: 
        red_shirts.sort(reverse = True)
    else: 
        red_shirts.sort()
    
    desiredSpeed = 0
    for id in range(0, len(blue_shirts)): 
        desiredSpeed += max(blue_shirts[id], red_shirts[id])
    
    return desiredSpeed


red_shirt_speeds = [5, 5, 3, 9, 2]
blue_shirt_speeds = [3, 6, 7, 2, 1]
fastest = False

desiredSpeed = tandemBicycle(blue_shirt_speeds, red_shirt_speeds, fastest)
print(f"Desired speed: {desiredSpeed}\n")