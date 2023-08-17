from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid, Subject, Teacher)
from datetime import date


def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
    for mark in bad_marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    comments = Chastisement.objects.filter(schoolkid=schoolkid)
    comments.delete()


def create_commendation(student_name, subject_title, text):
    try:
        student = Schoolkid.objects.get(full_name__contains=student_name)

        subject = Subject.objects.get(title=subject_title, year_of_study=student.year_of_study)

        subject_lessons = Lesson.objects.filter(
            subject=subject,
            year_of_study=student.year_of_study,
            group_letter=student.group_letter
        ).order_by('-date')

        if subject_lessons.exists():
            lesson_date = subject_lessons.first().date
        else:
            lesson_date = date.today()

        teacher = subject_lessons.first().teacher

        commendation = Commendation(
            text=text,
            created=lesson_date,
            schoolkid=student,
            subject=subject,
            teacher=teacher,
        )
        commendation.save()

        return True, "Похвала успешно создана."

    except Schoolkid.DoesNotExist:
        return False, "Ученик не найден."
    except Subject.DoesNotExist:
        return False, "Предмет не найден."
    except Teacher.DoesNotExist:
        return False, "Учитель не найден."
    except Exception as e:
        return False, str(e)
