def students_credits(*courses_info, needed_credits=240):
    student_book = {}  # a dictionary to store the course name and Diyan's credits
    result = []  # a list to store the final output messages

    # loop through each course info in the input arguments
    for course_info in courses_info:
        # extract the course name, credits, max points, and student points from the input string
        course_name, course_credits, max_pts, student_pts = course_info.split("-")

        # calculate the percentage of points the student earned in the course
        current_percentage = int(student_pts) / int(max_pts)

        # calculate the number of credits Diyan earned in the course
        credits_taken = current_percentage * int(course_credits)

        # store the course name and credits earned in the dictionary
        student_book[course_name] = credits_taken

    # calculate the total number of credits earned across all courses
    total_credits = sum(student_book.values())

    # check if Diyan has enough credits for a diploma
    if total_credits >= needed_credits:
        result.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {needed_credits - total_credits:.1f} credits more for a diploma.")

    # loop through the courses and credits in the dictionary, sorted by credits earned
    for course, points in sorted(student_book.items(), key=lambda x: -x[1]):
        result.append(f"{course} - {points:.1f}")

    # join the output messages into a single string separated by newlines
    return "\n".join(result)
