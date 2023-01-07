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
    PlaceofBirth=models.CharField(max_length=30, verbose_name="Place of Birth")

    def __str__(self) -> str:
        return self.Surname + " " +self.FirstName 

STATUS_CHOICE = (
    ("Alive", "Alive"),
    ("Dead", "Dead"),
)

class FamilyDetail(models.Model):
    FatherFullName = models.CharField(max_length=255, verbose_name="Father Full Name")
    FatherStatus = models.CharField(choices=STATUS_CHOICE, max_length=20, verbose_name="Father's Status")
    FatherAddress =  models.CharField(max_length=255, verbose_name="Father's Address", null=True, blank=True)
    FatherPhoneNumber =  models.CharField(max_length=255, verbose_name="Father's Phone Number", null=True, blank=True)
    FatherEmail =  models.EmailField(verbose_name="Father's Email", null=True, blank=True)
    FatherOccupation = models.CharField(max_length=255, verbose_name="Father's Occupation")
    MotherFullName = models.CharField(max_length=255, verbose_name="Mother Full Name")
    MotherStatus = models.CharField(choices=STATUS_CHOICE, max_length=20, verbose_name="Mother's Status")
    MotherAddress =  models.CharField(max_length=255, verbose_name="Mother's Address", null=True, blank=True)
    MotherPhoneNumber =  models.CharField(max_length=255, verbose_name="Mother's Phone Number", null=True, blank=True)
    MotherEmail =  models.EmailField(verbose_name="Mother's Email", null=True, blank=True)
    MotherOccupation = models.CharField(max_length=255, verbose_name="Mother's Occupation")