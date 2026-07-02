#Q.10)
import numpy as np
marks = np.random.randint(30, 101, size=(10, 5))
print("Student Marks (10 x 5):")
print(marks)
total_marks = marks.sum(axis=1)
average_marks = marks.mean(axis=1)
# Total and average marks
print("\nTotal Marks of Each Student:")
print(total_marks)
print("\nAverage Marks of Each Student:")
print(average_marks)
# Student with the highest total marks
highest_student = np.argmax(total_marks)
print("\nStudent with Highest Total Marks:", highest_student + 1)
print("Total Marks:", total_marks[highest_student])
# Student with the lowest total marks
lowest_student = np.argmin(total_marks)
print("\nStudent with Lowest Total Marks:", lowest_student + 1)
print("Total Marks:", total_marks[lowest_student])
# Class mean and standard deviation
print("\nOverall Class Mean:", marks.mean())
print("Overall Class Standard Deviation:", marks.std())
reshaped_marks = marks.reshape(5, 10)
print("\nReshaped Array (5 x 10):")
print(reshaped_marks)
# Marks of the top 3 students
top3 = np.argsort(total_marks)[-3:][::-1]
print("\nTop 3 Students and Their Marks:")
for i in top3:
    print("Student", i + 1, ":", marks[i])

