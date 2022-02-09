import json
import logging
from utils.cheking import Cheking
from utils.http_manager import HttpManager
from utils.logger import Logger
import requests

base_url = "https://rahulshettyacademy.com"  # Базовая url
key = "?key=qaclick123"  # Параметр для всех запросов

class Google_maps_api:
    LOGGER = logging.getLogger(__name__)



    @staticmethod
    def create_place():

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"

        }

        post_resource = "/maps/api/place/add/json"  # Ресурс метода Post

        url = base_url + post_resource + key
        print(url)
        result_post = HttpManager.post(url, json_for_create_new_location)
        print(result_post.text)

        return result_post


    def get_new_place(place_id):

        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = HttpManager.get(get_url)
        print(result_get.text)

        return result_get


    def put_new_place(place_id):
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        print(put_url)
        result_put = HttpManager.put(put_url, json_for_update_new_location)
        print(result_put.text)

        return result_put

    def delete_new_place(place_id):
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        json_for_delete_new_location = {
            "place_id": place_id
        }
        print(delete_url)
        result_delete = HttpManager.delete(delete_url, json_for_delete_new_location)
        print(result_delete.text)

        return result_delete