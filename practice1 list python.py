marks = [99, 87, 90, 65, 77, 56, 84, 96, 34, 23, 49, 95]
marks.sort(reverse=True) 
print(marks[2])



list_a = [56, 89, 234, 90, 56, 77]
list_b = [90, 56, 21, 96, 45, 89]
unique_values=set(list_a).union (set(list_b))
print(unique_values)




values = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
values[2][2].append(7000)
print(values)
values = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
values[2][2].insert(values[2][2].index(6000) + 1, 7000)


list_a = [56, 89, 234, 90, 56, 77]
list_b = [90, 56, 21, 96, 45, 89]
unique=set(list_a).difference(set(list_b))
print(unique)


names=["karna","arjun","bhima","yudhisthira","nakula","sahadev"]
names.sort()
print(names)


sub1={"math","physics","chemisty","history","politalcal-science"}
sub2={"botany","physics","zoology","history","politalcal-science"}
favorite=set(sub1).intersection(set(sub2))
print(favorite)


flower=["lily","champa","sunflower","rose","marigold"]
flower.sort()
print(flower)
fruits=["graps","blackberry","lichu","strobery","mango"]
fruits.sort()
print(fruits)
combines=set(flower).union(set(fruits))
print(combines)



marks = [99, 87, 90, 65, 77, 56, 84, 96, 34, 23, 49, 95]
marks.sort()
marks[::-1]
print(marks)

tup=("apple",90,67+88j,[5,4,3],{"a","b"})
tup[3].remove(3)
print(tup)