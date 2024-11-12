from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/categories', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        # return f"/store/{self.slug}/"  -> this is static method which is not recommended
        # return reverse('products_by_category', args=[self.slug]) -> either this one or the below is recommended as there are dynamic. this method passes argumment by position where as the below one is based on keywords
        return reverse('products_by_category', kwargs={"category_slug":self.slug})

    def __str__(self):
        return self.name
