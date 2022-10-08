from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app1.models import BookInfo
from app1.models import MemberInfo
from django.db.models import F, Q
from django.db.models import Sum  # , Min, Max, Avg, Count
from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import redirect
import json
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

def testing_render(request):
    # context: 在模板里传值
    context = {
        'name': 'alice'
    }

    return render(request, template_name='app1/index.html', context=context)


def testing_response(request):
    return HttpResponse('index')


@csrf_exempt
def testing_json(request):
    if request.method == 'POST':
        data_str = request.body.decode()
        data = json.loads(data_str)
        print(data.get('name'))
    return HttpResponse('index')


def index(request):
    msg = {'code': None, 'status': False, 'msg': None}
    if request.method == 'GET':
        book_info_datas = BookInfo.objects.all()

        context = {
            'book_info_datas': book_info_datas
        }
        msg.update(code=200, status=True, msg='successful')
        # return JsonResponse(data=msg)
        # return redirect(to=reverse(viewname='query_member_info'))
        return render(request, template_name='app1/index.html', context=context)


def jump_page_testing(request):
    """
    页面跳转
    """
    # redirect 方法来跳转页面
    # reverse 方法来动态获取 指定urls中name参数
    return redirect(to=reverse('app1: query_member_info'))


@csrf_exempt
def add_book_info(request):
    """
    添加书籍信息
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        pub_date = request.POST.get('pub_date')

        # 方法一
        # book = BookInfo(
        #     name=name,
        #     pub_date=pub_date,
        # )
        # book.save()

        # 方法二
        BookInfo.objects.create(name=name, pub_date=pub_date)

        return JsonResponse(data={'code': 200, 'status': 'True', 'data': f'添加{name}成功'}, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse(data={'code': 500, 'status': 'False', 'data': f'请求方法错误'}, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def update_book_info(request):
    """
    更新书籍信息
    """
    if request.method == 'POST':
        book_name = request.POST.get('name')
        update_name = request.POST.get('update_name')
        try:
            # 使用objects.get(key=value), 如果存在返回BookInfo对象, 不存在则跳出; 报错: BookInfo matching query does not exist.
            data_book = BookInfo.objects.get(name=book_name)
            if data_book.name == book_name:
                # 方法一
                data_book.name = update_name
                data_book.save()

                # 方法二
                BookInfo.objects.filter(name__exact=book_name).update(name=update_name)
                return JsonResponse(data={'code': 200, 'status': True, 'data': f'修改{book_name}为{update_name}'},
                                    json_dumps_params={'ensure_ascii': False})
            else:
                return JsonResponse(data={'code': 500, 'status': False, 'data': f'未查询到{book_name}'}, json_dumps_params={'ensure_ascii': False})
        except Exception as error:
            print(error)
            return JsonResponse(data={'code': 500, 'status': False, 'data': f'未查询到{book_name}'}, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse(data={'code': 500, 'status': False, 'data': f'请求方法错误'}, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def del_book_info(request):
    """
    删除书籍信息(真实删除数据)
    """
    if request.method == 'POST':
        book_name = request.POST.get('name')
        try:
            data_book = BookInfo.objects.get(name=book_name)
            if data_book.name == book_name:
                data_book.delete()
                return JsonResponse(data={'code': 200, 'status': True, 'data': f'删除{book_name}成功'}, json_dumps_params={'ensure_ascii': False})
            else:
                return JsonResponse(data={'code': 500, 'status': False, 'data': f'未查询到{book_name}'}, json_dumps_params={'ensure_ascii': False})
        except Exception as error:
            print(error)
            return JsonResponse(data={'code': 500, 'status': False, 'data': f'未查询到{book_name}'}, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse(data={'code': 500, 'status': False, 'data': f'请求方法错误'}, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def is_del_book_info(request):
    """
    逻辑删除书籍信息
    """
    if request.method == 'POST':
        book_name = request.POST.get('name')
        try:
            data_book = BookInfo.objects.get(name=book_name)
            if data_book.name == book_name:
                BookInfo.objects.filter(name__exact=book_name).update(is_deleted=1)
                return JsonResponse(data={'code': 200, 'status': True, 'data': f'逻辑删除{book_name}成功'}, json_dumps_params={'ensure_ascii': False})
            else:
                return JsonResponse(data={'code': 500, 'status': False, 'data': f'未查询到{book_name}'}, json_dumps_params={'ensure_ascii': False})
        except Exception as error:
            print(error)
            return JsonResponse(data={'code': 500, 'status': False, 'data': f'未查询到{book_name}'}, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse(data={'code': 500, 'status': False, 'data': f'请求方法错误'}, json_dumps_params={'ensure_ascii': False})


def query_book_info_testing(request):
    """
    查询书籍信息
    """
    # get()  只查询一条数据; 返回BookInfo对象, -> objects 利用 .字段名来获取字段信息; 不存在则抛出异常 报错: matching query does not exist.
    BookInfo.objects.get(id=1)
    # all()  查询所有数据; 返回QuerySet集合对象, -> list 可以用for来遍历, 返回BookInfo对象 -> objects
    BookInfo.objects.all()
    # count()  数量查询, 返回数据表中有多少行数据, -> int
    # BookInfo.objects.all().count()
    BookInfo.objects.count()

    # filter, get, exclude 相当于mysql中的where查询
    """
    filter: 筛选/过滤, 返回n个结果(n>=0)
    get: 筛选/过滤, 返回一个结果
    exclude: 排除筛选/过滤, 返回n个结果(n>=0)
    """
    # 查询ID等于1的书籍信息
    BookInfo.objects.get(id__exact=1)
    # 查询书名包含'湖'的图书
    BookInfo.objects.filter(name__contains='湖')
    # 查询以'部'结尾的书籍
    BookInfo.objects.filter(name__endswith='部')
    # 查询书名为空的图书
    BookInfo.objects.filter(name__isnull=True)
    # 查询ID为1或3或5的图书
    BookInfo.objects.filter(id__in=[1, 3, 5])
    # 查询ID大于3的图书
    BookInfo.objects.filter(id__gt=3)
    # 查询ID不等于3的图书
    BookInfo.objects.exclude(id__exact=3)
    # 查询1980年出版的图书
    BookInfo.objects.filter(pub_date__year=1980)
    # 查询1990年1月1日后发布的图书
    BookInfo.objects.filter(pub_date__gt='1990-01-01')

    # F, Q 对象
    # from django.db.models import F, Q
    """
    F: 字段和字段比较
    Q: 或者, Q() | Q() ... | Q(); 并且, Q() & Q() ... & Q()
    ~Q: 表示not, ~Q()
    """
    # F
    # 阅读量大于评论量的书籍
    BookInfo.objects.filter(read_count__gt=F('comment_count'))
    # 阅读量大于2倍评论量的书籍
    BookInfo.objects.filter(read_count__gt=F('comment_count') * 2)
    # Q
    # ID大于2并且阅读量大于20的书籍; and
    BookInfo.objects.filter(id__gt=2, read_count__gt=20)
    # ID大于2或阅读量大于20的书籍; or
    BookInfo.objects.filter(Q(id__gt=2) | Q(read_count__gt=20))
    # 查询ID不等于3的图书
    BookInfo.objects.exclude(id__exact=3)
    BookInfo.objects.filter(~Q(id__exact=3))

    # 聚合函数, 需要调用objects.aggregate()方法; objects.aggregate()返回key=字段名__聚合函数名,value=value的一个字典 -> dict
    # from django.db.models import Sum, Min, Max, Avg, Count
    """
    sum: objects.aggregate(Sum())
    max: objects.aggregate(Max())
    min: objects.aggregate(Min())
    avg: objects.aggregate(Avg())
    count: objects.aggregate(Count())
    """
    BookInfo.objects.aggregate(Sum('read_count'))

    # 排序 objects.filter().order_by(''), 或者 objects.all().order_by(''), 由低到高(默认升序) -> list
    # 阅读量按照升序排序
    BookInfo.objects.all().order_by('read_count')
    # 阅读量按照降序排序
    BookInfo.objects.all().order_by('-read_count')

    # 关联查询
    # 已知书籍名称查询人物信息 BookInfo.objects.get(name__exact='天龙八部').memberinfo_set.all()
    book1 = BookInfo.objects.get(name__exact='天龙八部')
    book1.memberinfo_set.all()
    # 已知人物信息查询书籍信息 MemberInfo.objects.get(name__exact='黄蓉').book.name
    # member_info1 = MemberInfo.objects.get(name__exact='黄蓉')
    # var = member_info1.book.name
    # print(var)
    # 关联查询的筛选
    # 已知人物信息, 查询书籍
    BookInfo.objects.filter(memberinfo__name__exact='黄蓉')
    BookInfo.objects.filter(memberinfo__description__contains='掌')
    # 已知书籍信息, 查询人物
    MemberInfo.objects.filter(book__name__exact='天龙八部')
    MemberInfo.objects.filter(book__read_count__gte=20)

    # 查询集


@csrf_exempt
def query_book_info(request):
    """
    查询书籍
    """
    data_json_return = {
        'code': 500,
        'status': False,
        'data': None
    }
    if request.method == 'GET':
        data_json_books = {}
        data_books = BookInfo.objects.filter(is_deleted__exact=0)
        for book_data_index, book_data in enumerate(data_books):
            data_json_book = {
                'id': book_data.id,
                'name': book_data.name,
                'read_count': book_data.read_count,
                'comment_count': book_data.comment_count
            }
            data_json_books.update({book_data_index: data_json_book})
        data_json_return.update(code=200, status=True, data=data_json_books)
        return JsonResponse(data=data_json_return, json_dumps_params={'ensure_ascii': False})
    elif request.method == 'POST':
        book_id = int(request.POST.get('id'))
        book_name = request.POST.get('name')
        if book_name == '':
            book_name = None
        if book_name is not None:
            try:
                book_data = BookInfo.objects.get(name__exact=book_name)
                data_json_book = {
                    'id': book_data.id,
                    'name': book_data.name
                }
                data_json_return.update(data=data_json_book)
                return JsonResponse(data=data_json_return, json_dumps_params={'ensure_ascii': False})
            except Exception as error:
                print(error)
                data_json_return.update(data=f'未查询到{book_name}')
                return JsonResponse(data=data_json_return, json_dumps_params={'ensure_ascii': False})
        else:
            if book_id is not None:
                try:
                    data_book = BookInfo.objects.get(id__exact=book_id)
                    data_json_book = {
                        'id': data_book.id,
                        'name': data_book.name,
                        'read_count': data_book.read_count,
                        'comment_count': data_book.comment_count
                    }
                    data_json_return.update(data=data_json_book)
                    return JsonResponse(data=data_json_return, json_dumps_params={'ensure_ascii': False})
                except Exception as error:
                    print(error)
                    data_json_return.update(data=f'未查询到ID为{book_id}的书籍')
                    return JsonResponse(data=data_json_return, json_dumps_params={'ensure_ascii': False})
            else:
                data_json_return.update(data='请传入字段数据')
                return JsonResponse(data=data_json_return, json_dumps_params={'ensure_ascii': False})
    else:
        data_json_return.update(data='请求方法错误')
        return JsonResponse(data=data_json_return, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def query_member_info(request):
    """
    成员信息查询
    """
    data_json_return = {
        'code': 500,
        'status': False,
        'data': None
    }
    if request.method == 'GET':
        data_json_members = {}
        data_members = MemberInfo.objects.all()
        page = Paginator(data_members, 10)
        for data_member_index, data_member in enumerate(page.page(1)):
            member_info = {
                'id': data_member.id,
                'name': data_member.name,
                'gender': data_member.gender,
                'description': data_member.description,
                'book': BookInfo.objects.get(memberinfo__id__exact=data_member.id).name,
            }
            if member_info.get('gender') == 0:
                member_info.update(gender='男')
            elif member_info.get('gender') == 1:
                member_info.update(gender='女')
            data_json_member = {data_member_index: member_info}
            data_json_members.update(data_json_member)
        data_json_return.update(code=200, status=True, data=data_json_members)
        return JsonResponse(data=data_json_return, json_dumps_params={'ensure_ascii': False})
    else:
        data_json_return.update(data='请求方法错误')
        return JsonResponse(data=data_json_return, json_dumps_params={'ensure_ascii': False})


def book_info_get(request):
    data_json_return = {
        'code': 500,
        'status': False,
        'data': None
    }
    book_id = request.GET.get('id')
    try:
        data_book = BookInfo.objects.get(id__exact=book_id)
        data_json_book = {
            'id': data_book.id,
            'name': data_book.name,
            'read_count': data_book.read_count,
            'comment_count': data_book.comment_count
        }
        data_json_return.update(code=200, status=True, data=data_json_book)
        return JsonResponse(data=data_json_return, json_dumps_params={'ensure_ascii': False})
    except Exception as error:
        print(error)
        data_json_return.update(data=f'未查询到ID为{book_id}的书籍')
        return JsonResponse(data=data_json_return, json_dumps_params={'ensure_ascii': False})


class CenterView(LoginRequiredMixin, View):
    """
    个人中心
    """
    
    @staticmethod
    def get(request):
        return HttpResponse('个人中心展示')

    @staticmethod
    def post(request):
        return HttpResponse('个人信息修改')





