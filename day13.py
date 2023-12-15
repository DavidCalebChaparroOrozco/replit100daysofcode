print("Exam")
name_of_exam = input("Enter the name of exam: ")
total_score = int(input("Enter the max score: "))
your_score = int(input("Enter your score: "))

number_score = float(your_score / total_score)
final_number = round(number_score,3)
final_perc = round(float(your_score / total_score) * 100,3)

print("You score", final_perc, "%")

if final_number >= .90:
  print("You score is an A+")
elif final_number >= .80 and final_number <= .89:
  print("You score is an A-")
elif final_number >= .70 and final_number <= .79:
  print("You score is an B")
elif final_number >= .60 and final_number <= .69:
  print("You score is an C")
elif final_number >= .50 and final_number <= .59:
  print("You score is an D")
elif final_number >= .50:
  print("You score is an U")
else:
  print("Try again")
