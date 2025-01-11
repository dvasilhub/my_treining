# Домашнее задание по теме "Обзор сторонних библиотек Python"

            # 1. Библиотека Requests:
import requests

# Отправление GET-запроса на API:
r = requests.get('https://api.github.com')

# Получение ответов в виде словаря
rj = r.json()
print(rj)

# Получение значения, путём обращения к конкретному ключу:
print(f'Значение: {rj['keys_url']}')

# Получение заголовков запросов:
print(r.request.headers)

# Отправление POST-запроса:
r = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(r.text)

# Скачивание и сохранение файла (изображения)
img_url = 'https://sun9-68.userapi.com/s/v1/ig2/IalNEc1QtDe0sSSWEIJY2DAi5uYPiVwFewlER5y236NV7fYTEQgL8PJ9QGHPq-40GE7b1rMVHUKWZ1BgfIuNEutP.jpg?quality=95&as=32x32,48x48,72x72,108x108,160x160,240x240,360x360,480x480,540x540,640x640,720x720,1080x1080&from=bu&u=L_eXtu8-u7SLUv0nZawRteZ8ILByxSi2tyr0p8Yyq-k&cs=807x807'
r = requests.get(img_url)
with open('urban.jpg', 'wb') as file:
    file.write(r.content)


            # 2. Библиотека Pillow:
from PIL import Image

# Открытие ранее скаченного файла
im = Image.open('urban.jpg')

# Получение данных о файле:
print(im.format, im.size, im.mode)

# Изменение размера изображения:
new_image = im.resize((500, 500))

# Применение эффекта размытия
r, g, b = new_image.split()
new_image = Image.merge("RGB", (b, g, r))

# Конвертирование изображения в другой формат и сохранение
new_image.save('newurban.png', format='PNG')


            # 3. Библиотека Matplotlib:
import matplotlib.pyplot as plt

# Задание данных
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Создание линейного графика
plt.plot(x, y, marker='o')
plt.title('Квадрат чисел')
plt.xlabel('Числа')
plt.ylabel('Квадраты')
plt.grid(True)
plt.show()