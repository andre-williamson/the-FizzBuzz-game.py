#Write your code below this row 👇
nums = 0 
for nums in range(0,101):
  print(nums)
  if  nums % 3 == 0 and nums % 5 ==0:
    print("fizzbuzz")
  if nums  % 5 == 0: 
   print("buzz")
  if nums % 3 == 0:
     print("fizzbuzz")