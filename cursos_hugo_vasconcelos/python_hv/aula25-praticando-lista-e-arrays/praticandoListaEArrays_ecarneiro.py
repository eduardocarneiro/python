
# list of students

students = []

studentsNumber = int(input("How many students you'd like to register: "))

studentsCount = 0

while studentsCount < studentsNumber:
    studentsCount += 1
    studentsNew = input("Type the name of the student %i/%i: " %(studentsCount,studentsNumber))
    students.append(studentsNew)

# report of students

print("\n")
print("Now lets input students reports")

studentsReports = []

for report in students:
    studentsReports = 0
    for reportEachStudent in range(1, 5):
        print("Type the report " + str(reportEachStudent) + " from " + report)
        getStudentReport = float(input())
        studentsReports += getStudentReport
        studentsScore = studentsReports / 4

    print(report + " score is: " + str(studentsScore))
