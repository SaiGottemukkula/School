length = int(input('Enter the length: '))
width = int(input('Enter the width: '))
height = int(input('Enter the height: '))
window = int(input('Enter the number of windows: '))
door = int(input('Enter the number of doors: '))
area1 = length * width * height
finalarea = area1 - (15) * window - (21) * door
paint = int(finalarea/400 - 10)
if int(finalarea/400) == float(finalarea/400):
  print(finalarea/400 - 10)
else:
  print(int(finalarea/400 + 1) - 10)
  print('You will need', paint + 1, 'gallon-container(s) of paint')
  