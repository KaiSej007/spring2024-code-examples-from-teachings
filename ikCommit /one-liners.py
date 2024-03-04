cap = [chr(i) for i in range(65, 91)]
print(cap)


cap1 = [chr(i) for i in range(65, 91) if i not in (70, 75, 80, 85)]
print(cap1)


cap2 = [chr(i) for i in range(ord('A'), ord('Z')+1,) if i not in (ord('F'), ord('K'), ord('P'), ord('U'))]

print(cap2)


list1 = ["b", "a", "c", "d", "e", "f", "g", "h", "i", "j"]

g = sorted(list1)

print(g)

print(list1)

print("------------------------------------------------------------------------------------------------------------------------------------------------------")

print("Ex: Sort a list")

def string_to_list(input_string):
    return list(input_string)

input = "tasterturkriger"
result_list = string_to_list(input)
c = sorted(result_list)
print(c)

print("------------------------------------------------------------------------------------------------------------------------------------------------------")

print("Ex: Text editor plugin simulation")

l = ["Claus", "Ib", "Per"]

hola = sorted(l)

hola.reverse()

print(hola)




