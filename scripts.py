from datacenter.models import Schoolkid, Chastisement, Commendation, Mark
from commendation_examples import commendations_examples


def create_commendation(child_name, subject):
	child = Schoolkid.objects.get(full_name__contains=child_name)
	last_lesson = Lesson.objects.filter(year_of_study=6, 
	group_letter='А', 
	subject__title=subject).order_by('-date').first()

	Commendation.objects.create(
	text=random.choice(commendations_examples), 
	created=last_lesson.date, 
	schoolkid=child, 
	subject=last_lesson.subject, 
	teacher=last_lesson.teacher
 	) 


def remove_chastisements(schoolkid):
	child = Schoolkid.objects.get(full_name__contains=schoolkid)
	chastisements = Chastisement.objects.filter(schoolkid=child)
	for chastisement in chastisements:
 		chastisement.delete()


def fix_marks(schoolkid):
	child = Schoolkid.objects.get(full_name__contains=schoolkid)
	bad_marks = Mark.objects.filter(schoolkid=child, points__in = [2, 3])
	for mark in bad_marks:
 		mark.points = 5
 		mark.save()
