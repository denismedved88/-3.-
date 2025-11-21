import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
Password = os.getenv('Password')
Login = os.getenv('Login')

recipient_name ='Ivan'
sender_name='bi_bika'
website_url='https://dvmn.org/profession-ref-program/denismedved0409/bi_bika/'
sender_email='denismedved040969@yandex.ru'
recipient_email='denismedved0409@yandex.ru'

text="""From: {sender_email}
To: {recipient_email}
Subject: Invitation 
Content-Type: text/plain; charset="UTF-8"
Привет, {recipient_name}! {sender_name} приглашает тебя на сайт {website_url}!

{website_url} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website_url}?

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website_url}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(recipient_name=recipient_name, sender_name=sender_name, website_url=website_url, recipient_email=recipient_email,sender_email=sender_email)

text = text.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login (Login, Password)
server.sendmail(sender_email, recipient_email, text)  
server.quit()