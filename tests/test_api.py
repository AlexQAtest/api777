from requests import Response
from utils.api import Google_maps_api
from utils.cheking import Cheking
import allure


@allure.epic("Test create place")
class Test_create_place():

    @allure.description("Test create, update, delete new place")
    def test_create_new_place(self):
        print("Метод post")
        result_post: Response = Google_maps_api.create_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Cheking.check_status_code(result_post, 200)
        Cheking.check_json_value(result_post, 'status', 'OK')

        print("Метод get post")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get,
                                 ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                  'language'])

        print("Метод put")
        result_put = Google_maps_api.put_new_place(place_id)
        Cheking.check_status_code(result_put, 200)
        Cheking.check_json_value(result_put, "msg", "Address successfully updated")


        print("Метод get put")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get,
                                 ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                  'language'])

        print("Метод delete")
        result_delete: Response = Google_maps_api.delete_new_place(place_id)
        Cheking.check_status_code(result_delete, 200)


        print("Метод get delete")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 404)
        Cheking.check_json_value(result_delete, 'status', 'OK')

        print("Тестирование создания, изменения и удаления новой локации прошло успешно")