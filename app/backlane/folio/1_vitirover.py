
from backlane.classes import *



def vitirover(request, folio):

    return {"skills":folio._generate_skills(),
            "description": folio.description}



if __name__ != "__main__":
    def _start():
        vitirover_folio = Folio('Vitirover',
                '/static/img/vitirover-thumb.png',
                "Vine field simulation with moving robotic mower")
        vitirover_folio.add_skills(['c++', 'qt'])

        FOLIO.registered_folio(vitirover_folio, vitirover)
    _start()