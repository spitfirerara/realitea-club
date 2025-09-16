import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('ball', 'Ball'),
        ('accessory', 'Accessory'),
        ('other', 'Other'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)  # nama item
    price = models.IntegerField()            # harga item
    description = models.TextField()         # deskripsi item
    thumbnail = models.URLField()  # link gambar
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  # kategori
    is_featured = models.BooleanField(default=False)    # status unggulan
    stock = models.PositiveIntegerField(default=0)      # stok barang
    brand = models.CharField(max_length=50, blank=True, null=True)  # merek

    created_at = models.DateTimeField(auto_now_add=True)  # waktu dibuat
    updated_at = models.DateTimeField(auto_now=True)      # update terakhir
    
    def __str__(self):
        return f"{self.name} - Rp{self.price:,}"
