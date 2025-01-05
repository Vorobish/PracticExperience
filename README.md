# Практическое задание:
## "Анализатор прайс-листов".

# Описание проекта

  ### В папке находятся несколько файлов, содержащих прайс-листы от разных поставщиков.

####	• Количество и название файлов не ограничено
####	• В названии должно быть слово "price" (остальные файлы игнорируются)
####	• Формат файлов: данные, разделенные точкой с запятой.
####	• В файле обязательно должны присутствовать три поля (остальные столбцы игнорируются):
####	    1. Наименование товара ("название", "продукт", "товар", "наименование")
####	    2. Цена товара ("цена", "розница")
####	    3. Вес товара ("фасовка", "масса", "вес")
  
## Функционал:
  
####	• Программа загружает данные из всех прайс-листов
####	• И через консоль предоставляет интерфейс для поиска товара по фрагменту названия с сорторовкой по цене за килогорамм (в виде таблицы)
####	• Работает циклически получая информацию от пользователя
####	• Сохраняет результат в виде массива данных в текстовый файл output.html (каждый раз перезаписывает)
####	• Для выхода - ввести слово "exit"

# Как запустить
  
####  1. Склонируйтке проект и перейдите в директорию проекта.
####  2. Установите необходимые библиотеки (перечислены ниже).
####  3. Создайте папку folder и загрузите в неё прайс-листы, которые требуется анализировать.
####  4. Путь до  папки указать в переменной "directory" (в модуле "project.py")
####  5. Откройте модуль "project.py" и запустите код с помощью команды "Run"

# Основные библиотеки

1. fnmatch — это библиотека для Python, которая позволяет сравнивать имя файла с заданным шаблоном и возвращает True, если они совпадают, иначе False.
2. os - библиотека, которая предоставляет множество функций для работы с операционной системой.
3. pandas — библиотека, которая позволяет работать с двумерными массивами неоднотипных данных.
