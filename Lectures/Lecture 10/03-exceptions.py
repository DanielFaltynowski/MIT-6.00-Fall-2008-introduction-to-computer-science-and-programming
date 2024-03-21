def realVal(valType, requestMessage, errorMessage):
    while True:
        val = input(requestMessage)
        try:
            val = valType(val)
            return val
        except:
            print(errorMessage)


def getGrades(fileName):
    try:
        gradesFile = open(fileName, 'r')
    except IOError:
        print('Could not open', fileName)
        raise 'GetGradesError'
    grades = []
    for line in gradesFile:
        grades.append(float(line))
    return grades


print(realVal(float, 'Enter a float: ', 'Invalid float value!'))

try:
    grades = getGrades('grades.txt')
    grades.sort()
    median = grades[len(grades) // 2]
    print('Median grade is', median)
except 'GetGradesError':
    print('Whoops!')