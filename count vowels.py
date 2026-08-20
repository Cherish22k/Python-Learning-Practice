#CODE:

string = input("Enter string:").lower()
vowels = "aeiou"
count = 0 
for ch in string:
  if ch in vowels:
    count +=1

print("vowels:" , count)
