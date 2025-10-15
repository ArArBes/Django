from django.db import models
from dataclasses import field

class University(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name if len(self.name) < 15 else f"{self.name[:15]}..."


class Course(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title if len(self.title) < 15 else f"{self.title[:15]}..."


class UniversityCourse(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='university_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='university_courses')
    semester = models.CharField(max_length=50)
    duration_weeks = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['university', 'course', 'semester'],
                                    name='unique university course semester')
        ]
    def __str__(self):
        return f"{self.university.name}: {self.course.title} ({self.semester})"
