"""
Acquired from: https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1256/#/final-prep

This problem is like the lists problem we saw on the midterm, but made better with lists of lists!
Say you're given a list of lists, where each inner list contains the average temperatures from all 12 months of a year as floats.
We want to find the average temperature for each year, and form a list of these annual averages.

Implement the function annual_temps(nested) that takes in a nested list of monthly temperature lists,
and returns a (non-nested) list of the average temperatures from each year.

"""
month_temperature=[[1,2,3,4,5,6,7,8,9,10,11,12],[3,0,0,0,0,0,0,0,0,0,0,0],[12,0,0,0,0,0,0,0,0,0,0,0]]

def annual_temps(temp_list):
    out=[]
    for i in range(len(temp_list)):
        total = 0
        for j in range(len(temp_list[i])):
            total+=temp_list[i][j]
        out.append(total/len(temp_list[i]))
    return out
print(annual_temps(month_temperature))

