from functools import wraps
from django.shortcuts import redirect


def login_auth(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        target_url = request.get_full_path()    # 获取用户想要访问的url
        if request.session.get('login_auth_key'):
            res = func(request, *args, **kwargs)
            return res
        else:
            return redirect(f'/login/?next={target_url}')   # 设置登录后跳转的页面url
    return inner

