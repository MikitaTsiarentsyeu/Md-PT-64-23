from django.db import models

class Author(models.Model):

    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(primary_key=True)

class Post(models.Model):

    POST_TYPES = [('c', 'copyright'), ('p', 'public')]

    title = models.CharField(max_length=200)
    content = models.TextField()
    issued = models.DateTimeField()
    image = models.ImageField(upload_to="uploads")
    post_type = models.CharField(max_length=1, choices=POST_TYPES)

    author = models.ForeignKey('Author', on_delete=models.CASCADE)


# class User: pass

# class Item(models.Model):

#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField()
#     # category = models.CharField()
#     category = models.ForeignKey("Category", on_delete=models.DO_NOTHING)

# class Category(models.Model):

#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to="cat_images")

# class Basket:

#     items = {"item name": "item count"}