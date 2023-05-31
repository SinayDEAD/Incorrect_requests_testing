import requests
import random
import string
import http
import socket
import urllib.parse
import zlib
import gzip
import sys
import subprocess
import http.client
import ssl
from urllib.parse import urlparse
import http.client
import httpx
import subprocess
from ftplib import FTP

url = 'https://cv-gml.ru/login'

#print ("Введите ссылку для проверки на некорректные запросы: ", sys.argv[1])
#url = str(sys.argv[1])
parsed_url = urllib.parse.urlparse(url)

#########################################
def send_invalid_method(url): #+
    try:
        response = requests.request("INVALID_METHOD", url)
        print('invalid method - > ', response)
        return response
    except requests.exceptions.RequestException as e:
        print('invalid method - > ' , str(e))
        return str(e)

def send_invalid_version(url):
    headers = {"User-Agent": "My User Agent",
               "Upgrade-Insecure-Requests": "3.0"
    } # Неверная версия протокола}
    try:
        response = requests.get(url, headers=headers)
        print('Non-existent page -> ',response)
        response.raise_for_status() # Генерирует исключение, если получен неправильный статус ответа
        content = response.content
        return content
    except requests.exceptions.RequestException as e:
        print('Ошибка ->', str(e))
        return str(e)

def send_invalid_page(url): #+
    try:
        response = requests.get(url + "/nonexistent_page")
        print('Non-existent page -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Non-existent page -> ',str(e))
        return str(e)

def send_invalid_parameters(url): #+
    try:
        params = {
            "invalid_param": "value"
        }
        response = requests.get(url, params=params)
        print('Incorrect parameters -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Incorrect parameters -> ',str(e))
        return str(e)

def send_invalid_method(url): #+
    try:
        method = 'DELETE'
        response = requests.request(method, url)
        print('Incorrect method -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Incorrect method -> ',str(e))
        return str(e)

def send_invalid_UserAgent(url): #+
    try:
        headers = {"User-Agent": "invalid-user-agent"}
        response = requests.get(url, headers=headers)
        print('Invalid User-agent -> ',response)
        return response
    except requests.RequestException as e:
        print('Invalid User-agent -> ',str(e))
        return str(e)

def send_invalid_type(url): #+
    try:
        payload = "<root>Invalid payload</root>"
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers, data=payload)
        print('Invalid Content-Type -> ',response)
        return response
    except requests.RequestException as e:
        print('Invalid Content-Type -> ',str(e))
        return str(e)

def send_invalid_encoding(url): #+
    # Отправляем запрос с использованием curl и неподдерживаемым Transfer-Encoding
    curl_command = ['curl', '-X', 'POST', '-H', 'Transfer-Encoding: gzip', '-d', 'data=Hello', url]
    curl_process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Получаем вывод curl (если необходимо)
    curl_output, curl_error = curl_process.communicate()
    print("Output from curl:")
    print(curl_output.decode())

    # Получаем ошибку curl (если есть)
    if curl_error:
        print("Error from curl:")
        print(curl_error.decode())

class InvalidCacheControlAdapter(requests.adapters.HTTPAdapter):
    def add_headers(self, request, **kwargs):
        request.headers["Cache-Control"] = "invalid"

def send_invalid_cash(url): #+
    try:
        session = requests.Session()
        session.mount("http://", InvalidCacheControlAdapter())
        session.mount("https://", InvalidCacheControlAdapter())
        response = session.get(url)
        print('Invalid Cash-Control -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Invalid Cash-Control -> ',str(e))
        return str(e)

def send_invalid_null(url): #+
    try:
        parsed_url = urllib.parse.urlparse(url)
        path_bytes = parsed_url.path.encode()
        path_bytes_with_null_byte = path_bytes + b'\x00'
        path_with_null_byte = path_bytes_with_null_byte.decode()
        updated_parsed_url = parsed_url._replace(path=path_with_null_byte)
        updated_url = urllib.parse.urlunparse(updated_parsed_url)
        response = requests.get(updated_url)
        print('Null byte  -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Null byte  -> ',str(e))
        return str(e)

