# Room Dimentions
length = int(input('Enter the length: '))
width = int(input('Enter the width: '))
height = int(input('Enter the height: '))
window = int(input('Enter the number of windows: '))
door = int(input('Enter the number of doors: '))
# Wall Dimentions (4 In Total)
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