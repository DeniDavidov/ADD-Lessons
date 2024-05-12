# Код писался без учета полученных знаний по циклам и условным операторам
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()
grades_average = [(sum(grades[0], 0)) / (len(grades[0])), (sum(grades[1], 0)) / (len(grades[1])), \
                  (sum(grades[2], 0)) / (len(grades[2])), (sum(grades[3], 0)) / (len(grades[3])), \
                  (sum(grades[4], 0)) / (len(grades[4])), ]
grades_students = dict(zip(students_list, grades_average))
print(grades_students)
