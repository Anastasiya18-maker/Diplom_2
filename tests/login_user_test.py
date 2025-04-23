
import allure
from API.user_api import UserApi




@allure.title("Тесты авторизации пользователя")
class TestLoginUser:
    access_token = None

    @allure.title("Авторизация существующего пользователя")

    @allure.description("Тестирует авторизацию с использованием существующего пользователя.")
    def test_login_with_existent_user(self):
        # Создаем пользователя
        UserApi.create_user("chernyshina15fs@yandex.ru", "18031993", "Анастасия")

        # Логинимся как существующий пользователь
        response = UserApi.login_user("chernyshina15fs@yandex.ru", "18031993")

        assert response.status_code == 200  # SC_OK

        actual_status = response.json().get("success")
        expected_status = True  # В Python булевое значение True

        assert actual_status == expected_status

        # Удаляем пользователя после теста
        self.access_token = response.json().get("accessToken")
        UserApi.delete_user(self.access_token)

    @allure.title("Авторизация несуществующего пользователя")

    @allure.description("Тестирует авторизацию с использованием несуществующего пользователя.")
    def test_login_with_not_existent_user(self):
        # Логинимся как несуществующий пользователь
        response_email = UserApi.login_user("chernyshina15fs@yandex.ru", "18031993")

        assert response_email.status_code == 401  # SC_UNAUTHORIZED

        actual_error_email = response_email.json().get("message")
        expected_error_email = "email or password are incorrect"

        assert actual_error_email == expected_error_email

        # Логинимся с неправильным паролем для существующего пользователя
        response_password = UserApi.login_user("chernyshina15fs@yandex.ru", "18031993")

        assert response_password.status_code == 401  # SC_UNAUTHORIZED

        actual_error_password = response_password.json().get("message")
        expected_error_password = "email or password are incorrect"

        assert actual_error_password == expected_error_password


if __name__ == "__main__":
    import pytest

    pytest.main()