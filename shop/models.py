from django.db import models

# Create your models here.
class Products(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=20)
    desc=models.CharField(max_length=300)
    # category=models.CharField(max_length=50, default="")
    # publish_date=models.DateField()
    photo=models.ImageField(upload_to="images/", blank=True, null=True ,default="")

    def __str__(self):
        return self.product_name





# product_id=models.AutoField
#     product_name=models.CharField(max_length=20)
#     desc=models.CharField(max_length=300)
#     category=models.CharField(max_length=50, default="")
#     publish_date=models.DateField(default="")
#     photo=models.ImageField(upload_to="images/", blank=True, null=True ,default="")


