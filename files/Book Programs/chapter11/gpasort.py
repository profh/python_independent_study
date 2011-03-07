# gpasort.py
#    A program to sort student information into GPA order.


from gpa import Student, makeStudent

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        outfile.write("%s\t%f\t%f\n" %
                      (s.getName(), s.getHours(), s.getQPoints()))
    outfile.close()
                      
def cmpGPA(s1, s2):
    return cmp(s1.gpa(), s2.gpa())

def main():
    print "This program sorts student grade information by GPA"
    filename = raw_input("Enter the name of the data file: ")
    data = readStudents(filename)
    data.sort(cmpGPA)
    filename = raw_input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print "The data has been written to", filename

if __name__ == '__main__':
    main()
    
