import http.client
from abc import ABC, abstractmethod
from http.client import responses


class HttpRequest(ABC):
    @abstractmethod
    def request(self, id: int) -> str:
        pass



class HttpGet(HttpRequest):
    def __init__(self, url: str,path: str):
        self.__url = url
        self.__path = path

    def request(self, id: int):
        conn = http.client.HTTPConnection(self.__url)
        conn.request("GET", f"/{self.__path}/{id}")
        response = conn.getresponse()

        if response.status == 200:
            data = response.read()
            return data.decode("utf-8")
        else:
            print(f"Error en la solicitud {response.status}")

        conn.close()



class HttpRequestFactory(ABC): # Factory es para definir configuracion
    def __init__(self, url: str, path: str):
        self._url = url
        self._path = path

    @abstractmethod
    def create(self)-> HttpRequest:
        pass


class HttpGetFactory(HttpRequestFactory):
    def create(self):
        return HttpGet(self._url, self._path)


get_factory = HttpGetFactory("jsonplaceholder.typicode.com", "posts")
http_get = get_factory.create()

res = http_get.request(8)

print(res)