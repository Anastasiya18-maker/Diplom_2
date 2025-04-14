import requests
import json
from URL import UsedUrl


class UserApi:
    @staticmethod
    def create_user(email, password, name):
        data_for_registration_user = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(
            UsedUrl.URL_CREATE_USER,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data_for_registration_user)
        )

        return response
    @staticmethod
    def delete_user(access_token):
        response = requests.delete(
            UsedUrl.URL_DELETE,
            headers={"Authorization": access_token}
        )
        return response

    @staticmethod
    def login_user(email, password):
        data_for_login = {
            "email": email,
            "password": password
        }

        response = requests.post(
            UsedUrl.URL_LOGIN_USER,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data_for_login)
        )
        return response

    @staticmethod
    def edit_user(email, password, access_token):
        data_for_login = {
            "email": email,
            "password": password
        }
        response = requests.patch(
            UsedUrl.URL_EDIT_USER,  # Здесь должен быть правильный URL для редактирования пользователя
            headers={
                "Authorization": access_token,
                "Content-Type": "application/json"
            },
            data=json.dumps(data_for_login)
        )
        return response