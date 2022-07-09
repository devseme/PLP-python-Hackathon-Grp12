#A list of careers.
careers = ['Engineering','Medicine','Teaching','Accounting','Finance']
print("Choose from these career: ",careers)

#Career questions.
career_questions = ['Do you love Science and Technology?' ,
                    'Do you love exploring the human body?',
                    'Are you capable of  Training others?',
                    'Are you good in handling accounts?',
                    'Can you handle Businesses well?']

#Career advice 
career_advice = ['Love technology, take the Engineering course. ' ,
                 'Like exploring the human body , take the Medicine course.',
                 'Like training others , take the Teaching course',
                 'Good in handling accounts , take the Accounting course' ,
                 'Good in handling  businesses , take the Finance course']

#Student chooses a career.
career_choice = input("Enter your career choice")


#Determining if a student is eligible.
if(career_choice == careers[0]):
  print("If yes , enter 1 in the next question")
  career_process = input(career_questions[0])
  
  if(career_process == 1):
    print(career_advice[0])
  else:
    print("Choose another career")


elif(career_choice == careers[1]):
  career_process = input(career_questions[1])
  if(career_process == 1):
    print(career_advice[1])
  else:
    print("Choose another career")

elif(career_choice == careers[2]):
  career_process = input(career_questions[2])
  if(career_process == 1):
    print(career_advice[2])
  else:
    print("Choose another career")

elif(career_choice == careers[3]):
  career_process = input(career_questions[3])
  if(career_process == 1):
    print(career_advice[3])
  else:
    print("Choose another career")

else:
  career_process = input(career_questions[4])
  if(career_process == 1):
    print(career_advice[4])
  else:
    print("Choose another career")
