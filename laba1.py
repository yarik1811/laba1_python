#проверка на наличие модулей
try:
    import sys  #для принудительного завершения  программы
except:
    print('У вас не установлен модуль sys. Проверьте его наличие и установите при помощи pip install sys')
    sys.exit(0)
try:
    import os   #работа с директориями
except:
    print('У вас не установлен модуль os. Проверьте его наличие и установите при помощи pip install os')
    sys.exit(0)
try:
    import zipfile  #работа с архивами
except:
    print('У вас не установлен модуль zipfile. Проверьте его наличие и установите при помощи pip install zipfile')
    sys.exit(0)
try:
    import shutil   #для удаления директории если пользователь это пожелает ;)
except:
    print('У вас не установлен модуль shutil. Проверьте его наличие и установите при помощи pip install shutil')
    sys.exit(0)
try:
    import requests #обращение к сайтам
except:
    print('У вас не установлен модуль requests. Проверьте его наличие и установите при помощи pip install requests')
    sys.exit(0)
try:
    import hashlib  #хеширование данных
except:
    print('У вас не установлен модуль hashlib. Проверьте его наличие и установите при помощи pip install hashlib')
    sys.exit(0)
try:
    import re   #работа с регулярками
except:
    print('У вас не установлен модуль re. Проверьте его наличие и установите при помощи pip install re')
    sys.exit(0)
try:
    import wget # для загрузки архива с интернета, если он отсутствует
except:
    print('У вас не установлен модуль wget. Проверьте его наличие и установите при помощи pip install wget')
    sys.exit(0)
try:
    from prettytable import PrettyTable #чисто для красоты вывода :)
except:
    print('У вас не установлен модуль prettytable. Проверьте его наличие и установите при помощи pip install prettytable')
    sys.exit(0)
try:
    from tqdm import tqdm   # для создания progress_bar
    from time import sleep  # для демонмтрации задержки progress_bar
    import random   # для создания диапазона
except:
    print('У вас не установлен модуль tqdm, или time или random. Проверьте его наличие и установите при помощи pip install tqdm или time или random')
    sys.exit(0)

# проверка на наличие архива, если его нет, то он будет скачан
if os.path.exists('zip_zip.zip') == False:
    table = PrettyTable()
    table.field_names = ['Info']
    table.add_row(['Отсутствует архив "zip_zip.zip"'])
    table.add_row(['Начинаю загрузку...'])
    print(table)
    url = 'https://github.com/yarik1811/laba1_python/blob/main/zip_zip.zip?raw=true'
    wget.download(url, os.getcwd())
    for i in tqdm(range(100), colour = 'green'):
        sleep(random.uniform(0.01, 0.01))
zip_lib = os.path.abspath('zip_zip.zip') # заранее получаем расположение архива, ибо потом программа зайдёт в папку, и тогда лаба вообще сломается :(

# Задание №1
#Создание новой директории, в которую будет распакован архив
a = input('Введите имя папки в которую желаете распаковать архив: ')
if os.path.exists(a) == True:   #проверка на существование директории с указанным именем
    choice = input('Папка с указанным уменем уже существует, желаете её удалить? (Y/N): ')
    if choice == 'Y' or choice == 'y':   #если хотят удалить, то просто удаляю все и создаю папку 
        shutil.rmtree(os.path.join(os.path.abspath(os.path.dirname(a)), a))
        os.path.abspath(a)
        os.mkdir(a)
    elif choice == 'N' or  choice == 'n':   #если нет, то циклично запрашиваем до тех пор пока не введут нормальное название
        while os.path.exists(a): 
            a = input('Папка с указанным уменем уже существует, введите новое название папки: ')
        os.mkdir(a)
    else:
        print('Ну нет так нет. Лаба ушла спац |_( •_• )_|.')
        sys.exit(0)
else:   #если указанное имя папки не занято, то она создаётся
    os.mkdir(a) 
print('\n')
table = PrettyTable()
table.field_names = ['Задание №1', '']
table.add_row(['Директория успешно создана', os.path.abspath(a)])
print(table)
print('\n')

#С помощью модуля zipfile извлечь содержимое архива в созданную директорию
arch_file = zipfile.ZipFile(zip_lib) 
os.chdir(a) #переход в директорию для распаковки
arch_file.extractall()  #распаковка исходного архива в указанную директорию
arch_file.close()
#print("Текущая директория:", os.getcwd())
directory_to_extract_to = os.getcwd()
#print("Все папки и файлы в директории:", os.listdir())

#Задание №2.1
txt_files = []    #список путей к .txt файлам
all_files = []  #список путей ко всем файлам (надо для 3 задания, ибо мне лень было повторять этот шаг потом ещё раз ГЫЫЫЫ)
for root, dir, files in os.walk(directory_to_extract_to):
    for file in files:
        all_files.append(root+'/'+file)
        if file.endswith(".txt"):
             txt_files.append(root+'/'+file)
             #print(root+'\\'+file )


#Задание №2.2
table = PrettyTable()
table.field_names = ['Путь к файлу', 'Значение хеша']
print('Все полученные значения хеша .txt файлов:')

for file in txt_files:
    target_file_data = open(file,'rb').read()
    result = hashlib.md5(target_file_data).hexdigest()
    #print(file + ' : ' + result)
    table.add_row([file, result])
