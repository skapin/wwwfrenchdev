
from backlane.classes import *



def networksimulation(request, folio):

    return {"skills":folio._generate_skills(),
            "description": folio.description}



if __name__ != "__main__":
    def _start():
        networksimulation_folio = Folio('NetworkSimulation', '/static/img/ns.png', "School project for large network congestion simulation with data visualization")
        networksimulation_folio.add_skills(['c++', 'qt'])

        FOLIO.registered_folio(networksimulation_folio, networksimulation)
    _start()