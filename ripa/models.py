from django.db import models

# Create your models here.
class VersionUnderTest(models.Model):
    version = models.CharField(max_length=10)

    def __str__(self):
        return self.version


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=10000, blank=True, default="")
    datetime_started = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Release(models.Model):
    name = models.CharField(max_length=10)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None)
    is_released = models.BooleanField()

    def __str__(self):
        return self.name


class Issue(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=10000, blank=True, default="")
    associated_project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None)
    associated_release = models.ForeignKey(Release, on_delete=models.CASCADE, null=True, default=None)

    status_choices = (
        ("NE", "New"),
        ("OP", "Open"),
        ("CL", "Closed"),
        ("IP", "In Progress"),
        ("IT", "In Testing")
    )

    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default="NE"
    )

    datetime_opened = models.DateTimeField(auto_now_add=True)
    datetime_last_modified = models.DateTimeField(auto_now=True)
    datetime_closed = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(
        max_length=20,
        choices=(
            ("HT", "Highest"),
            ("HR", "Higher"),
            ("NO", "Normal"),
            ("LR", "Lower"),
            ("LT", "Lowest")
        ),
        default="NO"
    )

    def __str__(self):
        return self.title


class Defect(Issue):
    escaped = models.CharField(
        max_length=4,
        choices=(
            ("Y", "Yes"),
            ("N", "No"),
        ),
        default="N"
    )

    def __str__(self):
        return self.title


class Feature(Issue):
    def __str__(self):
        return self.title


class RFC(Issue):
    def __str__(self):
        return self.title

