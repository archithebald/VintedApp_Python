from utils import cookies
from app.api.search import search

auth = cookies.load_auth_cookie()

c = {
    auth[0]: auth[1]
}

search(cookies=c, page=1)