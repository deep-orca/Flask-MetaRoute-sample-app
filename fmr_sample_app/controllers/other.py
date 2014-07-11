from flask.ext.metaroute import Controller, Route, Error
from flask import abort


class SomeCustomException(Exception):
    pass


@Controller("/other")
class OtherController(object):

    @Route("/")
    def index(self):
        return "Other Index"

    @Route("/test/<int:t>")
    def test2(self, t = 0):
        return "Other Test %d" % t

    @Route("/dbd")
    def raiseDBD(self):
        x = 10 / 0
        return "not in reach"

    @Route("/abort/403")
    def raise403(self):
        abort(403)
        return "not in reach"

    @Route("/raise/sce")
    def raiseSCE(self):
        raise SomeCustomException()
        return "not in reach"

    @Error(Exception)
    def err(self, ex = None):
        return "err: " + repr(ex)

    @Error(403)
    def err403(self, ex):
        return "err403: " + repr(ex)

    @Error(404)
    def errNotFound(self, _):
        return "<<< Not Found >>>"

    @Error(SomeCustomException)
    def errSCE(self, ex):
        return "errSCE: " + repr(ex)