import random
select=input('select to roll the dice yes or no: ')
a=random.randint(1,6)
if select == "yes":
  print(a)
  if a==1:
      print(' _______')
      print('|       |')
      print('|   .   |')
      print('|_______|')
  elif a==2:
      print(' _______')
      print('|       |')
      print('|  . .  |')
      print('|_______|')
  elif a==3:
      print(' _______')
      print('| .   . |')
      print('|   .   |')
      print('|_______|')
  elif a==4:
      print(' ______ ')
      print('| .  . |')
      print('| .  . |')
      print('|______|')
  elif a==5:
      print(' ______ ')
      print('|.    .|')
      print('|. .  .|')
      print('|______|')
  elif a==6:
      print(' ______ ')
      print('|. . . |')
      print('|. . . |')
      print('|______|')
  select1=input('u wanna roll again? yes or no:')
  while select1 =="yes":
   b=random.randint(1,6)
   print(b)
   if b==1:
      print(' _______')
      print('|       |')
      print('|   .   |')
      print('|_______|')
   elif b==2:
      print(' _______')
      print('|       |')
      print('|  . .  |')
      print('|_______|')
   elif b==3:
      print(' _______')
      print('| .   . |')
      print('|   .   |')
      print('|_______|')
   elif b==4:
      print(' ______ ')
      print('| .  . |')
      print('| .  . |')
      print('|______|')
   elif b==5:
      print(' ______ ')
      print('|.    .|')
      print('|. .  .|')
      print('|______|')
   elif b==6:
      print(' ______ ')
      print('|. . . |')
      print('|. . . |')
      print('|______|')
   break
  if select1=='no':
     print('thankyou for playing')
elif select == 'no':
  print('thankyou for playing')
