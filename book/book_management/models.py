from django.db import models

NOVEL = "novel"
SCIENTIFIC = "scientific"
HISTORICAL = "historical"
TEXTBOOK = 'textbook'

CATEGORY_TYPE_CHOICES = (
    (NOVEL, "رمان"),
    (SCIENTIFIC, "علمی"),
    (HISTORICAL, "تاریخی‌"),
    (TEXTBOOK, "کتاب درسی")
)


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام کتاب')
    category = models.CharField(max_length=20, default=NOVEL, choices=CATEGORY_TYPE_CHOICES, verbose_name="نوع کتاب")
    author_name = models.CharField(max_length=50, verbose_name='نویسنده')
    price = models.BigIntegerField(default=10000, verbose_name='قیمت')
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="زمان ساخت"
    )

    modified = models.DateTimeField(
        auto_now=True,
        db_index=True,
        verbose_name="آخرین زمان تغییر"
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب‌‌ها'
