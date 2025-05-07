beatles=[]
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
for i in range(2):
    beatle=input('Enter a beatle: ')
    beatles.append(beatle)

del beatles[3]
del beatles[3]

beatles.insert(0, 'Ringo Starr')

print(beatles)
