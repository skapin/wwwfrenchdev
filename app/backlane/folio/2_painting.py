
from backlane.classes import *


def painting(request, folio):

    return {"skills": folio._generate_skills(),
            "description": folio.description,
            "iframe": "/gallery/album/1/yggrasyl/"}


if __name__ != "__main__":
    def _start():
        painting_folio = Folio('Painting', '/static/img/drawing/pyramid.jpg', "My drawings and paintings.")
        painting_folio.add_skills([])

        FOLIO.registered_folio(painting_folio, painting)
    _start()
