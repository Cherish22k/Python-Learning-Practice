#Code

def findlargest(arr):
  if not arr:
    return 0

  max_value = arr[0]

  for num in arr:
    if num > max_value:
      max_value = num 

  return max_value
  print(findlargest)

 
