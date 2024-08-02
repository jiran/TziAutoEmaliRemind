# TziAutoEmaliRemind
使用Tzichecker测到卡时自动发送邮件提示

使用到的函数库os time requests json smtplib pyinstaller

这个程序将会在你测到卡的时候自动向你的邮箱发送提醒

邮件格式预览:

  你好像测到了Unban 5 张
  
  总共有Unban 5 张，21+ 2 张，rank 3 张，ban 4 张
  
  发送时间: 2024年8月2日16时34分23秒
  
使用前需点开程序更改smtp服务器以及端口 发送邮箱 邮箱授权码 目标邮箱

信息更改完毕后点击build.bat进行编译 双击点开程序即可运行

程序每隔5分钟检测一次 若没有测出卡不会发送邮件提示

