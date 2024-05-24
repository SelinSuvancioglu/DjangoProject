from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class AbstractModel(models.Model):
    updated_at = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name="Updated Date"
    )

    created_at = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name="Created Date"
    )

    class Meta:
        abstract = True


class GeneralSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Name"

    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Description"
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Parameter"

    )

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)


class Skills(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name="Order",
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Name",
        help_text="This is variable of the settings"
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name="Percentage",
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return f'Skill: {self.name}'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ('order',)


class Experience(AbstractModel):
    JobTitle = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Job Title"
    )
    JobDetail = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Detail"
    )
    Company = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Company"
    )

    Location = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Location"
    )

    StartDate = models.DateField(
        verbose_name='Start Date',
    )
    EndDate = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name="End date",
    )

    def __str__(self):
        return f'{self.Company}'

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ('-StartDate',)

class Education(AbstractModel):
    School = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="School"
    )
    Degree = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Degree"
    )
    Department = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Department"
    )
    GNO = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="GNO"
    )
    StartDate = models.DateField(
        verbose_name='Start Date',
    )
    EndDate = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name="End date",
    )

    def __str__(self):
        return f'{self.School}'

    class Meta:
        verbose_name = 'education'
        verbose_name_plural = 'educations'
        ordering = ('-StartDate',)

class Documentation(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name="Order"
    )
    slug = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Slug",
        help_text='',
    )
    button_text = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Button Text"
    )
    file = models.FileField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="File",
        upload_to='documents/',
    )

    def __str__(self):
        return f'{self.slug}'
    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ('order',)