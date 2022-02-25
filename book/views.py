from django.shortcuts import render
from django.http import HttpResponse
from book.models import Publisher, Book, Store


# Create your views here.
def book(request):
    all_book = Book.objects.get(id=1).publisher.name
    print(all_book)

    # used for selec_related
    # queryset = Book.objects.select_related('publisher').all()  # one to many relation
    # for i in queryset:
    #     print(i.name)
    #     print(i.publisher.name)
    #     print(i.publisher.age)

    # used for prefetch related
    queryset = Store.objects.prefetch_related('book')
    for index in queryset:
        book_name = [b.name for b in index.book.all()]
        print("Name", index.name)
        print("Book", book_name)

    return HttpResponse("Hi")


def orm(request):
    queryset = Book.objects.filter(id=1)
    # print("My sql query", queryset.query)
    queryset = Book.objects.values_list('id', 'name')  # <class 'django.db.models.query.QuerySet'>

    # check datatype
    # print("Datatype", type(queryset))
    for index in queryset:
        print(index[1])

    queryset = Book.objects.all()

    print("Data type", queryset.query)

    return HttpResponse("Hi")

    # student_data = StudentDetails.objects.filter()
    # s_data = student_data.aggregate(Avg('marks'))
