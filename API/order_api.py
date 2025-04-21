import requests
import allure
from URL import UsedUrl

class BaseApi:
    @staticmethod
    @allure.step("Получение базовых параметров для API")
    def base_api():
        return {
            "base_url": "https://stellarburgers.nomoreparties.site",
            "headers": {
                "Content-Type": "application/json"
            }
        }

class OrderApi(BaseApi):
    @staticmethod
    @allure.step("Получение ингредиентов")
    def get_ingredient():
        response = requests.get(f"{BaseApi.base_api()['base_url']}{UsedUrl.URL_INGREDIENTS}", headers=BaseApi.base_api()['headers'])
        return response

    @staticmethod
    @allure.step("Создание заказа без авторизации")
    def create_order_without_authorization(data_for_order):
        response = requests.post(f"{BaseApi.base_api()['base_url']}{UsedUrl.URL_ORDER}", json=data_for_order, headers=BaseApi.base_api()['headers'])
        return response

    @staticmethod
    @allure.step("Создание заказа с авторизацией")
    def create_order_with_authorization(data_for_order, access_token: str):
        headers = {
            **BaseApi.base_api()['headers'],
            "Authorization": access_token
        }
        response = requests.post(f"{BaseApi.base_api()['base_url']}{UsedUrl.URL_ORDER}", json=data_for_order, headers=headers)
        return response

    @staticmethod
    @allure.step("Получение заказа")
    def get_order(access_token: str):
        headers = {
            **BaseApi.base_api()['headers'],
            "Authorization": access_token
        }
        response = requests.get(f"{BaseApi.base_api()['base_url']}{UsedUrl.URL_ORDER}", headers=headers)
        return response

    @staticmethod
    @allure.step("Получение заказа без авторизации")
    def get_order_without_auth():
        response = requests.get(f"{BaseApi.base_api()['base_url']}{UsedUrl.URL_ORDER}", headers=BaseApi.base_api()['headers'])
        return response