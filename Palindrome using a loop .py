#CODE:

text = input("Enter a string:")
reverse = " "
for char in text:
  reverse = char + reverse
if text == reverse:
  print("Palindrome")
else:
  print("Not a Palindrome")


#OUTPUT:
Enter a string: 23456
Not a Palindrome
