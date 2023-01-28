from django.db import models
from django.core.exceptions import ValidationError

# skills grade.
GRADE = [
    ('1', 'little'),
    ('2', 'good'),
    ('3', 'Excellent'),
]
class Skill(models.Model):

    type = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    status = models.CharField(
       max_length=32,
       choices=GRADE,
       default="1",
    )
    def format_skills():
        '''format data do be readable by html '''
        skills_format = []
        skills_type = Skill.objects.values('type').distinct()
        for sk_type in skills_type:
            list_skills = []
            req = Skill.objects.filter(type__contains=sk_type['type']).values('name', 'status')
            for i in req: 
                list_skills.append(i)
            sorted_list_skills = sorted(list_skills, key=lambda item: item.get("status"),reverse=True)

            skills_format.append({'type': sk_type['type'], 'skills' : sorted_list_skills})
        return (skills_format)

    def __str__(self):
        return f'{self.type} - {self.name} - {self.status}'

class Experience(models.Model):
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    start_date = models.CharField(max_length=4, default="")
    end_date = models.CharField(max_length=4 )
    missions = models.TextField(max_length=1000)
    location = models.CharField(max_length=100, default="")
   
    def __str__(self):
        return f'{self.company} - {self.title}'

class Formation(models.Model):
    school = models.CharField(max_length=40)
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=10)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.title}'

class PersoInformation(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    mail = models.EmailField(max_length=64)
    website = models.CharField(max_length=128)
    job_title = models.CharField(max_length=64)
    linkedin = models.CharField(max_length=128)
    github = models.CharField(max_length=128)
    numberphone = models.CharField(max_length=100)
    location = models.CharField(max_length=128)
    information = models.TextField(max_length=1024)
    hobbies = models.TextField(max_length=1024)
    file_cv = models.FileField(upload_to='resume', blank=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    def clean(self):
        if PersoInformation.objects.exists() and not self.pk:
            raise ValidationError('You can have only one personnal information')
    class Meta:
        
        verbose_name = 'Personnal information'
        verbose_name_plural = 'Personnal information'

