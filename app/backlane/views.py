from django.http import HttpResponse
from django.views.generic import *
from django.shortcuts import render_to_response
from backlane.classes import *
from backlane.folio import *


def home(request):
    return HttpResponse("My WebSite")


def folio(request, name):
    params = {}
    title = name
    params['title'] = title
    for k in Folio.PORTFOLIO:
        if k['folio'].name.lower() == name.lower():
            params.update(k['func'](request, k['folio']))

    return render_to_response('backlane/folio.html', params)


def cv(request):
    work_list = []
    html_works = []

    aio_5 = CvWork('AIO', 'Community Platform', 'Jan 2019', 'Current')
    aio_5.add_skill(SkillPool.skill('magento'))
    aio_5.add_skill(SkillPool.skill('prestashop'))
    aio_5.add_skill(SkillPool.skill('docker'))
    aio_5.add_skill(SkillPool.skill('ariba'))
    aio_5.add_skill(SkillPool.skill('seo'))
    aio_5.add_skill(SkillPool.skill('php'))
    aio_5.add_skill(SkillPool.skill('html'))
    aio_5.add_skill(SkillPool.skill('css'))
    aio_5.add_skill(SkillPool.skill('ops'))
    aio_5.set_description(""" Design, code, test & deploy B2B & B2C e-commerce platform.
    -> Set-based between PrestaShop, Magento & wooCommerce
    -> Create test enviroment & production env. for Magento2 (using docker & git)
    -> Setup Punch-Out Catalogue for Ariba 
    -> Backup + CI pipeline
    -> Add Redis+Varnish caceh system 
    -> Apply, and customize theme to match our needs
    -> Find and deploy extensions
    -> Create analytics & export/improt data scripts
    """)

    aio_4 = CvWork('AIO', 'R&D', 'Aug 2018', 'Current')
    aio_4.add_skill(SkillPool.skill('documentation'))
    aio_4.add_skill(SkillPool.skill('c++'))
    aio_4.add_skill(SkillPool.skill('lean'))
    aio_4.add_skill(SkillPool.skill('management'))
    aio_4.set_description(""" NDA """)

    aio_3 = CvWork('AIO', 'AGV', 'October 2018', 'Current')
    aio_3.add_skill(SkillPool.skill('c++'))
    aio_3.add_skill(SkillPool.skill('arduino'))
    aio_3.add_skill(SkillPool.skill('vuejs'))
    aio_3.add_skill(SkillPool.skill('electronic'))
    aio_3.add_skill(SkillPool.skill('mechanical'))
    aio_3.add_skill(SkillPool.skill('3dprinter'))
    aio_3.add_skill(SkillPool.skill('mobile'))
    aio_3.add_skill(SkillPool.skill('API'))
    aio_3.set_description(
        """ Add Wi-Fi hotspot on our AGV. Provide API and mobile application to remote control the AGV easily. """)

    aio_2 = CvWork('AIO', 'Kanban Tools', 'March 2018', 'Current')
    aio_2.add_skill(SkillPool.skill('python'))
    aio_2.add_skill(SkillPool.skill('docker'))
    aio_2.add_skill(SkillPool.skill('vuejs'))
    aio_2.add_skill(SkillPool.skill('postgres'))
    aio_2.add_skill(SkillPool.skill('ops'))
    aio_2.set_description(""" Tool around kanban for the supply-chain.
        -> Andon system to check OK/NOK situation
        -> Generate documents for productions with scanning system
        -> Analytics""")

    aio_1 = CvWork('AIO', 'Product Owner Numii', 'March 2018', 'Current')
    aio_1.add_skill(SkillPool.skill('python'))
    aio_1.add_skill(SkillPool.skill('c++'))
    aio_1.add_skill(SkillPool.skill('vuejs'))
    aio_1.add_skill(SkillPool.skill('postgres'))
    aio_1.add_skill(SkillPool.skill('influxdb'))
    aio_1.add_skill(SkillPool.skill('docker'))
    aio_1.add_skill(SkillPool.skill('ai'))
    aio_1.add_skill(SkillPool.skill('mobile'))
    aio_1.add_skill(SkillPool.skill('management'))
    aio_1.add_skill(SkillPool.skill('lean'))
    # aio_1.add_skill(SkillPool.skill('tableau'))
    aio_1.set_description(""" Product Owner for Numii. 
    Numii is the new scale for healthier workplaces, through the use of artificial intelligence. 
    Featuring connected beacons, this swarm intelligence is creating the world’s first labour health database.
    
    We allow CSR-conscious companies to imagine strategies made around health at work and, 
    more broadly, allows us to imagine decent jobs for all of us. 
    Creating digital factory twins gives a detailed view of good work practices, 
    helping to pinpoint where hazards are. The Numii scale becomes part of the factory of the future, 
    plants who truly wish to put humans in the center of their choices.
    
    """)
    work_list.append(aio_5)
    work_list.append(aio_4)
    work_list.append(aio_3)
    work_list.append(aio_2)
    work_list.append(aio_1)

    waycom_4 = CvWork('Waycom', 'Concept & Develop New SI', 'March 2015', 'Feb 2016')
    waycom_4.add_skill(SkillPool.skill('python'))
    waycom_4.add_skill(SkillPool.skill('django'))
    waycom_4.add_skill(SkillPool.skill('angularjs'))
    waycom_4.add_skill(SkillPool.skill('postgres'))
    waycom_4.add_skill(SkillPool.skill('bootstrap'))
    waycom_4.add_skill(SkillPool.skill('docker'))
    waycom_4.add_skill(SkillPool.skill('jwt'))
    waycom_4.set_description(""" Design and develop new front-end and back-end stacks
    The idea is to develop severals micro-service as back-end and 2-3 front as portail which request back-end with REST API.
    - Python + Django + DRF as back-end
    <br>

    - Angualrjs + bootstrap as front-end
    - Common skeleton for each backend skeleton
    - Common skeleton for each frotn end with same visual, component, core and settings
    - Authentication systeme using a JSONWebToken(JWT) forged using pub/priv keys by a back-end interfacing a SAML/SSO core
    - Front and Back are develop and deployed using Docker""")
    work_list.append(waycom_4)

    waycom_3 = CvWork('Waycom', 'Calendar, Dayoff& On Call Tool', 'May 2015', 'August')
    waycom_3.add_skill(SkillPool.skill('python'))
    waycom_3.add_skill(SkillPool.skill('angularjs'))
    waycom_3.add_skill(SkillPool.skill('docker'))
    waycom_3.add_skill(SkillPool.skill('bootstrap'))
    waycom_3.add_skill(SkillPool.skill('mysql'))
    waycom_3.add_skill(SkillPool.skill('ldap'))
    waycom_3.set_description("""Created internal tool for dayoff, on call and team management based on LDAP. 
- The tool allow users to ask and manage their holiday and give better visibility for manager. 
- Directors can export user's holliday of the month.
- On call are assigned dynamicly by an algorythm but let the user trade dates with others and manage law-constrainte (not two week in a raw, no holliday etc...)
- Dayoff are sync. with Outlook calendar
- User can see validated dayoff of their direct manager and member of their teams.""")

    work_list.append(waycom_3)

    waycom_2 = CvWork('Waycom', 'Router Provisioning Tool', 'April 2015', ' Oct 2017')
    waycom_2.add_skill(SkillPool.skill('python'))
    waycom_2.add_skill(SkillPool.skill('angularjs'))
    # waycom_2.add_skill(SkillPool.skill('twing'))
    waycom_2.add_skill(SkillPool.skill('bootstrap'))
    waycom_2.add_skill(SkillPool.skill('git'))
    waycom_2.add_skill(SkillPool.skill('network'))
    waycom_2.set_description("""Created internal tool for automatic router provisioning
        """)

    work_list.append(waycom_2)

    waycom_1 = CvWork('Waycom', 'Firewall Configurator', 'October 2015', ' May 2016')
    waycom_1.add_skill(SkillPool.skill('python'))
    waycom_1.add_skill(SkillPool.skill('angularjs'))
    waycom_1.add_skill(SkillPool.skill('postgres'))
    waycom_1.add_skill(SkillPool.skill('bootstrap'))
    waycom_1.add_skill(SkillPool.skill('confluence'))
    waycom_1.add_skill(SkillPool.skill('git'))
    waycom_1.add_skill(SkillPool.skill('sublime'))
    waycom_1.add_skill(SkillPool.skill('debian'))
    waycom_1.add_skill(SkillPool.skill('network'))
    waycom_1.set_description("""
        Internal tool for easy firewall configuration and backup.<br><br>
        I develloped all the software (from scratch), the design, database structure to python parser.
        HTTP Daemon written in Python and WebInterface for Firewall configuration.<br><br>
        WaycomFirewall (WFW) provide a WebInterface to end-user for rule creation and display on Waycom firewall hardware.<br>
        - Targeted firewall: JunOS/ScreenOS/PaloAlto <br>
        """)
    work_list.append(waycom_1)

    teacher = CvWork('Teacher', 'Software Teacher', '2014', ' 2015')
    teacher.add_skill(SkillPool.skill('3dprinter'))
    teacher.add_skill(SkillPool.skill('python'))
    teacher.add_skill(SkillPool.skill('drone'))
    teacher.set_description("""
        Secondary school teacher (Lestonnac, Bordeaux). Student learn how to build a LEGO (NTX) robot and contol them with a computer. Student went to the 1st Robot Maker's Day tournament and to the FirstLegoLeague.<br>
        Python, CAO, 3D Printer, mechanical and programming course.
        """)
    teacher.add_link('http://www.firstlegoleague.org')
    teacher.add_link('http://robotmakersday.fr')
    work_list.append(teacher)

    polybox = CvWork('Polybox3D', 'CEO & Engineer', 'August 2013', ' October 2015')
    polybox.set_description(""" Co-creator of Polybox3D.
        Polybox 3D is a innovative multifunctions machine.<br>
        The concept of Polybox is to integrate 4 main functions:
        <br><br>
            * 5 axis CNC high precision <br>
            * 3D print<br>
            * 3D scan<br>
            * Pictures & videos shooting<br>
            <br>
        - Dev. Control center, with touchscreen UI, RealTime linux, AVR/ARM firmware, bash scripts, pythons software, C++/Qt software, CNC software, 3D scanner software, ...<br>
        - Business Management, from idea to start-up<br>
        - Writting Requirements Specification<br>
        - IT manager, machine to company materials (network setup, mail server, NAS, wiki, backup, desktop installation, ...)<br>
        - In charge of all the communication part: Logo design, graphic theme, website, pictures, community manager ...<br>
        - Help for mechanical CAD design and production (milling / drilling / commands)<br>
        - Help electronic production: SMT soldering, testing and inventory management<br>
        - And way more skills!<br>
        """)
    polybox.add_skill(SkillPool.skill('c++'))
    polybox.add_skill(SkillPool.skill('arduino'))
    polybox.add_skill(SkillPool.skill('qt'))
    polybox.add_skill(SkillPool.skill('embedded'))
    polybox.add_skill(SkillPool.skill('3dprinter'))
    polybox.add_skill(SkillPool.skill('inkscape'))
    polybox.add_skill(SkillPool.skill('shell'))
    polybox.add_skill(SkillPool.skill('python'))
    polybox.add_skill(SkillPool.skill('opensource'))
    polybox.add_skill(SkillPool.skill('management'))
    polybox.add_link('https://twitter.com/polybox3d')
    polybox.add_link('https://www.facebook.com/Polybox3D/')
    polybox.add_link('https://www.facebook.com/Polybox3D/')
    polybox.add_link('https://github.com/polybox3d')
    work_list.append(polybox)

    viti = CvWork('Vitirover', 'Internship', 'February 2013', 'August 2013')
    viti.add_skill(SkillPool.skill('embedded'))
    viti.add_skill(SkillPool.skill('c++'))
    viti.add_skill(SkillPool.skill('qt'))
    viti.add_skill(SkillPool.skill('arduino'))
    viti.add_skill(SkillPool.skill('3dprinter'))
    # viti.add_skill(SkillPool.skill('vhdl'))
    viti.add_link('http://www.vitirover.com')
    viti.set_description("""
        A revolutionary agroecological robots, to reduce professional risk, phytosanitary inputs and costs.<br>
        - VHDL motor component for the rover (FPGA chip)<br>
        - Study on kinect captor and other telemetry system<br>
        - QSIG data creator for GPS positionning <br>
        - 3D printer construction + customisation<br>
        """)
    work_list.append(viti)

    servelots = CvWorld('Servelots (India)', 'International Internship', 'June 2012', 'August 2012')
    servelots.add_skill(SkillPool.skill('firefox'))
    servelots.add_skill(SkillPool.skill('html'))
    servelots.add_skill(SkillPool.skill('css'))
    servelots.add_skill(SkillPool.skill('mongodb'))
    servelots.add_skill(SkillPool.skill('git'))
    servelots.add_link('http://servelots.com/new/3d.html')
    servelots.set_description("""
        Servelots is a web service provider for Small to Medium Enterprises.<br>
        - SEO Web<br>
        - Firefox plugin for live website renarration<br>
        - RDF components <br>
        - Renarration website + API<br>
        """)
    work_list.append(servelots)

    enseirb = CvSchool('ENSEIRB-MATMECA', 'Master\'s Degree in Engineering', '2010', '2013')
    enseirb.add_skill(SkillPool.skill('c++'))
    enseirb.add_skill(SkillPool.skill('c'))
    enseirb.add_skill(SkillPool.skill('database'))
    enseirb.add_skill(SkillPool.skill('php'))
    enseirb.add_skill(SkillPool.skill('network'))
    enseirb.add_skill(SkillPool.skill('python'))
    enseirb.add_skill(SkillPool.skill('assembly'))
    enseirb.add_skill(SkillPool.skill('management'))
    enseirb.add_skill(SkillPool.skill('money'))
    enseirb.add_link('http://www.enseirb-matmeca.fr/en')
    enseirb.set_description("""
        ENSEIRB-MATMECA is one of the 8 graduate schools of Bordeaux INP, specialized in complex systems design.<br><br>
        COMPUTER SCIENCE DEPARTMENT<br>
        - Theoretical and technical foundations of computing<br>
        - Project management and IT fot the corporate world<br>
        - Software development<br>
        - Distributed networks and systems<br>
        - Parallel and distributed computing<br>
        - Robotics & embedded system<br>
        - Software verification and dependability<br>
        """)

    work_list.append(enseirb)

    openflyers = CvWork('OpenFlyers', 'Intership', 'May 2010', ' August 2010')
    openflyers.add_skill(SkillPool.skill('php'))
    openflyers.add_skill(SkillPool.skill('c++'))
    openflyers.add_skill(SkillPool.skill('qt'))
    openflyers.add_skill(SkillPool.skill('asterisk'))
    openflyers.add_skill(SkillPool.skill('mysql'))
    openflyers.add_skill(SkillPool.skill('network'))
    openflyers.add_link('https://openflyers.com')
    openflyers.set_description("""
        Transport companiy on demand, training organization, rental company,
        flying club, sailing club, driving school.
        OpenFlyers the business management software coming from aeronautics.
        <br><br>
        - Worked on Asterisk server (SIP), setup phone call script with DB interaction<br>
        - Reworked call center Software<br>
        - Create PHP API for Asterisk and CallCenter<br>
        - Security research & network for daily database broadcast between each server<br>
        """)
    work_list.append(openflyers)

    freelance = CvWork('Technical Manager', 'Freelance', '2009', ' August 2010')
    freelance.add_skill(SkillPool.skill('wordpress'))
    freelance.add_skill(SkillPool.skill('css'))
    freelance.add_skill(SkillPool.skill('html'))
    freelance.add_skill(SkillPool.skill('php'))
    freelance.set_description("""
        Charge of technique, remote work for a project manager<br>
         - Design, improvement, and web sites's optimization<br>
         - Implementation and integration of graphic design by CSS<br>
         - Development of technical solutions for the SEO<br>
        """)
    work_list.append(freelance)

    iut = CvSchool('Software Institute (IUT BX1)', 'BTEC Higher National Diploma', '2008', '2010')
    iut.add_skill(SkillPool.skill('c'))
    iut.add_skill(SkillPool.skill('c++'))
    iut.add_skill(SkillPool.skill('qt'))
    iut.add_skill(SkillPool.skill('database'))
    iut.add_skill(SkillPool.skill('network'))
    iut.add_link('http://www.iut.u-bordeaux.fr/info')
    iut.set_description("""
        COMPUTER SCIENCE UNIVERSITY<br>
        - Theoretical and technical foundations of computing<br>
        - Software development C/C++<br>
        - Networks Basics<br>
        - Parallel and distributed computing<br>
        - Software verification<br>
        """)
    work_list.append(iut)

    for x in work_list:
        html_works.append(x.html())

    return render_to_response('backlane/cv.html', {'works':  html_works})


