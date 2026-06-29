from partner.utils.JWTUtils import create_access_token

data = {
    "user":"admin",
    "pwd":"123"
}
print(create_access_token(data))