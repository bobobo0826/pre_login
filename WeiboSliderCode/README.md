# WeiboSliderCode
m.weibo.cn登录，四宫格图形解锁验证码破解

<br><br>
详情请见博客：[《图形解锁破解（附Python代码）》](http://blog.csdn.net/bone_ace/article/details/71056741)。
<br><br><br>
20170422更新：
<br>
据反映无法运行，我试了一下，发现selenium设置浏览器窗口大小，其截图的大小并不就是窗口大小，所以剪切下来的图片大小并不固定。图片切错了，自然也无法识别了。是我程序的疏忽，明晚或者后天抽空完善，抱歉！<br><br>
20170509更新：
<br>
即使设置了窗口大小，但实际截下来的图片，分辨率还是会根据所在的电脑环境变化。此次将代码改成尽量用相对坐标来定位图片，并且将像素判断的条件作了一些调整，减小误判概率。Windows和Linux大部分环境能通过，mac还未成功，暂时没有机器作测试，不知道具体问题出在哪里，mac环境后续再更新。
<br><br>
20170519更新：<br>
将登陆的URL改一下。<br>
原为https://passport.weibo.cn/signin/login?entry=mweibo&r=http://weibo.cn/；<br>
现为https://passport.weibo.cn/signin/login?entry=mweibo&r=https://weibo.cn/。<br>
如果重定向的地址是http，会无法跳转，导致登陆失败（其实已经登陆成功，只是重定向的地址无法打开）。<br><br>
