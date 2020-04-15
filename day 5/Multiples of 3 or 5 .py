def solution(number):
  numb =[]
  
  for x in range(number):
      if (x%5==0) or (x%3==0):
          if x not in numb:
              numb.append(x)
  
  return sum(numb)