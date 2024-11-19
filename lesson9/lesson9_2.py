import tools
if __name__ == '__main__':
 nums = int(input('請輸入學生數量:'))
 student_names:list[str] = tools.get_names(nums=nums)
 students = tools.generate_students(names=student_names)
 for name in students:
    for key,value in name.items():
        print(f'{key}:{value}')
    print('=========================')