# 各网站登录：不完善，还有bug
## 微博登录
   1、微博预登陆，登录网页版微博：sina_login_direct
   
   2、微博模拟登陆，从手机端页面（wap站）登录微博，破解图形验证码，
      获取cookie：WeiboSliderCode
      
   
## 企查查登录
   1、设置headers和cookie，用request直接以登录的身份跳转详情页面：login3.py
   
   2、在webdriver中塞入cookie值跳转详情页面：cookies.py
   
   3、在企查查登录页面利用selenium webdriver自动填入用户名密码，
      设置滑动滑块，但是必须手动解决验证码：login2.py
      
 ## 百度搜索：
   headless模式运行,实现百度搜索：headless_baidu.py
