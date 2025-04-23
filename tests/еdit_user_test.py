
import allure
from API.user_api import UserApi



@allure.title("Тесты редактирования пользователя")
class TestEditUser:

    @allure.title("Редактирование email пользователя")

    @allure.description("Тестирует редактирование email пользователя.")
    def test_edit_user_email(self):
        # Создаем пользователя
        UserApi.create_user("chernyshina15fs@yandex.ru", "18031993", "Анастасия")

        # Логинимся и получаем токен доступа
        response = UserApi.login_user("chernyshina15fs@yandex.ru", "18031993")
        assert response.status_code == 200  # SC_OK
        access_token = response.json().get("accessToken")

        # Редактируем email пользователя
        response1 = UserApi.edit_user("chernyshina15fs@yandex.ru", "18031993", access_token)
        assert response1.status_code == 200  # SC_OK

        actual_message_with_email = response1.json().get("success")
        expected_message_with_email = True

        assert actual_message_with_email == expected_message_with_email

        # Удаляем пользователя после теста
        UserApi.delete_user(access_token)

    @allure.title("Редактирование пароля пользователя")

    @allure.description("Тестирует редактирование пароля пользователя.")
    def test_edit_user_password(self):
        # Создаем пользователя
        UserApi.create_user("chernyshina15fs@yandex.ru", "18031993", "Анастасия")

        # Логинимся и получаем токен доступа
        response = UserApi.login_user("chernyshina15fs@yandex.ru", "18031993")
        assert response.status_code == 200  # SC_OK
        access_token = response.json().get("accessToken")

        # Редактируем пароль пользователя
        response1 = UserApi.edit_user("chernyshina15fs@yandex.ru", "18031003", access_token)
        assert response1.status_code == 200  # SC_OK

        actual_message_with_password = response1.json().get("success")
        expected_message_with_password = True

        assert actual_message_with_password == expected_message_with_password

        # Удаляем пользователя после теста
        UserApi.delete_user(access_token)

    @allure.title("Попытка редактирования без авторизации")

    @allure.description("Тестирует попытку редактирования без токена доступа.")
    def test_edit_user_without_authorization(self):
        # Создаем пользователя и логинимся для получения токена доступа
        UserApi.create_user("chernyshina15fs@yandex.ru", "18031993", "Анастасия")

        response = UserApi.login_user("chernyshina15fs@yandex.ru", "18031993")

        assert response.status_code == 200  # SC_OK

        access_token = response.json().get("accessToken")

        # Попытка редактирования без авторизации (неправильный токен)
        response1 = UserApi.edit_user("chernyshina15fs@yandex.ru", "18031003", "NoAccessToken")
        assert response1.status_code == 401  # SC_UNAUTHORIZED

        actual_error_for_edit = response1.json().get("message")
        expected_error_for_edit = "You should be authorised"

        assert actual_error_for_edit == expected_error_for_edit

        # Удаляем пользователя после теста
        UserApi.delete_user(access_token)


if __name__ == "__main__":
    import pytest

    pytest.main()