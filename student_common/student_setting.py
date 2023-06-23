

def main():

    while True:

        menu()
        choice = int(input("请选择: "))

        if choice in range(0, 8):
            """判断为0的情况"""
            if choice == 0:
                answer = input("您确定要退出系统嘛？ y/n:")
                if answer == 'y' or answer == 'Y':
                    print("谢谢你的使用")
                    break
                else:
                    continue

            elif choice == 1:
                """调用1的录入学生信息函数"""
                insert()
            elif choice == 2:
                """调用2的查找学生信息函数"""
                search()
            elif choice == 3:
                """调用3的删除学生信息函数"""
                delete()
            elif choice == 4:
                """调用4的修改学生信息函数"""
                update()
            elif choice == 5:
                """调用5的成绩排序函数"""
                sort()
            elif choice == 6:
                """调用6的学生总人数函数"""
                count()
            elif choice == 7:
                """调用7显示所有学生信息函数"""
                show()


def menu():

    print("==============学生管理系统=====================")
    print("-----------------功能菜单----------------------")
    print("\t\t\t\t\t\t1.录入学生信息")
    print("\t\t\t\t\t\t2.查找学生信息")
    print("\t\t\t\t\t\t3.删除学生信息")
    print("\t\t\t\t\t\t4.修改学生信息")
    print("\t\t\t\t\t\t5.排序")
    print("\t\t\t\t\t\t6.统计学生总人数")
    print("\t\t\t\t\t\t7.显示所有学生信息")
    print("\t\t\t\t\t\t0.退出")
    print("-----------------------------------------------")

def insert():

    pass

def search():

    pass

def delete():

    pass

def update():

    pass

def sort():

    pass

def count():

    pass

def show():

    pass


if __name__ == '__main__':

    main()