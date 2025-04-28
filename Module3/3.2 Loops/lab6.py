blocks = int(input("Enter the number of blocks: "))

i=1
height=0
while blocks-i > 0:
    print(blocks, height, i)
    blocks-=i
    height+=1
    i+=1

print("The height of the pyramid:", height)

