

class Skill(object):
    def __init__(self, name, icon, description=False):
        self.name = name
        self.icon = icon
        if description:
            self.description = description
        else:
            self.description = name.capitalize()

    def html(self, extra_class=['iconize-sm']):
        return ('<em class="' +
                self.icon +
                ' ' +
                ' '.join(extra_class) +
                '" data-toggle="tooltip" data-placement="bottom" title="' +
                self.description +
                '"></em>')


class SkillPool(object):
    SKILLS = []

    def __init__(self):
        SkillPool.SKILLS.append(Skill('python', 'icon-python'))
        SkillPool.SKILLS.append(Skill('c', 'icon-c', 'C'))
        SkillPool.SKILLS.append(Skill('c++', 'icon-cplusplus', 'C++'))
        SkillPool.SKILLS.append(Skill('qt', 'stax-qt', 'Qt Framework'))
        SkillPool.SKILLS.append(Skill('shell', 'icon-shell', 'Script Shell'))
        SkillPool.SKILLS.append(Skill('database', 'icon-database', 'SQL & Database'))
        SkillPool.SKILLS.append(Skill('docker', 'stax-docker', 'Docker'))
        SkillPool.SKILLS.append(Skill('jwt', 'fa fa-asterisk', 'JSon Web Token'))
        SkillPool.SKILLS.append(Skill('vuejs', 'stax-vuejs', 'Vue.js'))

        SkillPool.SKILLS.append(Skill('raspberry', 'icon-rasbaerrypi', 'Raspberry'))
        SkillPool.SKILLS.append(Skill('arduino', 'stax-arduino', 'Arduino'))
        SkillPool.SKILLS.append(Skill('embedded', 'stax-chip', 'Embedded Systeme (AVR/ARM/FPGA/RealTime)'))
        SkillPool.SKILLS.append(Skill('3dprinter', 'stax-3dprinter2', '3D Printer & 3D Scanner'))
        SkillPool.SKILLS.append(Skill('drone', 'fa fa-space-shuttle', 'Drone & Hobby'))

        SkillPool.SKILLS.append(Skill('php', 'icon-php', 'PHP'))
        SkillPool.SKILLS.append(Skill('perl', 'icon-perl', 'Perl'))
        SkillPool.SKILLS.append(Skill('bootstrap', 'icon-bootstrap', 'Bootstrap 3.x'))
        SkillPool.SKILLS.append(Skill('css', 'icon-css3-alt', 'CSS'))
        SkillPool.SKILLS.append(Skill('html', 'icon-html5', 'HTML'))
        SkillPool.SKILLS.append(Skill('angularjs', 'icon-angular', 'AngularJS'))
        SkillPool.SKILLS.append(Skill('jquery', 'icon-jquery-alt', 'JQuery'))
        SkillPool.SKILLS.append(Skill('django', 'icon-jquery-alt', 'Django'))
        SkillPool.SKILLS.append(Skill('ldap', 'icon-database', 'LDAP'))

        SkillPool.SKILLS.append(Skill('mysql', 'icon-mysql-alt', 'JQuery'))
        SkillPool.SKILLS.append(Skill('postgres', 'icon-postgres', 'PostGresql'))
        SkillPool.SKILLS.append(Skill('mongodb', 'icon-mongodb', 'MongoDB'))
        SkillPool.SKILLS.append(Skill('symfony', 'stax-symfony', 'Symfony'))
        SkillPool.SKILLS.append(Skill('git', 'icon-git', 'Git'))
        SkillPool.SKILLS.append(Skill('sublime', 'icon-sublime', 'Sublime Text Editor'))
        SkillPool.SKILLS.append(Skill('photoshop', 'icon-photoshop', 'Photoshop'))
        SkillPool.SKILLS.append(Skill('confluence', 'icon-confluence', 'Confluence'))
        SkillPool.SKILLS.append(Skill('inkscape', 'stax-inkscape', 'Inkscape (Vector Drawing)'))
        SkillPool.SKILLS.append(Skill('debian', 'icon-debian', 'Debian'))
        SkillPool.SKILLS.append(Skill('opensource', 'icon-opensource', 'OpenSource Project'))
        SkillPool.SKILLS.append(Skill('firefox', 'fa fa-firefox', 'Firefox Plugin'))
        SkillPool.SKILLS.append(Skill('network', 'fa fa-wifi', 'Network Knowledge'))
        SkillPool.SKILLS.append(Skill('assembly', 'fa fa-gears', 'Assembly'))
        SkillPool.SKILLS.append(Skill('asterisk', 'fa fa-asterisk', 'Asterisk SIP/PABX'))
        SkillPool.SKILLS.append(Skill('wordpress', 'icon-wordpress', 'Wordpress'))

        SkillPool.SKILLS.append(Skill('management', 'fa fa-users', 'Management'))
        SkillPool.SKILLS.append(Skill('money', 'fa fa-euro', 'Accounting'))

        SkillPool.SKILLS.append(Skill('magento', 'icon-magento ', 'Accounting'))
        SkillPool.SKILLS.append(Skill('prestashop', 'fa fa-shopping-bag ', 'Prestashop'))
        SkillPool.SKILLS.append(Skill('ariba', 'stax-ariba ', 'Ariba SAP'))
        SkillPool.SKILLS.append(Skill('seo', 'fa google ', 'SEO'))
        SkillPool.SKILLS.append(Skill('ops', 'icon-ec3 ', 'Ops'))
        SkillPool.SKILLS.append(Skill('documentation', 'icon-confluence', 'Documentation'))
        SkillPool.SKILLS.append(Skill('lean', 'icon-phonegap', 'Lean'))
        SkillPool.SKILLS.append(Skill('electronic', 'fa fa-usb', 'Electronics'))
        SkillPool.SKILLS.append(Skill('mechanical', 'fa fa-gears', 'Mechanical'))
        SkillPool.SKILLS.append(Skill('mobile', 'fa fa-mobile', 'Mobile'))
        SkillPool.SKILLS.append(Skill('API', 'stax-api', 'API'))
        SkillPool.SKILLS.append(Skill('influxdb', 'icon-database', 'InfluxDB'))
        SkillPool.SKILLS.append(Skill('ai', 'stax-ai', 'A.I'))

    @staticmethod
    def skill(name):
        for s in SkillPool.SKILLS:
            if s.name == name:
                return s
        raise ValueError('Skill not defined')


skillpool = SkillPool()