print(table)
print('\n')

#Задание №3
target_hash = "4636f9ae9fef12ebd56cd39586d33cfb"
table = PrettyTable()
table.field_names = ['Задание №3', '']

for file in all_files:
    target_file_data = open(file,'rb').read()
    result = hashlib.md5(target_file_data).hexdigest()
    if result == target_hash:   #проверяем совпадает ли найденный хеш, с нужным
        target_file = file  #полный путь к искомому файлу
        #print('Путь к искомому файлу: '+target_file)
        target_file_data = open(target_file, 'r')   #открываем файл
        target_file_data = target_file_data.read()  #кидаем в переменную содержимое файла
        #print(target_file_data) #печатаем содержимое искомого файла
        break

table.add_row(['Путь к искомому файлу:', target_file])
table.add_row(['Содержимое файла: ', target_file_data])
print(table)
print('\n')

# Задание №4
r = requests.get(target_file_data)
result_dct ={} #словарь для записи содержимого таблицы
counter=0
#Получение списка строк таблицы

lines = re.findall(r'<div class="Table-module_row__3TH83">.*?</div>.*?</div>.*?</div>.*?</div>.*?</div>', r.text)
#print(lines)
for line in lines:
    #извлечение заголовков таблицы
    if counter == 0:
        #Удаление тегов
        headers = re.sub('(<.+>)', '', line)

        #Извлечение списка заголовков
        headers = re.findall('([А-ЯЁа-яё]+ ?[А-ЯЁа-яё]*)+', line)
        #print(headers)
        counter += 1
        continue
    
    #Удаление тегов
    temp = re.sub('<[^>]+>', ';', line)
    #print(temp)
    
    #Значения в таблице, заключенные в скобках, не учитывать. Для этого удалить скобки и символы между ними.
    #temp=re.sub(r'\(.*\)', ' ', temp)
    temp=re.sub(r'\([^)]*\)', '', temp)
    #print(temp)
    
    #Замена последовательности символов ';' на одиночный символ
    temp = re.sub(r'(;)\1{1,}', r'\1', temp)
    #print(temp)

    #Разбитие строки на подстроки
    tmp_split = re.split(r';', temp)
    #print(tmp_split)
    
    #Извлечение и обработка (удаление "лишних" символов) данных из первого столбца
    country_name = tmp_split[1]
    country_name = re.sub('\W{4}|\W{3}', '', country_name)
    #print(country_name)
    
    #Извлечение данных из оставшихся столбцов. Данные из этих столбцов должны иметь числовое значение (прочерк можно заменить на -1).
    #Некоторые строки содержат пробелы в виде символа '\xa0'.
    col1_val = tmp_split[2]
    col1_val = re.sub('\s|\xa0', '', col1_val)
    col1_val = re.sub('[^0-9]', '', col1_val)
    # print(col1_val)

    col2_val = tmp_split[3]
    col2_val = re.sub('\s|\xa0', '', col2_val)
    # print(col2_val)

    col3_val = tmp_split[4]
    col3_val = re.sub('\s|\xa0', '', col3_val)
    # print(col3_val)

    col4_val = tmp_split[5]  # активные случаи
    col4_val = re.sub('\s|\xa0', '', col4_val)
    col4_val = re.sub('_', '-1', col4_val)
    # print(col4_val)   

    # Запись извлеченных данных в словарь
    result_dct[country_name] = {}
    result_dct[country_name][headers[0]] = col1_val
    result_dct[country_name][headers[1]] = col2_val
    result_dct[country_name][headers[2]] = col3_val
    result_dct[country_name][headers[3]] = col4_val
    #print(country_name, result_dct[country_name])

    counter += 1

# Задание №5
# Запись данных из полученного словаря в файл
output = open('data.csv', 'w')
for key in result_dct.keys():
    output.write(key)
    output.write(': ')
    output.write(str(result_dct[key]))
    output.write('\n')
output.close()

table = PrettyTable()
table.field_names = ['Задание №5', '']
table.add_row(['Данные были записаны в файл data.csv', os.path.abspath('data.csv')])
print(table)
print('\n')

# Задание №6
#Вывод данных на экран для указанного первичного ключа (первый столбец таблицы)
target_country = None
print('Для завершения введите STOP')
while True: 
    target_country = input("Введите название страны: ")
    print('\n')
    if (target_country == 'stop') | (target_country == 'STOP'):
        break
    print_country = open(os.path.abspath('data.csv'), 'r')
    table = PrettyTable()
    table.field_names = ['Введенная страна: '+ target_country]
    country_find = False
    table.add_row(['Если было найдено несколько стран, то они все будут выведены\n']) #для штуки если вдруг введут только первую букву страны  
    for line in print_country:
        if re.match(target_country, line) != None:
            table.add_row([line])  
            country_find = True
    if country_find == False:
        table.add_row(['Указанной страны нет в таблице :('])
    print(table)
    print('\n')
print('Вы закончили мучение над моей лабой, вот вам коровка')
print(' /-----------\\')
print('<    му-му    >')
print(' \\-----------/')
print('                \\')
print('                 \\')
print('                   ^__^')
print('                   (oo)\_______')
print('                   (__)\\       )\\/\\')
print('                       ||----w |')
print('                       ||     ||\n')
