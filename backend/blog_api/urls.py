from django.urls import path,include
from .views import PostList,CreatePost,AdminPostDetail,DeletePost,EditPost
from rest_framework.routers import DefaultRouter 
app_name="blog_api"
#defaultrouter se tao url tu dong cho viewset nhu cac pt list retrieve delltee trong viewset
#tao  doi tg defaultrouter de thuc hien dinh dang url tu dong
#router=DefaultRouter()
#dang ki viewset muon tu dong url cho route
#tham so dau tien la tien to url
#basename la ten base co so cua url vs post/1
#router.register("",viewset=PostList,basename="post")
#dang ki mau url tu dong
router = DefaultRouter()
router.register('', PostList, basename='post')
urlpatterns = [
    path("",include(router.urls)),
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]



"""
urlpatterns = [
    #khi http yeu cau rel /n=so nguyen thi django se trich xuat dc so do va tra ve bien pk
path("<int:pk>/",PostDetail.as_view(),name="detailcreate"),
path("",PostList.as_view(),name="listcreate")
]"""