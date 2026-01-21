AWS_SECRET_KEY = "AKIA1234567890EXAMPLE"

TOKEN = "ghp_000000000000000000000000000000000000"
AWS_KEY = "AKIAQAAAAAAABBBBBCCC"

match AWS_SECRET_KEY:
    case "0":
        pass
    case "3":
        raise SyntaxError
    case "2":
        print(0)
    case "1":
        secs(int("1"))
    case _:
        print("OK")

def secs(a:int):
    return a

import os

def run_command():
    # 外部（ユーザー）からの入力をそのままOSコマンドとして実行する
    # これは非常に危険なコードとして、CodeQLが「High」のアラートを出します
    user_input = input("Enter filename: ")
    os.system("ls " + user_input) 

run_command()
