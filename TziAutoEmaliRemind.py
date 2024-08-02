import os
import time
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def get_status(url):
    response = requests.get(url)
    return response.json()['data']

def send_email(subject, body, to_email):
    from_email = "替换发送邮箱"
    password = "替换授权码"
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('替换smtp服务器', 替换端口) as server:
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
        print("发送成功")
    except Exception as e:
        print(f"发送失败: {e}")

def format_time():
    return datetime.now().strftime("%Y年%m月%d日%H时%M分%S秒")

def main():
    QQ = input("输入QQ：")
    url = f"http://api.tzick.club/Api?QQ={QQ}"
    os.system(f"title QQ: {QQ}")

    previous_status = None
    to_email = "替换发送目标邮箱"

    while True:
        status = get_status(url)
        os.system('cls')

        current_status = {
            'Minecraft_Unban': int(status['Minecraft_Unban']),
            'Minecraft_Hypixel_Level_21': int(status['Minecraft_Hypixel_Level_21']),
            'Minecraft_Hypixel_Rank': int(status['Minecraft_Hypixel_Rank']),
            'Minecraft_Banned': int(status['Minecraft_Banned'])
        }

        if previous_status:
            email_body = ""
            for key in current_status:
                if previous_status[key] + 1 == current_status[key]:
                    label = key.replace('Minecraft_', '').replace('_', ' ')
                    email_body += f"你好像测到了{label} {current_status[key]} 张\n"

            if email_body:
                email_body += f"\n总共有Unban {current_status['Minecraft_Unban']} 张，21+ {current_status['Minecraft_Hypixel_Level_21']} 张，rank {current_status['Minecraft_Hypixel_Rank']} 张，ban {current_status['Minecraft_Banned']} 张\n"
                email_body += f"发送时间: {format_time()}"
                send_email("主播你又测到卡了", email_body, to_email)

        print(f"HypixelUnban有: {current_status['Minecraft_Unban']} 张")
        print(f"21+的卡有: {current_status['Minecraft_Hypixel_Level_21']} 张")
        print(f"Rank有: {current_status['Minecraft_Hypixel_Rank']} 张")
        print(f"Banned有: {current_status['Minecraft_Banned']} 张")

        previous_status = current_status
        time.sleep(300)

if __name__ == "__main__":
    main()
