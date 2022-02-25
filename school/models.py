from django.db import models
from product.models import Common


class School(Common):
    school_name = models.CharField(
        max_length=100,
        verbose_name='School Name')
    state = models.CharField(
        max_length=100,
        verbose_name='state')
    city = models.CharField(
        max_length=100,
        verbose_name='city')

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'School'

    def __str__(self):
        return self.school_name


class SchoolDetails(Common):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="SchoolDetails_school",
        null=True,
        blank=True,
        limit_choices_to={"active_status": "1"},
        verbose_name="School",
    )
    address = models.CharField(
        max_length=100,
        verbose_name='Student Name')
    no_of_teacher = models.CharField(
        max_length=100,
        verbose_name='No Of Teacher')

    class Meta:
        verbose_name = 'School Details'
        verbose_name_plural = 'School Details'

    def __str__(self):
        return self.address


class StudentDetails(models.Model):
    name = models.CharField(max_length=150)
    marks = models.PositiveIntegerField()

    def __str__(self):
        return self.name


# null=True,
# 	blank=True


class Author(models.Model):
    author_name = models.CharField(max_length=255, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.author_name


class Bookdetail(models.Model):
    BOOK_STATUS = (
        ('PUBLISHED', 'Published'),
        ('ON_HOLD', 'On Hold'),
    )
    book_name = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='author')
    status = models.CharField(max_length=255, choices=BOOK_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.book_name


class AuthorDetail(models.Model):
    author_name = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "AuthorDetail"
        verbose_name_plural = "AuthorDetail"

    def __str__(self):
        return self.author_name


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="Article_category", )
    published = models.BooleanField(default=False)
    read_min = models.IntegerField()

    def __str__(self):
        return self.title
