
from backlane.classes import *



def drone(request, folio):

    return {"skills":folio._generate_skills(),
            "description": folio.description}



if __name__ != "__main__":
    def _start():
        drone_folio = Folio('Drones', '' , "My drone related files, pictures and videos")
        drone_folio.add_skills(['drone'])
        FOLIO.registered_folio(drone_folio, drone)
    _start()