def portfolio(request):
    html_folio = []
    for x in FOLIO.PORTFOLIO:
        html_folio.append(x['folio'].html())

    return render_to_response('backlane/portfolio.html', {'folio':  html_folio})


def generate_label(percent):
    if percent <= 20:
        return 'basics'
    elif percent <= 40:
        return 'medium'
    elif percent <= 60:
        return 'good'
    elif percent <= 80:
        return 'strong'
    elif percent <= 90:
        return 'high'
    elif percent <= 100:
        return 'expert'
    return ' '


def pieify(s, percent):
    html = """
    <span class="skillthum">
        <div data-percent=" """+str(percent)+""" " class="chart easyPieChart chart140">
        """+s.html(['iconize-md'])+"""
        <p class="pourcentlabel">"""+generate_label(percent)+"""</>
        </div>
        <!--<p class="text-center chart-text"></p>-->
    </span>
    """
    return html


def skills(request):
    prog_skills = []
    hard_skills = []
    web_skills = []
    tools_skills = []

    prog_skills.append(pieify(SkillPool.skill('c++'), 80))
    prog_skills.append(pieify(SkillPool.skill('c'), 80))
    prog_skills.append(pieify(SkillPool.skill('database'), 80))
    prog_skills.append(pieify(SkillPool.skill('qt'), 70))
    prog_skills.append(pieify(SkillPool.skill('python'), 50))
    prog_skills.append(pieify(SkillPool.skill('shell'), 40))

    hard_skills.append(pieify(SkillPool.skill('3dprinter'), 100))
    hard_skills.append(pieify(SkillPool.skill('arduino'), 95))
    hard_skills.append(pieify(SkillPool.skill('embedded'), 65))
    hard_skills.append(pieify(SkillPool.skill('raspberry'), 60))
    hard_skills.append(pieify(SkillPool.skill('drone'), 40))

    web_skills.append(pieify(SkillPool.skill('html'), 80))
    web_skills.append(pieify(SkillPool.skill('bootstrap'), 65))
    web_skills.append(pieify(SkillPool.skill('angularjs'), 55))
    web_skills.append(pieify(SkillPool.skill('css'), 50))
    web_skills.append(pieify(SkillPool.skill('php'), 45))
    web_skills.append(pieify(SkillPool.skill('jquery'), 15))

    tools_skills.append(pieify(SkillPool.skill('git'), 90))
    tools_skills.append(pieify(SkillPool.skill('sublime'), 85))
    tools_skills.append(pieify(SkillPool.skill('mysql'), 60))
    tools_skills.append(pieify(SkillPool.skill('postgres'), 60))
    tools_skills.append(pieify(SkillPool.skill('inkscape'), 40))
    tools_skills.append(pieify(SkillPool.skill('photoshop'), 25))
    tools_skills.append(pieify(SkillPool.skill('asterisk'), 10))

    return render_to_response('backlane/skills.html', {'programming':  prog_skills,
                                                       'hardware':  hard_skills,
                                                       'web':  web_skills,
                                                       'tools':  tools_skills})
