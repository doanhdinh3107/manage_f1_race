from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
#base de custom quyen tuy chinh
from rest_framework.permissions import SAFE_METHODS, BasePermission,IsAdminUser,DjangoModelPermissionsOrAnonReadOnly
#lop  nay dung de xu ly yeu cau get va post lien quan den 1 tap hop cac object
#serilizer dung de chuyen doi doi tuong object thah kei dy lieu json tg ung
"""
class PostUserWritePermission(BasePermission):
    #obj la doi tuong ma permision dang kiem tra tren do
    #neu khong qo quyen se in ra mess
    message='u dont have permissions'
    #lop nay tao ham permission tuy chinh tham so obj la doi tg goi den no
    def has_object_permission(self, request, view, obj):
        #neu la cac phuon thuc an toan
        if request.method in SAFE_METHODS:
            return True
        return obj.author==request.user

class PostList(viewsets.ModelViewSet):
     serializer_class=PostSerializer
     #ta co the ghi de cac ham co san cua model viewset de thuc hien cac tac vu
     #ghi de phuong thuc list object
     def get_queryset(self):
         return Post.objects.all()
     #ghi de phuong phuc retieve tung bai dang thong qua slug
     def get_object(self,queryset=None,**kwargs):
            #tham so kwargs la 1 tu dien chua cac tham so truyen vao tu url 
            #ta co the su dung no de loc cac object tuong ung
            item=self.kwargs.get("pk")
            return get_object_or_404(Post,slug=item)
   """

class PostList(viewsets.ModelViewSet):

    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)
    # Define Custom Queryset
    def get_queryset(self):
        return Post.objects.all()

#tao cac che do view cho admin de crud
#phuong thuc nay dc su dung de tao bai dang moi tu phuong thuc post
class CreatePost(generics.CreateAPIView):
    #day la tap hop cac object ban dau
    queryset=Post.objects.all()
    serializer_class=PostSerializer


class AdminPostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EditPost(generics.UpdateAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

class DeletePost(generics.RetrieveDestroyAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
""""
    #viewset lam ma de quan ly hon va viet ngan gon hon thay vi  phai tao 2 class cho líst va ca nhan
class PostList(viewsets.ViewSet):
    #dau tien can dinh nghia quyen cho class va du lieu cua class

    queryset=Post.postobjects.all()
    #tao 1 list chua tat ca cac post
    def list(self,request):
        #chuyen du lieu queryset chứa danh sách post thành json many=true cho phép truyền líst objects
        serializer_class=PostSerializer(self.queryset,many=True)
        return Response(serializer_class.data)
    #ham retrieve de truy xuat doi tuong cu the thong qua khoa ngoai
    def retrieve(self,request,pk=None):
        #loc ra doi tuong cu the bang ham get_object_404
        post=get_object_or_404(self.queryset,pk=pk)
        #chuyen du lieu snag json
        serializel_class=PostSerializer(post)
        return Response(serializel_class.data)"""