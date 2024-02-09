line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")

pos = input("Where do you want to put the treasure? \n").lower()
if pos == "a1":
  map[0][0] = "X"
elif pos == "b1":
  map[0][1] = "X"
elif pos == "c1":
  map[0][2] = "X"
elif pos == "a2":
  map[1][0] = "X"
elif pos == "b2":
  map[1][1] = "X"
elif pos == "c2":
  map[1][2] = "X"
elif pos == "a3":
  map[2][0] = "X"
elif pos == "b3":
  map[2][1] = "X"
elif pos == "c3":
  map[2][2] = "X"
else:
  print("Wrong Input")
print(f"{line1}\n{line2}\n{line3}")
