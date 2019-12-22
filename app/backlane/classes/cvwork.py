
from backlane.classes import *


class CvWork(object):
    def __init__(self, name, subname, date_from, date_to):
        self.skills = []
        self.name = name
        self.subname = subname
        self.date_from = date_from
        self.date_to = date_to
        self.description = "No Descr."

        self.knote_icon = "fa-suitcase"
        self.knote_class = "cvwork"
        self.links = []

    def set_description(self, description):
        self.description = description

    def add_link(self, link):
        self.links.append(link)

    def add_skill(self, skill):
        self.skills.append(skill)

    def _generate_knote(self):
        return '<div class="stop '+self.knote_class+'"><em class="fa '+self.knote_icon+'"></em></div>'

    def _generate_links(self):
        res = ''
        for l in self.links:
            res += '<a href="'+l+'"><button type="button" class="btn  btn-sm">'+l+'</button></a> '
        return res

    def _generate_skills(self):
        res = ''
        for s in self.skills:
            res += s.html()
        return res

    def html(self):
        html = ['<li>',
                self._generate_knote(),
                '<div class="box job-wrap"><div class="inner">',
                '<h2>'+self.name+'</h2>',
                '<h3>'+self.subname+'</h3><br>',
                '<p class="description">'+self.description+'</p>',
                self._generate_links(),
                '<div class="skills"><hr>',
                self._generate_skills(),
                '</div><br>',
                '<div class="label ng-binding">'+self.date_from+' - '+self.date_to+'</div>',
                '</div></li>']

        return ''.join(html)


class CvSchool(CvWork):
    def __init__(self, name, subname, date_from, date_to):
        CvWork.__init__(self, name, subname, date_from, date_to)
        self.knote_icon = "fa-graduation-cap"
        self.knote_class = "school"


class CvWorld(CvWork):
    def __init__(self, name, subname, date_from, date_to):
        CvWork.__init__(self, name, subname, date_from, date_to)
        self.knote_icon = "fa-globe"
        self.knote_class = "world"
