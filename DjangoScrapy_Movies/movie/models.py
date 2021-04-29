from django.db import models

class Movie(models.Model):
    title = models.CharField('Judul', max_length=255, unique=True)
    critics_consensus = models.TextField('Konsensus kritis', blank=True, null=True)
    average_grade = models.DecimalField('Nilai rata-rata', max_digits=3, decimal_places=2, blank=True, null=True)
    poster = models.ImageField('Cover', blank=True, null=True)
    amount_reviews = models.PositiveIntegerField('Jumlah ulasan', blank=True, null=True)
    approval_percentage = models.PositiveIntegerField('Persentase persetujuan', blank=True, null=True)

    def __str__(self):
        return self.title