import gear
import gear.widget
if __name__ == '__main__':
 nums = int(input('請輸入學生數量:'))
 student_names:list[str] = gear.widget.get_names(nums=nums)
 students = gear.widget.generate_students(names=student_names)
 for name in students:
    for key,value in name.items():
        print(f'{key}:{value}')
    print('=========================')