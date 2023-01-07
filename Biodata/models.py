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

NATIONALITY_CHOICE =(
    ("Ghanaian","Ghanaian" ),
    ("Nigerian", "Nigerian"),
    ("Benin", "Benin"),
    ("Garbon",  "Garbon"),    
    )

class ApplicantDetail(models.Model):
    Title = models.CharField(choices= TITLE_CHOICE, max_length=20)
    Surname = models.CharField(max_length=255, verbose_name="Surname")
    FirstName = models.CharField(max_length=255, verbose_name= "First Name")
    MiddleName = models.CharField(max_length=255, blank=True,null=True,verbose_name="Middle Name" )
    DateofBirth = models.DateField(verbose_name="Date of Birth")
    Gender = models.CharField(choices = GENDER_CHOICE, max_length=20)
    PlaceofBirth = models.CharField(max_length=30, verbose_name="Place of Birth")
    RegionofBirth = models.CharField(max_length=30, verbose_name="Region of Birth")
    Hometown = models.CharField(max_length=20, verbose_name="Hometown")
    RegionofHometown = models.CharField(max_length=30, verbose_name="Region of Hometown")
    Nationality = models.CharField(max_length=30,choices= NATIONALITY_CHOICE, verbose_name="Nationality")


    def __str__(self) -> str:
        return self.Surname + " " +self.FirstName 
