total_students=0
total_score=0

while True:
  name=input('Enter student name (or q to quit):')

  if name=='q':
    break

  score=int(input('Enter score:'))

  if score<0 or score>100:
      print('Invalid score. Please enter a number between 0 and 100.' )
      continue

  if score >=90:
    grade='A'

  elif score>80:
    grade='B'

  elif score>=70:
    grade='C'

  elif score>60:
    grade='D'

  else:
    grade='F'

  print(name+':',score, '->',grade)

  total_students=total_students+1
  total_score=total_score+score

if total_students>0:
  average=total_score/total_students

  print('Total students:',total_students)
  print('Average score:',round(average,2))

else:
  print('No students entered.')

