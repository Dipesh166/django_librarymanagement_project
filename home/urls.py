from django.urls import path
from .views import CreateUserView, ListAllUsersView, GetUserByIdView
from .views import AddNewBookView, ListAllBooksView, GetBookByIdView, AssignUpdateBookDetailsView
from .views import BorrowBookView, ReturnBookView, ListAllBorrowedBooksView



urlpatterns = [

    
    # User APIs
    path('users/create/', CreateUserView.as_view(), name='create_user'),
    path('users/list/', ListAllUsersView.as_view(), name='list_all_users'),
    path('users/<int:UserID>/', GetUserByIdView.as_view(), name='get_user_by_id'),

    # Book APIs
    path('books/add/', AddNewBookView.as_view(), name='add_new_book'),
    path('books/list/', ListAllBooksView.as_view(), name='list_all_books'),
    path('books/<int:BookID>/', GetBookByIdView.as_view(), name='get_book_by_id'),
    path('books/details/<int:BookID>/', AssignUpdateBookDetailsView.as_view(), name='assign_update_book_details'),

    # BorrowedBooks APIs
    path('borrow/', BorrowBookView.as_view(), name='borrow_book'),
    path('return/<int:id>/', ReturnBookView.as_view(), name='return_book'),
    path('borrowed/list/', ListAllBorrowedBooksView.as_view(), name='list_all_borrowed_books'),
]