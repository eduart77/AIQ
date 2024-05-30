from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age_number = models.IntegerField()
    interest_points = models.TextField()
    personality = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    subdomain = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


DEFAULT_PERSON_ID = 1  # Update this with the correct ID after creating the default Person record


class Response(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, default=DEFAULT_PERSON_ID)
    response_1_text = models.TextField()
    response_2_text = models.TextField()
    iteration_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Response {self.iteration_id}"


class FinalWordList(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    word = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)

    def __str__(self):
        return self.word
