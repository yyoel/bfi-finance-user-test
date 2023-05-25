"""
----------- Exercise 1 -----------
Q: Apa output dari program di bawah ini?
A: o
"""
nama = ['Chris', 'Jack', 'John', 'Daman']
print(nama[-2][-3])


"""
----------- Exercise 2 -----------
Q: Apa nilai akhir dari list_0, list_1?
A: 
list_0: ['Amir', 'Bear', 'Charlton', 'Daman', 1, 2, 3, 4]
list_1: ['Amir', 'Bear', 'Charlton', 'Daman', [1, 2, 3, 4]]
"""
list_0 = ['Amir', 'Bear', 'Charlton', 'Daman']
list_1 = ['Amir', 'Bear', 'Charlton', 'Daman']

list_2 = [1,2,3,4]

list_0.extend(list_2)
list_1.append(list_2)

"""
----------- Exercise 3 -----------
Q: Apa nilai akhir dari list_1, list_2, list_3?
A: 
list_1: ['Alice', 'Bear', 'Charlton', 'Kevin']
list_2: ['Alice', 'Bear', 'Charlton', 'Kevin']
list_3: ['Amir', 'Bob', 'Charlton', 'Daman']
"""
list_1 = ['Amir', 'Bear', 'Charlton', 'Daman']
list_2 = list_1
list_3 = list_1[:]

list_1[0] = 'Alice'
list_2[3] = 'Kevin'
list_3[1] = 'Bob'
print(list_1, list_2, list_3)