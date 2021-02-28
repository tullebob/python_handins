import random
class Student():
    def __init__(self, name, gender, data_sheet, image_url ):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url
    
    def get_avg_grade(self):
        avgGrade = 0
        grades = self.data_sheet.get_grades_as_list()
        for grade in grades:
            avgGrade + grade
        return avgGrade/len(grades)



class Datasheet():
    def __init__(self, courses=[]):
        self.courses = courses  

    def get_grades_as_list():
        gradeList = []
        for course in self.course:
            gradeList.append(course.grade)
        return gradeList




class Course():
    def __init__(self, name, classroom, teacher, ETCS, grade=None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        if grade is not None:
            self.grade = grade

def create_student():
    names = ['Mark Agaard', 'Cecilie Nielsen', 'Albert Ilga' , 'Freja Lodbo' 'Daniel San', 'Mikkel Grønmark', 'Katrine Lang', 'Camilla Palsin']
    genders = ['Male', 'Female']
    grades = [-3, 0, 2, 4, 7, 10, 12]
    courses = [Course('English', '1A', 'Thorbjørn Alkin', 20, random.choice(grades)), Course('Danish', '2A', 'Signe Vindelbo', 15, random.choice(grades)), Course('Math', '3A', 'Jon Bertelsen', 35, random.choice(grades)), Course('AP', '4A', 'Lars Larsen', 40, random.choice(grades))]
    image_urls = ['https://cdn4.vectorstock.com/i/1000x1000/06/18/male-avatar-profile-picture-vector-10210618.jpg',
    'https://i1.wp.com/www.donofweb.com/wp-content/uploads/2012/08/animepaper.netavatar-standard-artists-kurehito-misaki-halloween-cant-be-this-cute-188406-yamaro-preview-87bc4fac.jpg',
    'https://www.seekpng.com/png/detail/506-5061704_avatar-png.png',
    'https://pbs.twimg.com/profile_images/1786517293/faceyourmanga-female-avatar.jpg']

    
