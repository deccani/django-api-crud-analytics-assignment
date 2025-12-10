from django.db import models

# For Storing the tasks created by users in Task Manager module
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=50, 
        choices=[("pending", "Pending"), ("completed", "Completed")],
        default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# For Storing the Economic Indicator Data imported from World Bank API
class IndicatorData(models.Model):
    country = models.CharField(max_length=10)
    country_name = models.CharField(max_length=255)
    indicator_code = models.CharField(max_length=50)
    indicator_name = models.CharField(max_length=255)
    year = models.IntegerField()
    value = models.FloatField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('country', 'indicator_code', 'year')

    def __str__(self):
        return self.title
