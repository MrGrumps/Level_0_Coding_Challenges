#Task 0.5
def area_of_triangle(x, y, z):
    #Using side lenghts 
    s = 1/2 * (x + y + z)
    
    #Heron's Formula
    area = (s * (s - x) * (s - y) * (s - z)) **0.5
    return(area)

area_of_triangle(3,4,5)