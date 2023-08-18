from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid, Subject, Teacher)
from datetime import date
from django.core.exceptions import MultipleObjectsReturned


def get_schoolkid(student_name):
    try:
        student = Schoolkid.objects.get(full_name__contains=student_name)
        return student
    except Schoolkid.DoesNotExist:
        return None
    except MultipleObjectsReturned:
        return None


def fix_marks(schoolkid):
    student = get_schoolkid(schoolkid)
    bad_marks = Mark.objects.filter(schoolkid=student, points__lt=4)
    bad_marks.update(points=5)


def remove_chastisements(schoolkid):
    student = get_schoolkid(schoolkid)
    comments = Chastisement.objects.filter(schoolkid=student)
    comments.delete()


def create_commendation(student_name, subject_title, text):
    try:
        student = get_schoolkid(student_name)
        if student is None:
            return False, "Ученик не найден."

        subject = Subject.objects.get(title=subject_title, year_of_study=student.year_of_study)
        subject_lessons = Lesson.objects.filter(
            subject=subject,
            year_of_study=student.year_of_study,
            group_letter=student.group_letter
        ).order_by('-date')

        lesson_date = subject_lessons.first().date or date.today()

        teacher = subject_lessons.first().teacher

        Commendation.objects.create(
            text=text,
            created=lesson_date,
            schoolkid=student,
            subject=subject,
            teacher=teacher,
        )

        return True, "Похвала успешно создана."

    except Subject.DoesNotExist:
        return False, "Предмет не найден."
    except MultipleObjectsReturned as m:
        return False, str(m)
    except Exception as e:
        return False, str(e)
