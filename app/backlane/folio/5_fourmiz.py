
from backlane.classes import *



def fourmiz(request, folio):

    return {"skills":folio._generate_skills(),
            "description": folio.description}



if __name__ != "__main__":
    def _start():
        fourmiz_folio = Folio('FourmiZ', '/static/img/fourmiz.png', " School Project. Ants life simulation, 2D & 3D")
        fourmiz_folio.add_skills(['c', 'c++'])

        FOLIO.registered_folio(fourmiz_folio, fourmiz)
    _start()