

all_done = False
while not all_done:
    gpa = float(input("Please enter a valid US GPA from 0.0 to 4.0"))
    if 0.0 <= gpa <= 4.0:
        all_done = True
print(f"Your gpa is {gpa}")