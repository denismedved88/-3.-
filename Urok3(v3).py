import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
email_password = os.getenv('password')
email_login = os.getenv('email')
friend_name ='Ivan'
my_name='bi_bika'
website_url='https://dvmn.org/profession-ref-program/denismedved0409/bi_bika/'

email_text=("""From: denismedved040969@yandex.ru
To: denismedved0409@yandex.ru
Subject: Invitation 
Content-Type: text/plain; charset="UTF-8
Привет, {friendname}! {myname} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}?

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""").format(friendname=friendname, myname=myname, website=website)

text = text.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login (login, password)
server.sendmail('denismedved040969@yandex.ru', 'denismedved0409@yandex.ru', text)  
server.quit()