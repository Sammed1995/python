import datetime

user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_date - today_date

print(f"Dear user! Time remaining for your goal: {goal} is {time_till}")

Enter your goal with a deadline separated by colon
Project Submission:30.09.2025
Dear user! Time remaining for your goal: Project Submission is 30 days, 12:34:56.789012
