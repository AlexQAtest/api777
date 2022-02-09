import requests
from utils.logger import Logger
import allure


class HttpManager:
    headers = {'Content-Type': 'application/json'}
    cookie = ""


    @staticmethod
    def get(url):
        with allure.step("Login"):
            Logger.add_request(url, method="GET")
            result = requests.get(url,
                                  headers=HttpManager.headers,
                                 cookies=HttpManager.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        Logger.add_request(url, method="POST")
        result = requests.post(url,
                               json=body,
                               headers=HttpManager.headers,
                               cookies=HttpManager.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def put(url, body):
        Logger.add_request(url, method="PUT")
        result = requests.put(url,
                              json=body,
                              headers=HttpManager.headers,
                              cookies=HttpManager.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def delete(url, body):
        Logger.add_request(url, method="DELETE")
        result = requests.delete(url,
                                 json=body,
                                 headers=HttpManager.headers,
                                 cookies=HttpManager.cookie)
        Logger.add_response(result)
        return result