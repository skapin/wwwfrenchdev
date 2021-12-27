
from backlane.classes import *



def polybox3d(request, folio):

    return {"skills":folio._generate_skills(),
            "description": folio.description}



if __name__ != "__main__":
    def _start():
        polybox3d_folio = Folio('Polybox3D',
                    '/static/img/polybox_1.jpg',
                    """An innovative multifunctions machine:
                    5 axis CNC high precision, 3D print, 3D scan & recording""")
        polybox3d_folio.add_skills(['3dprinter', 'embedded', 'c++', 'qt', 'arduino'])
        polybox3d_folio.set_thumb_link("http://polybox3d.wixsite.com/polybox/")
        FOLIO.registered_folio(polybox3d_folio, polybox3d)
    _start()