""" ### grade score that determine A, B, C, D, AND F
def grade(score):
    if score >=80:
        return "A"
    elif score >= 60:
        return "B"
    elif score>=50:
        print("C")
    elif score >= 40:
        return "D"
    else:
        return "F"
    
print(grade(90))
print(grade(40))
print(grade(67))
print(grade(88))
print(grade(21))
print(grade(100))
print(grade(55))


def is_leap_year(year):
    if year %400==0:
        return True
    elif year %100==0:
        return False
    elif year%4==0:
        return True
    else:
        return "JUST A YEAR"
    
print(is_leap_year(2020))
print(is_leap_year(1900))
print(is_leap_year(2021))
print(is_leap_year(2024))
 """
 
def login(username, password):
     if username == "" and password == "":
         return "Error: Username and password are empty"
     elif username == "":
         return "Error: Username is empty"
     elif password == "":
         return "Error: Password is empty"
     else:
         return "Login Successful"

print(login("jacky",""))