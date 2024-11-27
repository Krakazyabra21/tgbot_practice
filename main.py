from config import api_key


from mubble import Token, API, Mubble

api = API(Token(api_key))
bot = Mubble(api)
