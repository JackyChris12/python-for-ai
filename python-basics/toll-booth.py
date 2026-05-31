# Vehicle types: "car", "truck", "motorcycle", "bus"
# Base rates: car=$2.50, truck=$4.00, motorcycle=$1.50, bus=$3.50
# Axle surcharge: truck +$1.00 per axle over 2, bus +$0.75 per axle over 2
# Multipliers (in order): transponder ×0.85, peak hour ×1.40, weekend ×0.75
# Peak hours: 6-9 inclusive OR 17-19 inclusive
# Validation order: vehicle → axles → hour → transponder → weekend
# Round final to 2 decimals, return "Toll: $X.XX"

def toll_booth(vehicle_type, axles, has_transponder,hour, is_weekend):
    valid_vehicles = ("car", "truck", "motorcycle", "bus")
    if vehicle_type not in valid_vehicles:
        return "Error: Invalid vehicle type."
    if type(axles) is not int or axles <2:
        return "Error: Invalid axle count."
    if type(hour) is not int or not( 0<=hour<=23):
        return "Error: Invalid hour."
    
    if type(has_transponder) is not bool:
        return "Error: Transponder must be True or False."
    if type(is_weekend) is not bool:
        return "Error: Weekend flag must be True or False."
    # Calculations
    if vehicle_type == "car":
        total = 2.50
    elif vehicle_type == "truck":
        total = 4.00
    elif vehicle_type == "motorcycle":
        total = 1.50
    elif vehicle_type == "bus":
        total = 3.50
    
    #axles
    if vehicle_type == "truck" and axles >2:
        total += (axles - 2) * 1.00
    
    elif vehicle_type == "bus" and axles >2:
        total+= (axles -2) *0.75
    
    if has_transponder is True:
        total *= 0.85    
    if (6 <= hour <= 9) or (17 <= hour <= 19):
        total *= 1.40
    
    if is_weekend is True:
        total *= 0.75
    
    total = round(total, 2)
    return f"Toll: ${total:.2f}"

    
    
    
print(toll_booth("car", 2, True, 8, False))      
print(toll_booth("truck", 4, False, 12, True))  
print(toll_booth("bus", 2, False, 18, False))    
print(toll_booth("bike", 2, True, 10, False))   
print(toll_booth("truck", 1.5, True, 10, False)) 
print(toll_booth("car", 2, True, 25, False))     
print(toll_booth("car", 2, "yes", 10, False))    
print(toll_booth("car", 2, True, 10, "no"))     


