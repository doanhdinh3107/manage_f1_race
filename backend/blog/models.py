from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
#tao model category
class Category(models.Model):
    #cac thuoc tinh
    name=models.CharField(max_length=100)
    titles = models.CharField(max_length=300, default='Default Title')
    #ham nay de show gt ta muon hien thi de dai dien cho model trong bang admin
    def __str__(self):
        return self.name
#tao model post
class Post(models.Model):
    #day la khoa ngoai de model post co the tham chieu den model category on_delete de khi xoa 
    #category thi cung xoa het thang post lien quan
    # day la 1 tuple de hien thi gia tri lua chon cho truong charfirl gt dau la gia tri lua chon gt 2 la tham so hien thi
    #class nay dung de truy van cac onject  cu the
  #class nay dung de tao 1 custom manage cung cap cac phuong thuc truy van tuy chinh cho model
    class PostObjects(models.Manager):
        #co def getquery dung de tra ve doi tuong voi truy van cu the
        def get_queryset(self) :
            return super().get_queryset().filter(status="published")
    options=(
        ('draft','Draft'),
        ('published','Published')
    )
    category=models.ForeignKey(Category,on_delete=models.PROTECT,default=1)
    title=models.CharField(max_length=250)
    excerpt=models.TextField(null=True)
    content=models.TextField()
    slug=models.SlugField(max_length=250,unique_for_date='published')
    published=models.DateTimeField(default=timezone.now)
    #neu user bi xoa thi tat ca bai dang lien quan den nguoi dug do cung bi xoa
    #relate_name de truy van nguoc khi dung tu model user neu su dung user.blog_posts.all se tra ve tat ca post cua nguuoi dung do
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="blog_posts")    
    status=models.CharField(max_length=10,choices=options,default="published")
    #day la toan bo objects luon
    objects=models.Manager()
    postobjects=PostObjects()#custom object
    #class nay de hien thi cac ban ghi theo orderby
    class Meta:
        ordering=('-published',)
    def __str__(self):
        return self.title
        