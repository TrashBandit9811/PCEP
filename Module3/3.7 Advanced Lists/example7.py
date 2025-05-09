rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# THREE dimensional list

# Hotel of three buildings, 15 floors, 20 rooms per floor

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

rooms[1][9][13] = True

rooms[0][4][1] = True

vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

print("There are", vacancy, "rooms available on the 15th floor of building 3.")


i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
      break
    print("*")
