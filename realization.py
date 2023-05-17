import requests
import random
import string
import http
import socket
import urllib.parse
import httpx
import zlib
import sys

#url = 'https://cv-gml.ru/login'

print ("Введите ссылку для проверки на некорректные запросы: ", sys.argv[1])
url = str(sys.argv[1])
parsed_url = urllib.parse.urlparse(url)

#########################################
def send_invalid_method(url):
    try:
        response = requests.request("INVALID_METHOD", url)
        print('invalid method - > ', response)
        return response
    except requests.exceptions.RequestException as e:
        print('invalid method - > ' , str(e))
        return str(e)

def send_invalid_version(url):
    parsed_url = http.client.urlsplit(url)
    host = parsed_url.netloc
    path = parsed_url.path
    conn = http.client.HTTPConnection(host)
    try:
        request_line = "GET {} HTTP/3.0\r\n".format(path)
        conn.request("GET", path, headers={"Host": host, "User-Agent": "My User Agent"})
        response = conn.getresponse()
        content = response.read()
        print('invalid version -> ', content)
        return content
    except http.client.HTTPException as e:
        print('invalid version -> ',str(e))
        return str(e)
    finally:
        conn.close()



from requests.adapters import HTTPAdapter

class InvalidProtocolAdapter(HTTPAdapter):
    def send(self, request, **kwargs):
        request.url = request.url.replace('http://', 'invalid://')
        return super().send(request, **kwargs)

def send_invalid_protocol(url):
    session = requests.Session()
    session.mount('http://', InvalidProtocolAdapter())
    try:
        response = session.get(url)
        print('invalid protocol -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('invalid protocol -> ' ,str(e))
        return str(e)


def send_invalid_page(url):
    try:
        response = requests.get(url + "/nonexistent_page")
        print('Non-existent page -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Non-existent page -> ',str(e))
        return str(e)

def send_invalid_parameters(url):
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

def send_invalid_method(url):
    try:
        method = 'DELETE'
        response = requests.request(method, url)
        print('Incorrect method -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Incorrect method -> ',str(e))
        return str(e)

def send_http2_request(url):
    try:
        client = httpx.Client(http2=True)
        response = client.get(url)
        print('HTTP/2 -> ',response)
        return response
    except httpx.HTTPError as e:
        print('HTTP/2 -> ',str(e))
        return str(e)
    finally:
        client.close()


def send_big_length(url):
    headers = {
    "Content-Length": "9999999999"
    }
    try:
        response = requests.post(url, headers=headers, data="")
        print('Invalid Content-length  -> ',response)
        return response
    except requests.RequestException as e:
        print('Invalid Content-length  -> ',str(e))
        return str(e)

def send_invalid_UserAgent(url):
    try:
        headers = {"User-Agent": "invalid-user-agent"}
        response = requests.get(url, headers=headers)
        print('Invalid User-agent -> ',response)
        return response
    except requests.RequestException as e:
        print('Invalid User-agent -> ',str(e))
        return str(e)

def send_invalid_type(url):
    try:
        headers = {
            "Content-Type": "application/invalid"
        }
        response = requests.get(url, headers=headers)
        print('Invalid Content-Type -> ',response)
        return response
    except requests.RequestException as e:
        print('Invalid Content-Type -> ',str(e))
        return str(e)

class InvalidTransferEncodingAdapter(requests.adapters.HTTPAdapter):
    def add_headers(self, request, **kwargs):
        request.headers["Transfer-Encoding"] = "invalid"

def send_invalid_encoding(url):
    try:
        session = requests.Session()
        session.mount("http://", InvalidTransferEncodingAdapter())
        session.mount("https://", InvalidTransferEncodingAdapter())
        response = session.get(url)
        print('Invalid Trasfer-Encoding  -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Invalid Trasfer-Encoding  -> ',str(e))
        return str(e)

class InvalidCacheControlAdapter(requests.adapters.HTTPAdapter):
    def add_headers(self, request, **kwargs):
        request.headers["Cache-Control"] = "invalid"

def send_invalid_cash(url):
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

def send_invalid_null(url):
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


def send_invalid_delete(url):
    head= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": url,
    "Cookie": "",
    }

    try:
        response = requests.get(url, headers=head)
        print('Deleted Cookies -> ',response)
        return response
    except http.client.HTTPException as e:
        print('Deleted Cookies -> ',str(e))
        return str(e)



def send_invalid_crlf(url):
    try:
        headers = {
            "Invalid-Header": "Invalid-Value\nContent-Type: application/json"
        }
        response = requests.get(url, headers=headers)
        print('Empty CRLF -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Empty CRLF -> ',str(e))
        return str(e)


def send_invalid_request_body(url):
    try:
        payload = "<invalid_payload>"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, data=payload, headers=headers)
        print('Invalid request body -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Invalid request body -> ',str(e))
        return str(e)

def send_invalid_request_body_length(url):
    try:
        payload = "Invalid payload with incorrect length"
        headers = {
            "Content-Type": "application/json",
            "Content-Length": str(len(payload) - 1)
        }
        response = requests.post(url, data=payload, headers=headers)
        print('Invalid request length -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Invalid request length -> ',str(e))
        return str(e)

def send_invalid_gzip(url):
    try:
        payload = "Invalid payload"
        headers = {
            "Content-Type": "application/json",
            "Content-Encoding": "gzip"
        }
        compressed_data = zlib.compress(payload.encode())
        response = requests.post(url, data=compressed_data, headers=headers)
        print('Broken gzip -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Broken gzip -> ',str(e))
        return str(e)

def send_invalid_delimiters(url):
    try:
        payload = "Invalid payload"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = "%%%" + payload + "###"
        response = requests.post(url, data=body, headers=headers)
        print('Invalid delimiters -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Invalid delimiters -> ',str(e))
        return str(e)


def send_invalid_fragments(url):
    try:
        payload = "Invalid payload"
        headers = {
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
    try:
        payload = "Invalid payload"
        headers = {
            "Content-Length": "99999",
            "Content-Type": "text/plain"
        }
        response = requests.post(url, data=payload, headers=headers)
        print('Missed request length -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Missed request length -> ',str(e))
        return str(e)

def send_invalid_json(url):
    try:
        invalid_payload = "Invalid payload"
        headers = {
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
            "Content-Type": "application/octet-stream"
        }
        response = requests.post(url, data=invalid_payload, headers=headers)
        print('Invalid format -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Invalid format -> ',str(e))
        return str(e)


def send_invalid_big_body(url):
    try:
        invalid_payload = "Invalid payload"
        headers = {
            "Content-Length": "9999999999999999999999999999999999999"
        }
        response = requests.post(url, data=invalid_payload, headers=headers)
        print('Unexpected Content-length -> ',response)
        return response
    except requests.exceptions.RequestException as e:
        print('Unexpected Content-length -> ',str(e))
        return str(e)

send_invalid_method(url)
send_invalid_version(url)
send_invalid_protocol(url)
send_invalid_page(url)
send_invalid_parameters(url)
send_invalid_method(url)
send_http2_request(url)
send_big_length(url)
send_invalid_UserAgent(url)
send_invalid_type(url)
send_invalid_encoding(url)
send_invalid_cash(url)
send_invalid_null(url)
send_invalid_delete(url)
send_invalid_crlf(url)
send_invalid_request_body(url)
send_invalid_request_body_length(url)
send_invalid_gzip(url)
send_invalid_delimiters(url)
send_invalid_fragments(url)
send_invalid_missed(url)
send_invalid_json(url)
send_invalid_format(url)
send_invalid_big_body(url)
