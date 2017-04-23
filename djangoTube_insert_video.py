import requests


class Post_new_video:
    def __init__(self):
        self.setup()

    def setup(self):
        self.br = requests.Session()
        res = self.br.get("http://127.0.0.1:8000/video/new")
        self.token = res.cookies['csrftoken']


    def post(self, title, key):
        data = {'csrfmiddlewaretoken': self.token,
        'title': title,
        'key':key,}

        return self.br.post("http://127.0.0.1:8000/video/new", data)

