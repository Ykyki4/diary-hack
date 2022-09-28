from datacenter.models import Schoolkid, Chastisement, Commendation, Mark
from commendation_examples import COMMENDATION_EXAMPLES


def create_commendation(child_name, subject, year_of_study, group_letter):
    child = Schoolkid.objects.get(full_name__contains=child_name)
    last_lesson = Lesson.objects.filter(year_of_study=year_of_study,
                                        group_letter=group_letter,
                                        subject__title=subject).order_by('-date').first()
    Commendation.objects.create(
                text=random.choice(COMMENDATION_EXAMPLES),
                created=last_lesson.date,
                schoolkid=child,
                subject=last_lesson.subject,
                teacher=last_lesson.teache
    )


def remove_chastisements(schoolkid):
    child = Schoolkid.objects.get(full_name__contains=schoolkid)
    Chastisement.objects.filter(schoolkid=child).delete()


def fix_marks(schoolkid):
    child = Schoolkid.objects.get(full_name__contains=schoolkid)
    bad_marks = Mark.objects.filter(schoolkid=child,
                                    points__in = [2, 3])
    bad_marks.update(points=5)
