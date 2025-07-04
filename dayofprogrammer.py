def day_of_programmer(year):
    if year ==1918:
        return f"26.09.{year}"
    is_leap_year = False
    
    if year <= 1917:
        is_sleap_year = year % 4 == 0
    else:
        is_sleap_year = year % 400 == 0 or (year % 4 ==0 and year %100
 != 0)

    return f"12.09.{year}"if is_sleap_year else f"13.09.{year}"









