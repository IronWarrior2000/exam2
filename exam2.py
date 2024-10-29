#Bill Nguyen | 10/29/24 | Exam 2

# Create a student management system in Python with a Student class that includes student_id, name, and score attributes, 
# along with a __str__ method to display student details. Write functions to manage a list of Student objects: add_student 
# to add a new student, search_student to perform a linear search by student_id and return details or "Student not found," 
# and sort_students to sort the list by score in descending order. Start by creating a sample list of at least three Student 
# objects for testing. Then, use add_student, sort_students, and search_student to demonstrate the functionality. Include output 
# for the results of these operations clearly, showing the sorted list of students and the results of any search performed.

class Student:

    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score

    def setStudentID(self, id):
        self.student_id = id

    def setName(self, name):
        self.name = name

    def setScore(self, score):
        self.score = score

    def getStudentID(self):
        return self.student_id

    def getName(self):
        return self.name

    def getScore(self):
        return self.score
    
    def __str__(self):
        return f"Student: {self.name} - ID: {self.student_id} - Score: {self.score}\n"

def userInput():
    user = input("Enter in the value here?")
    return user

def students():
    student1 = Student(101, "Jimmy Smith", 73)
    student2 = Student(102, "Tyler Adams", 98)   
    student3 = Student(103, "Fred Robbie", 82)
    studentsList = [student1, student2, student3]
    
    return studentsList

def add_student(studentsList):
    print(f"To add student please enter in their name, school ID, and score here!!")
    name = userInput()
    id = int(userInput())
    score = int(userInput())
    newStudent = Student(id, name, score)
    print(f"\n{newStudent.getName()} has been added.\n\n")
    studentsList.append(newStudent)
    for x in studentsList:
        print(x)
    return studentsList

def searchStudent(studentsList, target):
    for index in range(len(studentsList)):
        if studentsList[index] == target:
            return index
    return -1


def sortStudent(studentsList):
    for index in range(len(studentsList)):
        minimumIndex = index
        for max in range(index+1, len(studentsList)):
            if studentsList[max] < studentsList[minimumIndex]:
                minimumIndex = max

        studentsList[index], studentsList[minimumIndex] = studentsList[minimumIndex], studentsList[index] 
    return studentsList


def main():
    while True:
        try:
            studentsList = students()
            print("Welcome to the Student Management System")
            print(f"1. Add a Student \n2. Search a Student \n3. Sort Students \n4. Exit System")
            user = int(userInput())
            if user == 1:
                add_student(studentsList)
            elif user == 2:
                print("Who do you want to search for?")
                for x in studentsList:
                    print(x)
                target = int(input("Enter in their ID here"))
                results = searchStudent(studentsList, target)
                if results != -1:
                    print(f"Student Found at index!\n {results}")
                else:
                    print(f"Sorry that Student cannot be found or does not exist in the system")
            elif user == 3:
                sortedStudentList = sortStudent(studentsList)
                for x in sortedStudentList:
                    print(x)
            elif user == 4:
                break
            else:
                print("Please enter in the number of one of the 4 options above.")



        except ValueError:
            print("ValueError")
    

main()