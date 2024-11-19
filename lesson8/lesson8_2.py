import random
def get_names(nums:int=2)->list[str]:
    with open('names.txt',encoding='utf-8',mode='r') as file:
        names_str = file.read()
    names:list[str] = names_str.split(sep='\n')
    names = random.choices(names,k=nums)
    return names

def generate_students(names:list[str]) -> list[dict]:
    students:list[dict] = []
    for name in names:
        height = random.randint(140,190)
        weight = random.randint(50,110)
        BMI = weight / ((height/100)**2)
        status = get_status(BMI)
        student = {'名字': name, '身高': height, '重量': weight, 'BMI': BMI, '狀態':status}
        students.append(student)
    return students

def get_status(BMI:int)->str:#有傳出值的function
    if BMI >=35:
        status = "重度肥胖"
    elif BMI >= 30:
        status = "中度肥胖"
    elif BMI >= 27:
        status = "輕度肥胖"
    elif BMI >= 24:
        status = "過重"
    elif BMI >= 18.5:
        status = "正常範圍"
    else:
        status = "體重過輕"

    return status 



nums = int(input('請輸入學生數量:'))
student_names:list[str] = get_names(nums=nums)
students = generate_students(names=student_names)
for name in students:
    for key,value in name.items():
        print(f'{key}:{value}')
    print('=========================')

