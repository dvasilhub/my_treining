task_count = 12 # Количество выполненных ДЗ
hours_count = 1.5 # Количество затраченных часов
course_name = "Python" # Название курса
onetask_time = hours_count/task_count # Время на одно задание

# Выведите на экран(в консоль), используя переменные
print("Название курса:", str(course_name)+",", "всего задач: "+str(task_count)+",", "затрачено времени: "+str(hours_count)+" часов или", str(hours_count*60)+" минут, среднее время выполнения: "+str(onetask_time)+" часа или", str(onetask_time*60)+" минут.")