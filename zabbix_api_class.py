import json
import requests

class ZabbixApi:
    def __init__(self, api_url, user_id, password, hostname):
        self.api_url = api_url
        self.user_id = user_id
        self.password = password
        self.hostname = hostname
        self.headers = {
            'Content-Type': 'application/json-rpc',
        }
    def user_login_api(self):  # ユーザー認証トークン取得API
        user_login_parameter = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {"user": self.user_id, "password": self.password},
            "id": 1,
        }
        user_login = json.dumps(user_login_parameter)
        response_user_login = requests.post(
            self.api_url, headers=self.headers, data=user_login)
        data_user_login = response_user_login.json()
        if 'error' in data_user_login:
            return data_user_login['error']
        zbx_auth = data_user_login['result']
        return zbx_auth
      
    def host_get_api(self, zbx_auth):  # ホスト情報取得API
        host_get_parameter = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": "extend",
                "selectProxy": "extend",
                "selectParentTemplates": "extend",
                "selectItems": "extend",
                "selectTriggers": "extend",
                "selectInterfaces": "extend",
                "selectGroups": "extend",
                "selectMacros": "extend",
                "selectTags": "extend",
                "filter": {
                    "host": [
                        self.hostname
                    ]
                }
            },
            "id": 1,
            "auth": zbx_auth
        }
        host_get = json.dumps(host_get_parameter)
        response_host_get = requests.post(
            self.api_url, headers=self.headers, data=host_get)
        data_host_get = response_host_get.json()
        return data_host_get
      
    def proxy_get_api(self, zbx_auth):  # プロキシ情報取得API
        host_get_parameter = {
            "jsonrpc": "2.0",
            "method": "proxy.get",
            "params": {
                "output": "extend",
            },
            "id": 1,
            "auth": zbx_auth
        }
        proxy_get = json.dumps(host_get_parameter)
        response_proxy_get = requests.post(
            self.api_url, headers=self.headers, data=proxy_get)
        data_proxy_get = response_proxy_get.json()
        return data_proxy_get
      
    def trigger_get_api(self, zbx_auth):  # トリガー情報取得API
        parameter = {
            "jsonrpc": "2.0",
            "method": "trigger.get",
            "params": {
                "output": "extend",
                "selectFunctions": "extend",
                "expandExpression": "true",
                "selectTags": "extend",
                "filter": {
                    "host": self.hostname
                },
            },
            "id": 1,
            "auth": zbx_auth
        }
        trigger_get = json.dumps(parameter)
        response_trigger_get = requests.post(
            self.api_url, headers=self.headers, data=trigger_get)
        data_trigger_get = response_trigger_get.json()
        return data_trigger_get
