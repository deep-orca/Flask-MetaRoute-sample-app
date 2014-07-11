from flask.ext.metaroute import Controller, Route, Error


@Controller
class IndexController(object):

    @Route("/")
    def index(self):
        return "xxx"

    @Route("/test/<int:t>")
    def test2(self, t = 0):
        print("X %d" % t)
        return "test %d x" % t


