from django.shortcuts import render
from .models import User
from django.views import generic


def index(request):
    num_users = User.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_users': num_users}
    )


# def user_detail_view(request, pk):
#     try:
#         user_id = User.objects.get(pk=pk)
#         print(user_id)
#     except User.DoesNotExist:
#         raise Http404("User with such id does not exist")
#
#     # book_id=get_object_or_404(Book, pk=pk)
#
#     return render(
#         request,
#         'index.html',
#         context={'user': user_id, }
#     )

class UserListView(generic.ListView):
    model = User


class UserDetailView(generic.DetailView):
    model = User
