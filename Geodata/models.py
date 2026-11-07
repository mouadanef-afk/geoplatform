from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name="cities")
    population = models.PositiveIntegerField(null=True, blank=True)
    area_km2 = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "cities"

    def __str__(self):
        return self.name

    @property
    def density(self):
        if self.population is None:
            return None
        return round(self.population / self.area_km2)