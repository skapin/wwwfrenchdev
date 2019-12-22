
from backlane.classes import *



def printer3d(request, folio):

    return {"skills":folio._generate_skills(),
            "description": folio.description}



if __name__ != "__main__":
    def _start():
        printer3d_folio = Folio('3D Printer', '', "My personal homemade 3D Printer (FFF/FDM)")
        printer3d_folio.add_skills(['3dprinter', 'arduino', 'embedded'])

        FOLIO.registered_folio(printer3d_folio, printer3d)
    _start()