# Room Dimentions
length = int(input('Enter the length: '))
width = int(input('Enter the width: '))
height = int(input('Enter the height: '))
window = int(input('Enter the number of windows: '))
door = int(input('Enter the number of doors: '))
if length > 0 and width > 0 and height > 0:
  # Wall Dimensions (4 In Total)
  wall1 = length * height
  wall2 = height * width
  # Finding The Amount Of Paint Needed
  total_area = 2 * (wall1 + wall2)
  # ^ Total Area (Including Windows And Doors)
  final_area = total_area - 15 * window - 21 * door
  # One Gallon-Bucket Of Paint Covers 400 Square Feet
  buckets = int(final_area / 400)
  # ^ Gallons Of Paint
  # Rounding Up If Needed
  if final_area % 400 != 0:
    buckets = buckets + 1
  print('You Need', buckets, 'Gallon-Buckets Of Paint')
else:
  print('The Values For The Length, Width, And Height Have To Be Greater Than Zero')