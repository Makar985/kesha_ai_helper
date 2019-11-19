# Подключение всех необходимых библиотек
# Нам нужно: speech_recognition, os, sys, webbrowser
# Для первой бибилотеки прописываем также псевдоним
import speech_recognition as sr
import os
import sys
import webbrowser
import time
import random
#import subbprocess

#file = ""
#def openFile(fileName):
#subprocess.run(['open', fileName], check=True)
# Функция, позволяющая проговаривать слова
# Принимает параметр "Слова" и прогроваривает их
def talk(words):
	print(words) # Дополнительно выводим на экран
	os.system("say " + words) # Проговариваем слова

# Вызов функции и передача строки 
# именно эта строка будет проговорена компьютером
talk("Привет, чем я могу помочь вам?")

""" 
	Функция command() служит для отслеживания микрофона.
	Вызывая функцию мы будет слушать что скажет пользователь,
	при этом для прослушивания будет использован микрофон.
	Получение данные будут сконвертированы в строку и далее
	будет происходить их проверка.
"""
def command():
	# Создаем объект на основе библиотеки
	# speech_recognition и вызываем метод для определения данных
	r = sr.Recognizer()

	# Начинаем прослушивать микрофон и записываем данные в source
	with sr.Microphone() as source:
		# Просто вывод, чтобы мы знали когда говорить
		print("Говорите")
		# Устанавливаем паузу, чтобы прослушивание
		# началось лишь по прошествию 1 секунды
		r.pause_threshold = 1
		# используем adjust_for_ambient_noise для удаления
		# посторонних шумов из аудио дорожки
		r.adjust_for_ambient_noise(source, duration=1)
		# Полученные данные записываем в переменную audio
		# пока мы получили лишь mp3 звук
		audio = r.listen(source)

	try: # Обрабатываем все при помощи исключений
		""" 
		Распознаем данные из mp3 дорожки.
		Указываем что отслеживаемый язык русский.
		Благодаря lower() приводим все в нижний регистр.
		Теперь мы получили данные в формате строки,
		которые спокойно можем проверить в условиях
		"""
		zadanie = r.recognize_google(audio, language="ru-RU").lower()
		# Просто отображаем текст что сказал пользователь
		print("Вы сказали: " + zadanie)
	# Если не смогли распознать текст, то будет вызвана эта ошибка
	except sr.UnknownValueError:
		# Здесь просто проговариваем слова "Я вас не поняла"
		# и вызываем снова функцию command() для
		# получения текста от пользователя
		talk("Я вас не поняла")
		zadanie = command()

	# В конце функции возвращаем текст задания
	# или же повторный вызов функции
	return zadanie

# Данная функция служит для проверки текста, 
# что сказал пользователь (zadanie - текст от пользователя)
def makeSomething(zadanie):
    
    # Попросту проверяем текст на соответствие
    # Если в тексте что сказал пользователь есть слова
    # "открыть сайт", то выполняем команду
    if 'открыть google' in zadanie or 'открыть гугл' in zadanie or "google" in zadanie or "гугл" in zadanie:
	    # Проговариваем текст
	    talk("Уже открываю")
	    # Указываем сайт для открытия
	    url_google = 'https://google.com'
	    # Открываем сайт
	    webbrowser.open(url_google)
    elif 'открыть youtube' in zadanie or 'открыть ютуб' in zadanie or "youtube" in zadanie or "ютуб" in zadanie:
        talk("Уже открываю")
        url_youtube = 'https://www.youtube.com'
        webbrowser.open(url_youtube)
    elif "клаус" in zadanie or "доктор клаус" in zadanie or "claus" in zadanie or "doctor claus" in zadanie:
        talk("Да это я, босс")
        time.sleep(1)
        talk("Вы что то хотели?")
    if 'открыть yandex' in zadanie or 'открыть яндекс' in zadanie or "yandex" in zadanie or "яндекс" in zadanie:
	    # Проговариваем текст
	    talk("Уже открываю")
	    # Указываем сайт для открытия
	    url_yandex = 'https://yandex.ru'
	    # Открываем сайт
	    webbrowser.open(url_yandex)
    if 'открыть hobby games' in zadanie or 'открыть хобби геймс' in zadanie or "hobby games" in zadanie or "хобби геймс" in zadanie:
	    # Проговариваем текст
	    talk("Уже открываю")
	    # Указываем сайт для открытия
	    url_hb = 'https://hobbygames.ru'
	    # Открываем сайт
	    webbrowser.open(url_hb)
    if 'открыть games workshop' in zadanie or 'открыть геймс воркшоп' in zadanie or "games workshop" in zadanie or "геймс воркшоп" in zadanie:
	    # Проговариваем текст
	    talk("Уже открываю")
	    # Указываем сайт для открытия
	    url_gw = 'https://www.games-workshop.com/en-WW/Home'
	    # Открываем сайт
	    webbrowser.open(url_gw)
    if 'открыть wikipedia' in zadanie or 'открыть википедию' in zadanie or "wikipedia" in zadanie or "википедия" in zadanie:
	    # Проговариваем текст
	    talk("Уже открываю")
	    # Указываем сайт для открытия
	    url_wp = 'https://www.wikipedia.org'
	    # Открываем сайт
	    webbrowser.open(url_wp)
    #if "открыть файл" in zadanie or "файл" in zadanie:
            #print("Введите название файла.")
            #file = input()
            #print("Открываю...")
            #openFile(file)

	    
        
    # если было сказано "стоп", то останавливаем прогу
    elif 'стоп' in zadanie:
	    # Проговариваем текст
	    talk("Да, конечно, без проблем")
	    # Выходим из программы
	    sys.exit()
    elif "монетку" in zadanie or "монетка" in zadanie:
        talk("Бросаю")
        mon = random.randint(1,2)
        resmon = str
        if mon == 1:
            resmon = "решка"
        else:
            resmon = "орел"
        talk(resmon)
    # Аналогично
    elif 'имя' in zadanie:
	    talk("Меня зовут Сири")
    elif 'до свидания' in zadanie:
            talk("До свидания!")
            sys.exit()

# Вызов функции для проверки текста будет 
# осуществляться постоянно, поэтому здесь
# прописан бесконечный цикл while
while True:
	makeSomething(command())
