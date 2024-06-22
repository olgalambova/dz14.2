from student import Student
from group import Group
from group_limit_reached_exception import GroupLimitReachedException

def main():
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    st3 = Student('Male', 25, 'Liza', 'Taylor', 'AN145')
    st4 = Student('Male', 25, 'Liza', 'Taylor', 'AN145')
    try:
        gr = Group('PD1')
        gr.add_student(st1)
        gr.add_student(st2)
        gr.add_student(st3)
        gr.add_student(st4)

    except GroupLimitReachedException as error:
        print(error)
    except Exception as error:
        print(error)

    print(gr)

if __name__ == '__main__':
    main()

