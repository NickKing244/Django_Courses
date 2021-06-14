from django.db import models

class CourseManager(models.Manager):
    def course_validator(self, post_data):
        errors = {}
        if len(post_data['name']) < 5:
            errors['name'] = "Name must be at least 5 characters long"
        if len(post_data['description']) < 15:
            errors['description'] = "Description must be at least 15 characters long"
        return errors

class Description(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.content}"

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description, related_name="course",null=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()