import requests
import allure
from data.data_for_registration_user import DataForRegistrationUser

class UserApi:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"

    @staticmethod
    def create_user(email, password, name):
        response = requests.post(f"{UserApi.BASE_URL}/auth/register", json={
            "email": email,
            "password": password,
            "name": name
        })
        return response

    @staticmethod
    def delete_user(access_token):
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.delete(f"{UserApi.BASE_URL}/users", headers=headers)
        return response


@allure.title("Тесты создания пользователя")
class TestCreateUser:

    @allure.title("Создание пользователя")
    @allure.step("Создание нового пользователя")
    @allure.description("Тестирует создание нового пользователя.")
    def test_we_can_create_user(self):
        response = UserApi.create_user(DataForRegistrationUser().email, DataForRegistrationUser().password, DataForRegistrationUser().name)

        assert response.status_code == 200  # SC_OK
        access_token = response.json().get("accessToken")

        # Удаляем пользователя после теста
        UserApi.delete_user(access_token)

    @allure.title("Попытка создать пользователя дважды")
    @allure.step("Создание пользователя с теми же данными дважды")
    @allure.description("Тестирует создание пользователя с уже существующими данными.")
    def test_double_create_user(self):
        data = (DataForRegistrationUser().email, DataForRegistrationUser().password, DataForRegistrationUser().name)
        response = UserApi.create_user(*data)


        assert response.status_code == 200  # SC_OK

        response1 = UserApi.create_user(*data)

        assert response1.status_code == 403  # SC_FORBIDDEN
        actual_message = response1.json().get("message")
        expected_message = "User already exists"

        assert actual_message == expected_message

        access_token = response.json().get("accessToken")

        # Удаляем пользователя после теста
        UserApi.delete_user(access_token)

    @allure.title("Создание пользователя без одного поля")
    @allure.step("Попытка создать пользователя без обязательного поля")
    @allure.description("Тестирует создание пользователя без указания обязательных полей.")
    def test_create_without_one_field(self):
        response = UserApi.create_user("", "18031993", "Анастасия")

        assert response.status_code == 403  # SC_FORBIDDEN
        actual_error = response.json().get("message")
        expected_error = "Email, password and name are required fields"

        assert actual_error == expected_error


if __name__ == "__main__":
    import pytest
    pytest.main()