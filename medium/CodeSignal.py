'''
Given a list of student grades (a value between 1 to 5) records in the following format: "[name]: [grade]", find the student with the highest average grade. It is guaranteed that all students have different average grades.

Note: names do not contain spaces, and each grade is an integer in the string.

Example

For records = ["John: 5", "Michael: 4", "Ruby: 2", "Ruby: 5", "Michael: 5"], the output should be solution(records) = "John".

Let's calculate students' average grades:

"John" = 5
"Michael" = (4 + 5) / 2 = 4.5
"Ruby" = (2 + 5) / 2 = 3.5.
Since 5 > 4.5 > 3.5, the result is "John".
For records = ["Kate: 5", "Kate: 5", "Maria: 2", "John: 5", "Michael: 4", "John: 4"], the output should be solution(records) = "Kate".

Let's calculate students' average grades:

"Kate" = (5 + 5) / 2 = 5
"Maria" = 2
"John" = (5 + 4) / 2 = 4.5
"Michael" = 4
Since 5 > 4.5 > 4 > 2, the result is "Kate".
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.string records

An array of strings representing students' names and their grades.

Guaranteed constraints:
1 ≤ records.length ≤ 100,
1 ≤ records[i] ≤ 20.

[output] string

Return the name of the student who has the highest average grade.
'''

def solution(records):
    '''
    
    keep track of the students individaul name 
    students occurrences
    keep each grades 
    {
        micheal : [9,2]
    }
    obj 
    highest = 0
    output = name
    loop list 
    add name to the obj 
    if the exist, add the grade to the first value in the array 
    increment the second numbers
    '''
    
    students = {}
    output = ""
    highest = float("-inf")
    
    for record in records:
        student = record.split(":") 
        print(student)
        name = student[0] 
        grade = int(student[1]) 
        if name in students:
            students[name][0]+= grade
            students[name][1]+=1
        else:
            students[name] =[grade,1]
        
        
    for name,(total, count) in students.items():
        average = total/count
        if average > highest:
            highest = average   
            output = name
            
    print(students , highest)        
    
    return output
