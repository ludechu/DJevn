from django.db import models

# Create your models here.
class apiManger(models.Manager):
    #自定义模型类,是公共的，其他模型类也可以引用
    def get_queryset(self):
        return super(apiManger,self).get_queryset().filter(status=True,is_deleted=False)

    def create_api(self,Name):
        # 定义一个方法，用于添加数据
        new_api = self.model(name=Name)
        return new_api

class t_api(models.Model):
    #一个模型类定义一个表
    #自定义模型管理器,后期对数据库操作时，将不是用student.objects.all,而是用student.stuObj.all
    apiQuery = apiManger()
    addapi = apiManger()
    apiQuery1 = models.Manager()
    name = models.CharField(max_length=20, verbose_name='接口名称')
    project_id = models.IntegerField(null=True,verbose_name='项目ID')
    tree = models.IntegerField(null=True,verbose_name='树节点id')
    des = models.TextField(null=True, verbose_name='描述')
    method = models.IntegerField(null=True,verbose_name='请求方式')
    evn_id = models.IntegerField(null=True,verbose_name='环境id')
    url = models.CharField(null=True,max_length=60, verbose_name='接口url')
    para_list = models.TextField(null=True, verbose_name='参数列表')
    creater = models.CharField(null=True,max_length=10, verbose_name='创建人')
    create_time = models.DateField(auto_now_add=True, verbose_name='创建时间')
    last_modify_time = models.DateField(auto_now=True, verbose_name='最近修改时间')
    status = models.BooleanField(default=True, verbose_name='是否启用')
    is_deleted = models.BooleanField(default=False, verbose_name='是否删除')

    def __str__(self):
        return self.name
    class Meta:
        #定义元选项
        #定义数据表名，因为模型创建出来的表包含项目名+表名，不好使
        db_table = "t_api"
        #对象的默认排序字段，获取对象的列表时使用,默认升序，排序会增加数据库开销
        ordering = ['id']
        # ordering = ['-id']#降序






