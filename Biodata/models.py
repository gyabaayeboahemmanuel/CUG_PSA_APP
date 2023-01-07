from django.db import models


# Create your models here.
TITLE_CHOICE = (
 ("Mr.", "Mr."),
 ("Mrs.", "Mrs."),
 ("Ms.", "Ms"),
 ("Rev.", "Rev."),
 ("Sr.", "Sr.")
)

GENDER_CHOICE = (
    ("Male", "Male"),
    ("Female", "Female"),
)

class ApplicantDetail(models.Model):
    Title = models.CharField(choices= TITLE_CHOICE, max_length=20)
    Surname = models.CharField(max_length=255, verbose_name="Surname")
    FirstName = models.CharField(max_length=255, verbose_name= "First Name")
    MiddleName = models.CharField(max_length=255, blank=True,null=True,verbose_name="Middle Name" )
    DateofBirth = models.DateField(verbose_name="Date of Birth")
    Gender = models.CharField(choices = GENDER_CHOICE, max_length=20)
    

    def __str__(self) -> str:
        return self.Surname + " " +self.FirstName 