def send_invalid_delete(url): #+
    # Отправляем запрос без куки с использованием curl
    curl_command = ['curl', '-X', 'GET', '-H', 'Cookie:', '-D', '-', url]
    curl_process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Получаем вывод curl (включая заголовки ответа)
    curl_output, curl_error = curl_process.communicate()
    print("Output from curl:")
    print(curl_output.decode())

    # Получаем ошибку curl (если есть)
    if curl_error:
        print("Error from curl:")
        print(curl_error.decode())

def send_invalid_crlf(url): # чисто попытка
    parsed_url = urllib.parse.urlparse(url)
    host = parsed_url.netloc
    port = 80
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    # Отправляем запрос с внедренными символами CRLF
    request = "GET / HTTP/1.1\r\nHost: " + host +"\r\nUser-Agent: Mozilla/5.0\r\n\r\n"
    print(request)
    sock.send(request.encode())

    # Получаем ответ от сервера
    response = sock.recv(4096)
    print(response.decode())

    # Закрываем соединение
    sock.close()

def send_invalid_request_body(url): #+
    try:
        payload = "<invalid_payload>"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": url,
            "Content-Type": "application/json",
        }
        response = requests.post(url, data=payload, headers=headers)
        print('Invalid request body -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Invalid request body -> ',str(e))
        return str(e)

def send_invalid_request_body_length(url): #+
    # Определяем тело запроса
    request_body = 'This is the actual request body'
    # Получаем длину тела запроса и уменьшаем её на 1
    content_length = str(len(request_body) - 1)

    # Отправляем запрос с ошибочной длиной тела с использованием curl
    curl_command = ['curl', '-X', 'POST', '-H', 'Content-Type: text/plain', '--header', 'Content-Length: ' + content_length, '-d', request_body, url]
    curl_process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Получаем вывод curl (если необходимо)
    curl_output, curl_error = curl_process.communicate()
    print("Output from curl:")
    print(curl_output.decode())

    # Получаем ошибку curl (если есть)
    if curl_error:
        print("Error from curl:")
        print(curl_error.decode())

def send_invalid_gzip(url): #+
    try:
        # Определяем некорректные данные для сжатого тела запроса
        invalid_body_data = 'This is an invalid compressed request body'

        # Сжимаем данные с использованием zlib
        compressed_data = zlib.compress(invalid_body_data.encode())

        # Отправляем запрос с некорректным сжатым телом запроса с использованием requests
        headers = {'Content-Type': 'application/json', 'Content-Encoding': 'gzip'}
        response = requests.post(url, data=compressed_data, headers=headers)

        # Получаем ответ от сервера
        print("Response status code:", response.status_code)
        print("Response content:", response.text)
    except requests.exceptions.RequestException as e:
        print('Broken gzip -> ',str(e))
        return str(e)

def send_invalid_delimiters(url): #+
    # Определяем некорректные данные с ошибочными разделителями в теле запроса
    invalid_body_data = '%%%This|is|an|invalid|body###'

    # Отправляем запрос с некорректными разделителями в теле с использованием curl
    curl_command = ['curl', '-X', 'POST', '-H', 'Content-Type: text/plain', '-d', invalid_body_data, url]
    curl_process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Получаем вывод curl (если необходимо)
    curl_output, curl_error = curl_process.communicate()

    print("Output from curl:")
    if curl_output:
        try:
            # Если данные сжаты, декодируем их с использованием gzip
            if curl_output.startswith(b'\x1f\x8b'):
                curl_output = gzip.decompress(curl_output)
            print(curl_output.decode())
        except UnicodeDecodeError:
            print("Unable to decode output")

            # Получаем ошибку curl (если есть)
    if curl_error:
        print("Error from curl:")
        print(curl_error.decode())

def send_invalid_fragments(url): #+
    try:
        payload = "Invalid payload"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": url,
            "Content-Type": "text/plain"
        }
        fragments = ["$%^&", "@!#*", "&$#!"]
        body = "".join(fragments) + payload
        response = requests.post(url, data=body, headers=headers)
        print('Encoding with incorrect fragments -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Encoding with incorrect fragments -> ',str(e))
        return str(e)

