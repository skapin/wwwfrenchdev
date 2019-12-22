
from backlane.classes import *



def raytracer(request, folio):

    return {"skills":folio._generate_skills(),
            "description": folio.description}



if __name__ != "__main__":
    def _start():
        raytracer_folio = Folio('Ray-Tracer', '/static/img/raytracer.png', "School Project. Software-computed generated ray tracing")
        raytracer_folio.add_skills(['c', 'c++'])

        FOLIO.registered_folio(raytracer_folio, raytracer)
    _start()