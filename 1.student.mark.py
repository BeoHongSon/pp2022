from datetime import datetime

def getStudentCount ():
    return int (input ("Enter number of students: "))
    
def getStudentDetails ():
    sid = input ("Enter student id: ")
    sname = input ("Enter student name: ")
    while True:
        try:
            sdob = input ("Enter student's date of birth dd/mm/yyyy: ")
            dob = datetime.strptime(sdob, "%d/%m/%Y")
        except ValueError:
            print("Wrong date of birth format!")
            continue
        break
    dobd = str(dob.day) + "-" + str(dob.month) + "-" + str(dob.year)
    return sid, sname, dobd
    
def getCourseCount ():
    return int (input ("Enter number of courses: "))
    
def getCourseDetails ():
    cid = input ("Enter course id: ")
    cname = input ("Enter course name: ")
    return cid, cname
    
def getMarks (sid, cid):
    prompt = f"Enter marks for student {sid} for course {cid}: ".format (sid, cid)
    input (prompt)
    
nStudents = getStudentCount ()
studentLst = []
for i in range (nStudents):
    id, nm, dob = getStudentDetails ()
    studentLst.append ((id, nm, dob))

print ("\nListing all students now...")
for s in studentLst:
    print (f"Student id: {s[0]} Name: {s[1]} Date of birth: {s[2]}")

nCourses = getCourseCount ()
courseLst = []
for i in range (nCourses):
    cid, cname = getCourseDetails ()
    courseLst.append ((cid, cname))
    
d = {}
while True:
  n = int (input ("Enter how many student-course marks do you want to enter? "))
  if n < 0 or n > nStudents * nCourses:
      print("Student-course marks is not available, re-enter please")
      continue
  break 
for i in range (n):
      while True:
          sid = input ("Enter student id: ")
          cid = input ("Enter course id: ")
          if sid not in [student [0] for student in studentLst]:
              print ("Bad student id!")
              continue 
          if cid not in [course [0] for course in courseLst]:
              print ("Bad course id!")
              continue 
          break
    
      while True:
          marks = float (input ("Enter marks: "))
          if marks < 0 or marks > 20:
              print("Mark is not available, please re-enter the mark")
              continue
          break
    
      if cid in d:
          d [cid].append ((sid, marks))
      else:
          d [cid] = [(sid, marks)]

print ("\nListing all courses now...")
for c in courseLst:
    print (f"Course id: {c[0]} Name: {c[1]}")
    
cid = input ("\nWhich course do you want to see all student marks for? ")
if cid in d:
    for tups in d [cid]:
        print (f"Student {tups[0]} got {tups[1]} marks")