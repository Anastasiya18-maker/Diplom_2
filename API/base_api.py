import requests
import allure
class UsedUrl:
    BURGER_URL = "https://stellarburgers.nomoreparties.site"  # Замените на ваш реальный URL

class BaseApi:
    @staticmethod
    @allure.step("Получение базовых параметров для API")
    def base_api():
        # Возвращаем базовые параметры для API
        return {
            "base_url": UsedUrl.BURGER_URL,
            "headers": {
                "Content-Type": "application/json"
            }
        }
