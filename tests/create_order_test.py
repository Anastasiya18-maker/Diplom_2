import allure

from API.user_api import UserApi
from API.order_api import OrderApi



class TestCreateOrder:
    @allure.title("Создание пользователя перед тестами")
    @allure.step("Создание пользователя")
    @allure.description("Создает пользователя перед выполнением тестов.")
    def set_up(self):
        UserApi.create_user("chernyshina15fs@yandex.ru", "18031993", "Анастасия")


    @allure.title("Удаление пользователя после тестов")
    @allure.step("Удаление пользователя")
    @allure.description("Удаляет пользователя после выполнения тестов.")
    def tear_down(self):
        response = UserApi.login_user("chernyshina15fs@yandex.ru", "18031993")
        access_token = response.json().get("accessToken")
        UserApi.delete_user(access_token)

    @allure.title("Создание заказа с авторизацией")
    @allure.step("Создание заказа с авторизацией")
    @allure.description("Тестирует создание заказа с авторизацией.")
    def test_create_order_with_authorization(self):
        self.set_up()

        response = UserApi.login_user("chernyshina15fs@yandex.ru", "18031993")
        access_token = response.json().get("accessToken")

        response1 = OrderApi.get_ingredient()
        ingredients = [
            response1.json()["data"][1]["_id"],
            response1.json()["data"][2]["_id"]
        ]
        data_for_order = {"ingredients":ingredients}

        response2 = OrderApi.create_order_with_authorization(data_for_order, access_token)

        assert response2.status_code == 200  # SC_OK
        actual_status = response1.json().get("success")
        expected_status = True
        assert actual_status == expected_status

        self.tear_down()

    @allure.title("Создание заказа без авторизации")
    @allure.step("Создание заказа без авторизации")
    @allure.description("Тестирует создание заказа без авторизации.")
    def test_create_order_without_authorization(self):
        self.set_up()

        response = OrderApi.get_ingredient()

        ingredients = [
            response.json()["data"][0]["_id"],
            response.json()["data"][1]["_id"]
        ]
        data_for_order = {"ingredients": ingredients}

        response1 = OrderApi.create_order_without_authorization(data_for_order)

        assert response1.status_code == 200  # SC_OK
        actual_status = response1.json().get("success")
        expected_status = True
        assert actual_status == expected_status

        self.tear_down()

    @allure.title("Создание заказа без ингредиентов")
    @allure.step("Создание заказа без ингредиентов")
    @allure.description("Тестирует создание заказа без указания ингредиентов.")
    def test_create_order_without_ingredients(self):
        ingredients = []
        data_for_order = {"ingredients": ingredients}

        response = OrderApi.create_order_without_authorization(data_for_order)

        assert response.status_code == 400  # SC_BAD_REQUEST
        actual_error = response.json().get("message")
        expected_error_message = "Ingredient ids must be provided"

        assert actual_error == expected_error_message

    @allure.title("Создание заказа с неверными ингредиентами")
    @allure.step("Создание заказа с неверными ингредиентами")
    @allure.description("Тестирует создание заказа с неверными идентификаторами ингредиентов.")
    def test_create_order_with_false_ingredients(self):
        ingredients = [
            "I don`t care kakoi ingredient",
            "Again wrong Ingredient"
        ]
        data_for_order = {"ingredients": ingredients}

        response = OrderApi.create_order_without_authorization(data_for_order)

        assert response.status_code == 500  # SC_INTERNAL_SERVER_ERROR


if __name__ == "__main__":
    test_instance = TestCreateOrder()
