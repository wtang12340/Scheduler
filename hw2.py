#!/usr/bin/env python
"""
NAME: William Tang
Assignment 2
CS440 / CS640 Artificial Intelligence
"""


import collections
import sys

def ReadInputFile(filename):
  """Read a scheduling problem from a text file.

  Input format: One line per student, space-separated columns.  The first
  column is the student, the remaining columns represent the shifts that
  student is available to work.

  Example input file format:
  Alice 0 1 2 3
  Bob 1 2
  Charlie 2 3
  Danielle 3 0

  Returns:
      A map from student to a list of shifts.
  """
  with open(filename) as input_file:
    return dict((fields[0], fields[1:]) for line in input_file
        for fields in (line.split(),))

def Solve(student_availabilities):
  """Solve the constraint satisfaction problem.

  Args:
    student_availabilities: a dictionary mapping a student (a string) to a list
        of shifts in which that student can work (also strings)

  Returns:
    A dictionary mapping shifts to pairs of different students.  All times
        mentioned in the input must have entries; all students must appear
        with two different shifts, and if a shift t is mapped to student s,
        student_availabilities[s] must include t.
  """
  #dictionary with final answer
  resultDict = {}
  #dictionary of students mapped with number of shifts assigned
  shiftsAssigned = {}  
  #sorted list of open shifts
  sortedOpen = []
  #number of people assigned to shift index
  numAssigned = []
  #maximum number of shifts
  max_shift = 0

  #Creates a sorted list based on the number of available shifts of each student using helper function.
  sortedOpen, max_shift = sortByNumShifts(student_availabilities)

  #Fills number of shifts assigned into shiftsAssigned
  shiftsAssigned = listStudentShifts(student_availabilities)
  for i in range(max_shift+1):
      numAssigned.append(0)

  #The following assigns students to shifts.    
  for numShifts in sortedOpen:
      
    for student in sortedOpen[numShifts]:
        
        #Goes through each shift of a student and assign them if the shift is not filled
        for shift in student_availabilities[student]:
            if (numAssigned[int(shift)] < 2 and shiftsAssigned[student] < 2):
                if (int(shift) not in resultDict.keys()):
                    resultDict[int(shift)] = student
                else:
                    resultDict[int(shift)] = (resultDict[int(shift)], student)
                #increments number of shifts assigned to a student
                shiftsAssigned[student] += 1
                #increments the number of students assigned to a shift
                numAssigned[int(shift)] += 1

        #The following ensures a student is assigned 2 shifts.        
        if ((shiftsAssigned[student] < 2)):
            swap = False
            #Goes through student's shifts again and swaps shift assignments
            for s in student_availabilities[student]:
                students = resultDict[int(s)]
                student1 = students[0]
                student2 = students[1]
                if(student != student1 or student != student2):
                    
                    #Tries to swap student 1
                    for s1 in student_availabilities[student1]:
                        if (len(s1) == 2):
                            pass
                        else:
                            #Goes through and see if a swap is possible
                            for currentShift in s1:
                                #Check if student 1 already assigned to a current shift
                                if (numAssigned[int(currentShift)] < 2 and not swap):
                                    resultDict[int(currentShift)] = (resultDict[int(currentShift)], student1)
                                    resultDict[int(s)] = (student, student2)
                                    numAssigned[int(currentShift)] += 1
                                    swap = True
                                    
                    #Tries to swap student 2                
                    if (not swap):
                        for s2 in student_availabilities[student2]:
                            if (len(s2) == 2):
                                pass
                            else:
                                #Go through student 2's shifts and see if swap possible
                                for currentShift in s2:
                                    if (numAssigned[int(currentShift)] < 2 and not swap):
                                        resultDict[int(currentShift)] = (resultDict[int(currentShift)], student2)
                                        resultDict[int(s)] = (student, student1)
                                        numAssigned[int(currentShift)] += 1
                                        swap = True
                  
  #returns the final solution
  for x in range(len(numAssigned)):
      if (numAssigned[x] != 2):
          return {}
        
  #put names in alphabetical order
  for shift, students in resultDict.iteritems():
      x, y = students
      l = [x,y]
      l.sort()
      students = tuple(l)
      resultDict[int(shift)] = students
      shift = str(shift)
      
  #changing integers back to strings for the keys to run tests
  for shift in resultDict.keys():
      resultDict[str(shift)] = resultDict.pop(shift)
  return resultDict

#Creates a sorted list based on the number of available shifts of each student.
def sortByNumShifts(student_availabilities):
    sortedOpen = {}
    max_shift = 0  
    for student, shifts in student_availabilities.iteritems():
        numShifts = len(shifts)
        for currentShift in shifts:
            if max_shift < int(currentShift):
                max_shift = int(currentShift)
        if numShifts not in sortedOpen.keys():
            sortedOpen[numShifts] = [student]
        else:
            sortedOpen[len(shifts)].append(student)
    return sortedOpen, max_shift

#Creates a list that returns number of shifts assigned to a student
def listStudentShifts(studentList):
    newStudentList = {}
    for student, shift in studentList.iteritems():
        newStudentList[student] = 0
    return newStudentList

def main():
  student_availabilities = ReadInputFile(sys.argv[1])
  solution = Solve(student_availabilities)
  if solution:
    for time, (student0, student1) in solution.iteritems():
      print time, student0, student1
  else:
    print 'No satisfying assignment exists'
    
if __name__ == '__main__':
  main()
