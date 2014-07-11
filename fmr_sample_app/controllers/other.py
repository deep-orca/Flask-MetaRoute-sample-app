from flask.ext.metaroute import Controller, Route, Error
from flask import abort


class SomeCustomException(Exception):
    pass


class SomeOtherCustomException(Exception):
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

    @Route("/raise/soce")
    def raiseSOCE(self):
        raise SomeOtherCustomException()
        return "not in reach"



    @Error(403, SomeOtherCustomException)
    def err403orSOCE(self, ex = None):
        return "err403orSOCE: " + repr(ex)

    @Error(404)
    def errNotFound(self, ex = None):
        return "<<< Not Found >>>"

    @Error(SomeCustomException)
    def errSCE(self, ex = None):
        return "errSCE: " + repr(ex)