def send_invalid_missed(url):
    # Отправляем запрос с отсутствующей длиной запроса с использованием curl
    curl_command = ['curl', '-X', 'POST', '-H','Content-Length:', 'Content-Type: text/plain', '-d', b'Hello, world!', url]
    curl_process = subprocess.Popen(curl_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Вводим данные в stdin процесса curl для отправки
    curl_output, curl_error = curl_process.communicate()

    print("Output from curl:")
    if curl_output:
        try:
            # Если данные сжаты, декодируем их с использованием gzip
            if curl_output.startswith(b'\x1f\x8b'):
                curl_output = gzip.decompress(curl_output)
            print(curl_output.decode())
        except UnicodeDecodeError:
            print("Unable to decode output")

            # Получаем ошибку curl (если есть)
    if curl_error:
        print("Error from curl:")
        print(curl_error.decode())

def send_invalid_json(url):
    try:
        invalid_payload = "wedrftgyhuji_@#$<>Invalid payload"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Content-Type": "application/json"
        }
        response = requests.post(url, data=invalid_payload, headers=headers)
        print('Json -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Json -> ',str(e))
        return str(e)

def send_invalid_format(url):
    try:
        invalid_payload = "Invalid payload"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Content-Type": "application/octeam"
        }
        response = requests.post(url, data=invalid_payload, headers=headers)
        print('Invalid format -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Invalid format -> ',str(e))
        return str(e)

######################

def send_http2_request(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Cache-Control": "no-cache",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": url,
        "Content-Type": "text/plain"
    }

    try:
        with httpx.Client(http2=True) as client:
            response = client.get(url, headers=headers)
        if len(response.content) == 0:
            print('Empty Response')
        else:
            print('HTTP/2 >', response.status_code)
        return response
    except httpx.RequestError as e:
        print('Request Error:', str(e))
        return str(e)

def send_invalid_protocol(url):
    # Определяем некорректные данные с ошибочным протоколом HTTP/0.9
    invalid_protocol_data = 'GET /index.html\n'

    # Запускаем ncat в отдельном процессе и передаем некорректные данные
    ncat_process = subprocess.Popen(['ncat', url], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ncat_process.stdin.write(invalid_protocol_data.encode())
    ncat_process.stdin.flush()
    ncat_output, ncat_error = ncat_process.communicate()
    ncat_process.stdin.close()

    # Получаем вывод ncat

    # Получаем код ответа из вывода ncat
    status_code = get_status_code(ncat_output.decode())
    print("Status code:", status_code)

# Получаем ошибку ncat (если есть)
    if ncat_error:
        print("Error from ncat:")
        print(ncat_error.decode())

def get_status_code(response_output):
    lines = response_output.split('\n')
    if len(lines) > 0:
        status_line = lines[0]
        if ' ' in status_line:
            status_code = status_line.split(' ')[1]
            return status_code.strip()

    return None

def send_big_content_length(url): # Наконецто рабочая ТВААААААРЬ
    # Определяем некорректное значение для заголовка Content-Length
    big_content_length = '9999999'

    # Отправляем запрос с некорректным значением Content-Length с использованием curl
    curl_command = ['curl', '-X', 'POST', '-H', 'Content-Length: ' + big_content_length, url]
    curl_process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Получаем вывод curl (если необходимо)
    curl_output, curl_error = curl_process.communicate()
    print("Output from curl:")
    print(curl_output.decode())

    # Получаем ошибку curl (если есть)
    if curl_error:
        print("Error from curl:")
        print(curl_error.decode())



#send_invalid_method(url)
#send_invalid_version(url)
#send_invalid_page(url)
#send_invalid_parameters(url)
#send_invalid_method(url)
#send_invalid_UserAgent(url)
#send_invalid_type(url)
#send_invalid_encoding(url)
#send_invalid_cash(url)
#send_invalid_null(url)
#send_invalid_delete(url)
#send_invalid_crlf(url)
#send_invalid_request_body(url)
#send_invalid_request_body_length(url)
#send_invalid_gzip(url)
#send_invalid_delimiters(url)
#send_invalid_fragments(url)
#send_invalid_missed(url)
#send_invalid_json(url)
#send_invalid_format(url)
#send_http2_request(url)
#send_invalid_protocol(url)
#send_big_content_length(url)
