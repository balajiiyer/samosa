import falcon


class UserStatsResource:
    def on_get(self, req, resp):
        pass


class UserRegisterResource:
    def on_post(self, req, resp):
        pass

app = falcon.APT()

user_stats = UserStatsResource()
register_samosa = UserRegisterResource()

app.add_route('/stats', user_stats)
app.add_route('/user', register_samosa)