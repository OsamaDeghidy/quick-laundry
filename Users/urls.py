from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
urlpatterns = [
 # urls.py


        path('signup/', views.signup, name='signup'),
        #path('profile/', views.profile, name='profile'),
      path('login/', CustomLoginView.as_view(), name='login'),



         path('logout/', auth_views.LogoutView.as_view(),name='logout'),


         path('change_password/', auth_views.PasswordChangeView.as_view(template_name='users/change_password.html'), name='change password'),
        path('change_password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/change_password_done.html'), name='password_change_done' ),

       
    path('delivery-agent-signup/', views.delivery_agent_signup, name='delivery_agent_signup'),
    path('available-orders/', views.available_orders, name='available_orders'),
    path('claim-order/<int:order_id>/', views.claim_order, name='claim_order'),
    path('personal-orders/', views.personal_orders, name='personal_orders'),
    path('add-notes/<int:order_id>/', views.add_notes, name='add_notes'),
    path('order-details/<int:order_id>/', views.order_details, name='order_details'),
]

