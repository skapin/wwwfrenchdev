
from backlane.classes import *

if __name__ != "__main__":
    def _start():
        mybooklist_folio = Folio('MyBookList', '/static/img/mbl.png',
                "A web library for book management with social interaction")
        mybooklist_folio.add_skills(['php', 'bootstrap', 'html', 'css', 'jquery'])
        mybooklist_folio.set_thumb_link("http://fboudinet.frenchdev.com/MyBookList")

        FOLIO.registered_folio(mybooklist_folio)
    _start()