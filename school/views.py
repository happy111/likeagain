from django.shortcuts import render
from django.http import HttpResponse
from school.models import *
from django.db.models import Count, Sum, Max, Avg, Case, When, Value, IntegerField, BooleanField


# Create your views here.
# aggregate() is a clause , collection of object
# annotate used for groupby

def home(request):
    student_data = StudentDetails.objects.filter()
    s_data_avg = student_data.aggregate(Avg('marks'))
    s_data_sum = student_data.aggregate(Sum('marks'))

    book_data = Bookdetail.objects.values('author').annotate(num_books=Count('book_name'))

    # <QuerySet [{'author': 2, 'num_books': 2}, {'author': 1, 'num_books': 2}]>

    # SELECT "school_bookdetail"."author_id", COUNT("school_bookdetail"."book_name")
    # AS "num_books" FROM "school_bookdetail" GROUP BY "school_bookdetail"."author_id"

    # book_data = Bookdetail.objects.values('author')

    print("eeeeeeeeeeeeeeeeee", book_data)
    return HttpResponse("School here")
