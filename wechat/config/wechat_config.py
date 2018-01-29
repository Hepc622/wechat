"""----------------------------基本信息-----------------------------"""
# 微信公众号id
app_id = 'wx3d4424c7b7f0682f'
# 微信secret
app_secret = 'ba79850f0bb2f10f2e93836ed629c3a4'
# url
app_url = 'http://hpc.4kb.cn/'
# 获取服务器ip
server_ip_url = 'https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token=%s'
"""----------------------------请求url-----------------------------"""
# 获取access_token的链接
access_token_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'
# 创建菜单的url,post方式
create_menu_url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s'
# 查询菜单的url
query_menu_url = 'https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s'
# 删除菜单的ul
delete_menu_url = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s'
