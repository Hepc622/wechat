"""----------------------------基本信息-----------------------------"""
# 微信公众号id
app_id = 'wx3d4424c7b7f0682f'
# 微信secret
app_secret = 'ba79850f0bb2f10f2e93836ed629c3a4'
# url
app_url = 'http://hpc.4kb.cn/'
# 获取服务器ip
server_ip_url = 'https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token=%s'
"""----------------------------menu操作url-----------------------------"""
# 获取access_token的链接
access_token_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'
# 创建菜单的url,post方式
create_menu_url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s'
# 查询菜单的url
query_menu_url = 'https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s'
# 删除菜单的ul
delete_menu_url = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s'
"""----------------------------回复消息XML-----------------------------"""
# 文本消息
text_content = '<xml>' \
               '    <ToUserName><![CDATA[%s]]></ToUserName>' \
               '    <FromUserName><![CDATA[%s] ]></FromUserName>' \
               '    <CreateTime>%s</CreateTime>' \
               '    <MsgType><![CDATA[text]]></MsgType>' \
               '    <Content><![CDATA[%s]]></Content>' \
               '</xml>'
# 图片消息
img_content = '<xml>' \
               '    <ToUserName><![CDATA[%s]]></ToUserName>' \
               '    <FromUserName><![CDATA[%s] ]></FromUserName>' \
               '    <CreateTime>%s</CreateTime>' \
               '    <MsgType><![CDATA[image]]></MsgType>' \
              '     <Image><MediaId><![CDATA[%s]]></MediaId></Image>' \
              '</xml>'
# 语音消息
voice_content = '<xml>' \
              '    <ToUserName><![CDATA[%s]]></ToUserName>' \
              '    <FromUserName><![CDATA[%s] ]></FromUserName>' \
              '    <CreateTime>%s</CreateTime>' \
              '    <MsgType><![CDATA[voice]]></MsgType>' \
              '    <Voice><MediaId><![CDATA[%s]]></MediaId></Voice>' \
              '</xml>'
# 视频消息
voice_content = '<xml>' \
                '    <ToUserName><![CDATA[%s]]></ToUserName>' \
                '    <FromUserName><![CDATA[%s] ]></FromUserName>' \
                '    <CreateTime>%s</CreateTime>' \
                '    <MsgType><![CDATA[video]]></MsgType>' \
                '    <Video>' \
                '       <MediaId><![CDATA[%s]]></MediaId>' \
                '       <Title><![CDATA[%s]]></Title>' \
                '       <Description><![CDATA[%s]]></Description>' \
                '    </Video>' \
                '</xml>'
# 音乐消息
music_content = '<xml>' \
                '    <ToUserName><![CDATA[%s]]></ToUserName>' \
                '    <FromUserName><![CDATA[%s] ]></FromUserName>' \
                '    <CreateTime>%s</CreateTime>' \
                '    <MsgType><![CDATA[music]]></MsgType>' \
                '    <Music>' \
                '       <Title><![CDATA[%s]]></Title>' \
                '       <Description><![CDATA[%s]]></Description>' \
                '       <MusicUrl><![CDATA[%s]]></MusicUrl>' \
                '       <HQMusicUrl><![CDATA[%s]]></HQMusicUrl>' \
                '       <ThumbMediaId><![CDATA[%s]]></ThumbMediaId>' \
                '   </Music>'\
                '</xml>'
# 图文消息
news_content = '<xml>' \
                '    <ToUserName><![CDATA[%s]]></ToUserName>' \
                '    <FromUserName><![CDATA[%s] ]></FromUserName>' \
                '    <CreateTime>%s</CreateTime>' \
                '    <MsgType><![CDATA[news]]></MsgType>' \
                '    <ArticleCount>2</ArticleCount>' \
                '    <Articles>' \
                '       <item>' \
                '           <Title><![CDATA[%s]]></Title>' \
                '           <Description><![CDATA[%s]]></Description>' \
                '           <PicUrl><![CDATA[%s]]></PicUrl>' \
                '           <Url><![CDATA[%s]]></Url>' \
                '       </item>' \
                '   </Articles>' \
                '</xml>'
"""----------------------------模板消息接口-----------------------------"""
# 设置所属行业 post
add_industry_url = 'https://api.weixin.qq.com/cgi-bin/template/api_set_industry?access_token=$s'
# 获取行业信息
get_industry_url = 'https://api.weixin.qq.com/cgi-bin/template/get_industry?access_token=%s'
# 获取模板id post
get_template_id_url = 'https://api.weixin.qq.com/cgi-bin/template/api_add_template?access_token=%'
# 获取模板list
get_template_list_url = 'https://api.weixin.qq.com/cgi-bin/template/get_all_private_template?access_token=%s'
# 删除模板 post
delete_template_url = 'https://api.weixin.qq.com/cgi-bin/template/del_private_template?access_token=%s'
# 发送模板 post
''' 发送成功，微信服务器会向我们配置的url发送下面信息表示成功
    <xml>
       <ToUserName>< ![CDATA[gh_7f083739789a] ]></ToUserName>
       <FromUserName>< ![CDATA[oia2TjuEGTNoeX76QEjQNrcURxG8] ]></FromUserName>
       <CreateTime>1395658920</CreateTime>
       <MsgType>< ![CDATA[event] ]></MsgType>
       <Event>< ![CDATA[TEMPLATESENDJOBFINISH] ]></Event>
       <MsgID>200163836</MsgID>
       <Status>< ![CDATA[success] ]></Status>
   </xml>
'''
send_template_url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s'

