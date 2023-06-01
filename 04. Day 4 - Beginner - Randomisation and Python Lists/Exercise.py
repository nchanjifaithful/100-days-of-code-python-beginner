# ?? Don't change the code below ??
row1 = ["??","??","??"]
row2 = ["??","??","??"]
row3 = ["??","??","??"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# ?? Don't change the code above ??

#Write your code below this row ??
index_row, index_column = int(position[0]), int(position[1])
print(index_row)
map[index_column - 1][index_row - 1] = "XX"
 


#Write your code above this row ??

# ?? Don't change the code below ??
print(f"{row1}\n{row2}\n{row3}")
