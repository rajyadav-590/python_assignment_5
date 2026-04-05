#using try and except.
try:
    dictionary_name_marks = {
        "raj":90,
        "shyam":80,
        "raman":50,
        "suresh":60,
        "puneet":80,
        "sameer":70,
        "azhan":60
    }
    user_input = input("Enter the student's name: ").strip()
    print(f"{user_input}'s marks: {dictionary_name_marks[user_input.lower()]}")
except KeyError:
    print("Student not found.")



#without using try and except
# dictionary_name_marks = {
#     "raj": 90,
#     "shyam": 80,
#     "raman": 50,
#     "suresh": 60,
#     "puneet": 80,
#     "sameer": 70,
#     "azhan": 60
# }

# user_input = input("Enter the student's name: ").strip().lower()

# if user_input in dictionary_name_marks:
#     print(f"{user_input.capitalize()}'s marks: {dictionary_name_marks[user_input]}")
# else:
#     print("Student not found.")