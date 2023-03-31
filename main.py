def calculate_gpa(grades, credits):
    total_grade_points = 0
    total_credits = 0
    for i in range(len(grades)):
        if grades[i] == 'A':
            grade_point = 4.0
        elif grades[i] == 'A-':
            grade_point = 3.7
        elif grades[i] == 'B+':
            grade_point = 3.3
        elif grades[i] == 'B':
            grade_point = 3.0
        elif grades[i] == 'B-':
            grade_point = 2.7
        elif grades[i] == 'C+':
            grade_point = 2.3
        elif grades[i] == 'C':
            grade_point = 2.0
        elif grades[i] == 'C-':
            grade_point = 1.7
        elif grades[i] == 'D+':
            grade_point = 1.3
        elif grades[i] == 'D':
            grade_point = 1.0
        elif grades[i] == 'F':
            grade_point = 0.0
        else:
            raise ValueError("Invalid grade")

        total_grade_points += grade_point * credits[i]
        total_credits += credits[i]

    if total_credits == 0:
        return 0.0
    else:
        return total_grade_points / total_credits