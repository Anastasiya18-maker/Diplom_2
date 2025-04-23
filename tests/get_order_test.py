
import allure


from API.user_api import UserApi
from API.order_api import OrderApi



@allure.title("Тесты получения заказа")
class TestGetOrder:
    access_token = None

    @allure.title("Получение заказа с авторизацией")

    @allure.description("Тестирует получение заказа с использованием токена доступа.")
    def test_get_order_with_authorization(self):
        # Создаем пользователя

        response = UserApi.create_user("chernyshina15fs@yandex.ru", "18031993", "Анастасия")

        # Логинимся и получаем токен доступа
        response = UserApi.login_user("chernyshina15fs@yandex.ru", "18031993")
        assert response.status_code == 200  # SC_OK
        self.access_token = response.json().get("accessToken")

        # Получаем заказ с авторизацией
        response1 = OrderApi.get_order(self.access_token)
        assert response1.status_code == 200  # SC_OK

        actual_status = response1.json().get("success")
        # Удаляем пользователя после теста
        UserApi.delete_user(self.access_token)

        assert actual_status is True




    @allure.title("Получение заказа без авторизации")
    @allure.step("Получение заказа без авторизации")
    @allure.description("Тестирует получение заказа без токена доступа.")
    def test_get_order_without_authorization(self):
        # Получаем заказ без авторизации
        response = OrderApi.get_order_without_auth()

        assert response.status_code == 401  # SC_UNAUTHORIZED

        actual_error = response.json().get("message")
        expected_error = "You should be authorised"

        assert actual_error == expected_error


if __name__ == "__main__":
    import pytest

    pytest.main()