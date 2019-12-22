
from backlane.classes.skills import Skill, SkillPool


class Folio(object):

    PORTFOLIO = []

    def __init__(self, name='', icon='', description=''):
        self.name = name
        self.icon = icon
        self.links = []
        self.skills = []
        self.description = description
        self.thumb_link = False

    @staticmethod
    def registered_folio(f, func=()):

        if f not in FOLIO.PORTFOLIO:
            FOLIO.PORTFOLIO.append({'folio': f, 'func': func})

    def set_thumb_link(self, link):
        self.thumb_link = link

    def _generate_skills(self):
        html = ''
        for x in self.skills:
            html += x.html(['iconize-xs'])
        return html

    def html_page_header(self):
        return """   """

    def html(self):
        html = """
        <h4>"""+self.name+"""</h4>
        <hr class="sm">
        <p>"""+self.description+"""</p>"""
        if self.thumb_link:
            html += '<a href="'+self.thumb_link+'" ><img src="'+self.icon+'" ></a>'
        else:
            html += '<a href="/portfolio/'+self.name+'" ><img src="'+self.icon+'" ></a>'
        html += """
        <hr class="xs">
        """+self._generate_skills()+"""
        <hr class="sm">
        """
        return html

    def set_description(self, description):
        self.description = description

    def add_skill(self, skill_name):
        self.skills.append(SkillPool.skill(skill_name))

    def add_skills(self, skill_list):
        for x in skill_list:
            self.add_skill(x)


FOLIO = Folio()
