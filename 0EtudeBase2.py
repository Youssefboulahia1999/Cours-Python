names = ['youssef','youssef2','youssef3']
names = names + ['youssef4']
print(names)
movie_titles = ["Eternal Sunshine of the Spotless Kandy","Memento","Requiem for a Dream"]

numbers = [344, 345, 23, 14, 566, 696, 9]

print(names[1])
#le - donne le dernier element
print(names[-1])

names.append('youssef4')
print(names[-1])

names = names = ['youssef5']
print(names[-1])

#ajouter a la fin
names.extend(['youssef6','youssef7'])
print(names[-2],names[-1])
num = [1,2,4,5]

#ajoute a la place 2 le 3
num.insert(2,3)

print(num)
print(names)
print(names)

names.remove("youssef7")
print(names)

del names[0]

print(names)


names = ['youssef','youssef2','youssef3']
#supprime la dernier ou n'inporte qu'elle index
names.pop(1)
names.pop()
print(names)
names = ['youssef','youssef2','youssef3']
print(names)
names.clear()
print(names)


tuple_ = ('truc','truc2','truc3')
print(tuple_)
#remove ne marche pas dans un tuple
# tuple_.remove('truc3')
print(tuple_[2])

movies = [
("Eternal Sunshine of the Spotless Mind", 2004),
("Memento", 2000),
("Requiem for a Dream", 2000)
]

print(movies[1][0])
for i in movies:
    for a in i:
        if a == 'Requiem for a Dream':
            truc = a
print(truc)

# Operateurs de comparaison 
print(5 < 10)
print(5 > 10)
print(10 > 10)
print("A" < "a")
#<= et >=
print(10 > 10)
print(10 >= 10)

#is is not
a = [1,2,3]
b = [1,2,3]
c = a

print(id(a))
print(id(b))
print(id(c))

print(a == b)
print(a is b)
print(a is c)


