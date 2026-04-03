import requests
from django.shortcuts import redirect
from django.http import HttpResponse
from django.conf import settings
from urllib.parse import urlencode
import json


def oauth_login(request):
    params = {
        'response_type': 'code',
        'client_id': settings.CLOUDREVE_CLIENT_ID,
        'redirect_uri': settings.CLOUDREVE_REDIRECT_URI,
        'scope': 'openid profile',
    }

    auth_url = f"{settings.CLOUDREVE_BASE_URL}/session/authorize?{urlencode(params)}"
    return redirect(auth_url)


def oauth_callback(request):
    code = request.GET.get('code')

    if not code:
        return HttpResponse("未收到授权码", status=400)

    # 用授权码换取access_token
    token_url = f"{settings.CLOUDREVE_BASE_URL}/api/v4/session/oauth/token"
    token_data = {
        'grant_type': 'authorization_code',
        'client_id': settings.CLOUDREVE_CLIENT_ID,
        'client_secret': settings.CLOUDREVE_CLIENT_SECRET,
        'code': code,
    }

    response = requests.post(token_url, data=token_data)

    if response.status_code != 200:
        return HttpResponse(f"获取token失败: {response.text}", status=400)

    token_info = response.json()
    access_token = token_info.get('access_token')

    # 获取用户信息
    userinfo_url = f"{settings.CLOUDREVE_BASE_URL}/api/v4/session/oauth/userinfo"
    user_response = requests.get(
        userinfo_url,
        headers={'Authorization': f'Bearer {access_token}'}
    )

    if user_response.status_code != 200:
        return HttpResponse(f"获取用户信息失败: {user_response.text}", status=400)

    user_info = user_response.json()

    # 直接展示用户信息
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>用户信息</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>第三方平台用户信息</h1>
        <pre>{json.dumps(user_info, ensure_ascii=False, indent=2)}</pre>
        <p><a href="/oauth/login/">重新登录</a></p>
    </body>
    </html>
    """

    return HttpResponse(html)