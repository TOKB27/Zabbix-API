import json
from dotenv import load_dotenv
import os
import zabbix_api_class

# .env ファイルから環境変数を読み込む
load_dotenv()

# Zabbix APIの共有情報を用意
api_url = os.getenv('ZBX_API_URL')
user_id = os.getenv('ZBX_USER')
password = os.getenv('ZBX_PASS')

# 取得対象のホストを指定する
hostname = 'HostA'

# API実行
api_module = zabbix_api_class.ZabbixApi(api_url, user_id, password, hostname)
zbx_auth = api_module.user_login_api()
data_host_get = api_module.host_get_api(zbx_auth)
data_proxy_get = api_module.proxy_get_api(zbx_auth)
data_trigger_get = api_module.trigger_get_api(zbx_auth)
