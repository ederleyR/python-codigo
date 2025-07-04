
def dayOfProgrammer(year):
    year = int(input("ingrese año: "))
    if year < 1918:
  
        if year % 4 == 0:
            
            february_days = 29
        else:
            february_days = 28
    elif year == 1918:
      
        february_days = 15
    else:
       
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            
            february_days = 29
        else:
            february_days = 28

   
    days = [31, february_days, 31, 30, 31, 30, 31, 31]
    total_days = sum(days)


    day = 256 - total_days
    month = 9  


    if day < 10:
        day_str = f"0{day}"
    else:
        day_str = str(day)

    if month < 10:
        month_str = f"0{month}"
    else:
        month_str = str(month)

    return f"{day_str}.{month_str}.{year}"


print(dayOfProgrammer(2017))  
print(dayOfProgrammer(2016))  
print(dayOfProgrammer(1918))  