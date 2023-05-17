# Incorrect_requests_testing

Данная программа включает в себя 24 некорректных запроса, который разработаны согласно классификации, пытающейся покрыть максимальное
вариативное множество ошибок, которые могут вызваны всему возможными ошибками в HTTP-сообщении.

  Так как бибоитека "Request" пусть и является наиболее удобной для отправки запросов, она также имеет особенность, такую как
редактировать ошибки.Данная особенность попыталась быть обойденной использованием сокетов, библиотекой httpx и 
нетривиальными версиями запросов.

Также содержится файл с подробным описанием каждой функции.

 Для корректного использованияследует иметь python3 и библиотеки:
 requests
 random
 string
 http
 socket
 urllib.parse
 httpx
 zlib
 sys

Для запуска требуется написать "python3 realization.py "ссылка на проверяемый сайт" "

Пример запуска - 
python3 realization.py https://cv-gml.ru/login





