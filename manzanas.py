
def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    count_apples = sum(1 for apple in apples if s <= a + apple <= t)
    
    count_oranges = sum(1 for orange in oranges if s <= b + orange <= t)
    
    print(count_apples)
    print(count_oranges)

s = 7  
t = 11  
a = 5  
b = 15  
apples = [-2, 2, 1]  
oranges = [5, -6]  

countApplesAndOranges(s, t, a, b, apples, oranges)
