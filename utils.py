import configparser
import os.path

father_path = os.path.dirname(os.path.abspath(__file__))

now_path = os.path.join(father_path, "imgs.png")

utils_path = os.path.join(father_path, "utils.ini")
# print(now_path)

config_path = configparser.ConfigParser()

config_path.read(utils_path, encoding="utf-8")

pick = config_path.get("pick", "env")

tenantcode = config_path.get(pick, "tenantcode")
env = config_path.get(pick, "env")
password = config_path.get(pick, "password")
account = config_path.get(pick, "account")
print(pick, env, tenantcode, account, password)
