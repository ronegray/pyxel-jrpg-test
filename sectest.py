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

def secs(a:int):
    return a

