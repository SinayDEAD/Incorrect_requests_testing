# Incorrect_requests_testing
Данная программа включает в себя 24 некорректных запроса, которые разработаны 
согласно классификации, предназначенной для покрытия максимально вариативного 
множества ошибок, которые могут быть вызваны возможными ошибками в HTTP-
сообщении.

Несмотря на то, что библитека "Request" является наиболее удобной для отправки 
запросов, она способна самостоятельно редактировать ошибки. Чтобы попробовать 
обойти данную особенность, будут использоваться сокеты, библиотека httpx и инструменты curl и ncat и 
нетривиальные версии запросов.

Также в гите содержится файл с подробным описанием каждой функции.

Для корректного использования следует установить 
1. python3 и библиотеки: 
requests,
random,
string,
http,
socket,
urllib.parse,
zlib,
gzip,
sys,
subprocess,
http.client,
ssl,
urllib.parse,
http.client,
httpx,
subprocess,
ftplib
2. Доустановить curl и ncat

Перед запусаком необходимо убрать комментарии из тех тестов, что вы хотите провести и выбрать ввод из терминала или уже выбранные сайты.
Для запуска требуется ввести в консоль команду: 

1. python3 realization.py "ссылка на проверяемый сайт" 
2. python3 realization.py

Пример запуска 1 : python3 realization.py https://cv-gml.ru/login
Пример запуска 2 : python3 realization.py 

P.S. При одновременном запуске, ответы от сервера могут быть искажены, поэтому каждую функцию лучше запускать отдельно.


