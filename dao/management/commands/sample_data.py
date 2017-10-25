from django.core.files import File
from django.core.management import BaseCommand

from dao.models import *
from geoposition.fields import Geoposition
import os
import requests
import tempfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.generate_countries()
        self.generate_contacts()
        self.generate_careers()
        self.generate_clients()
        self.generate_events()
        self.generate_expertise()
        self.generate_business_domains()

    def download_file_from_url(self, url):
        filename = os.path.basename(url)
        try:
            request = requests.get(url, stream=True)
        except requests.exceptions.RequestException as e:
            return None
        if request.status_code != requests.codes.ok:
            return None
        lf = tempfile.NamedTemporaryFile()
        for block in request.iter_content(1024 * 8):
            if not block:
                break
            lf.write(block)

        return filename, File(lf)

    def store_image(self, image):
        filename = os.path.basename(image)
        image_obj, created = Image.objects.get_or_create(
            image=filename,
            defaults={
                'image': filename
            }
        )
        if created:
            image_obj.image.save(filename, self.download_file_from_url(image)[1], save=True)
        return image_obj

    def create_images(self, images):
        result = []
        for image in images:
            result.append(self.store_image(image))
        return result

    def generate_countries(self):
        country, created = Country.objects.update_or_create(
            iso='de',
            defaults={
                'name': 'Germany',
            }
        )
        if created:
            image = self.download_file_from_url('http://flags.fmcdn.net/data/flags/w1160/de.png')
            country.flag.save(image[0], image[1], save=True)

        country, created = Country.objects.update_or_create(
            iso='ro',
            defaults={
                'name': 'Romania',
            }
        )
        if created:
            image = self.download_file_from_url('http://flags.fmcdn.net/data/flags/w1160/ro.png')
            country.flag.save(image[0], image[1], save=True)

    def generate_contacts(self):
        Contact.objects.update_or_create(
            city='Munchen',
            defaults={
                'name': 'DialogData GmbH & Co. KG',
                'coordinates': Geoposition(48.13873204565224, 11.527860760688782),
                'country': Country.objects.get(iso='de'),
                'city': 'Munchen',
                'address': 'Barthstr. 18',
                'postal_code': '80339',
                'phone': '+498989058950',
                'fax': '+4989890589599',
                'email': 'munich@dialogdata.de'
            }
        )
        Contact.objects.update_or_create(
            city='Berlin',
            defaults={
                'name': 'DialogData GmbH & Co. KG',
                'coordinates': Geoposition(52.5341205, 13.3950019),
                'country': Country.objects.get(iso='de'),
                'city': 'Berlin',
                'address': 'Anklamer Straße 5',
                'postal_code': '10115',
                'phone': '+4917623589396',
                'email': 'berlin@dialogdata.de'
            }
        )
        Contact.objects.update_or_create(
            city='Timisoara',
            defaults={
                'name': 'DialogData GmbH & Co. KG',
                'coordinates': Geoposition(45.744471, 21.233235),
                'country': Country.objects.get(iso='ro'),
                'city': 'Timisoara',
                'address': 'Str. Putna nr. 6',
                'postal_code': '300593',
                'phone': '+40356100694',
                'email': 'timisoara@dialogdata.de'
            }
        )

    def generate_careers(self):
        Job.objects.update_or_create(
            title='eCommerce / SAP / hybris',
            defaults={
                'title': 'eCommerce / SAP / hybris',
                'subtitle': 'Senior Developer (m/w) bei Dialog Datawerden',
                'place': Place.objects.get(city='Munchen'),
                'description': '<b>We have an open position hybris developer, experienced with the following technologies:</b><br><br>Hybris >= 4.0<br>Database: SQL experience, with Oracle or other databasesPL/SQL is nice to have<br>Web: JavaScript, CSS, HTMLHTML5 is nice to havefluent in English or German<br>If you fit this profile, please apply at <a href=\"mailto:recruiting.tsr@dialogdata.de\">recruiting.tsr@dialogdata.de</a>'
            }
        )
        Job.objects.update_or_create(
            title='Mid-Level/Senior Java Developer',
            defaults={
                'title': 'Mid-Level/Senior Java Developer',
                'subtitle': 'We are looking for experenced collegues to join our E-Commerce development team.',
                'place': Place.objects.get(city='Timisoara'),
                'description': '<b>We have an open position for a talented developer, experienced with the following technologies:</b><br><br>Java Enterprise: 3+ years development experience with J2EE or newer, JSP/Servlets, EJB(2.1 or 3)<br>Experience with Weblogic is a plus<br>Database: SQL experience, with Oracle or other databasesPL/SQL is nice to have<br>Web: JavaScript, CSS, HTMLHTML5 is nice to havefluent in English or German<br>If you fit this profile, please apply at <a href=\"mailto:recruiting.tsr@dialogdata.de\">recruiting.tsr@dialogdata.de</a>'
            }
        )
        Job.objects.update_or_create(
            title='Java/JEE Developer',
            defaults={
                'title': 'Java/JEE Developer',
                'subtitle': 'We are looking for experenced collegues to join our E-Commerce development team.',
                'place': Place.objects.get(city='Timisoara'),
                'description': '<b>We have an open position for a talented developer, experienced with the following technologies:</b><br><br>Java Enterprise: 3+ years development experience with J2EE or newer, JSP/Servlets, EJB(2.1 or 3)<br>Experience with Weblogic is a plus<br>Database: SQL experience, with Oracle or other databasesPL/SQL is nice to have<br>Web: JavaScript, CSS, HTMLHTML5 is nice to havefluent in English or German<br>If you fit this profile, please apply at <a href=\"mailto:recruiting.tsr@dialogdata.de\">recruiting.tsr@dialogdata.de</a>'
            }
        )
        Job.objects.update_or_create(
            title='Senior Java/JEE Developer',
            defaults={
                'title': 'Senior Java/JEE Developer',
                'subtitle': 'We are looking for experenced collegues to join our E-Commerce development team.',
                'place': Place.objects.get(city='Berlin'),
                'description': '<b>We have an open position for a talented developer, experienced with the following technologies:</b><br><br>Java Enterprise: 3+ years development experience with J2EE or newer, JSP/Servlets, EJB(2.1 or 3)<br>Experience with Weblogic is a plus<br>Database: SQL experience, with Oracle or other databasesPL/SQL is nice to have<br>Web: JavaScript, CSS, HTMLHTML5 is nice to havefluent in English or German<br>If you fit this profile, please apply at <a href=\"mailto:recruiting.tsr@dialogdata.de\">recruiting.tsr@dialogdata.de</a>'
            }
        )

    def generate_clients(self):
        Client.objects.update_or_create(
            title='BMW',
            defaults={
                'title': 'BMW',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-bmw.jpg',
                'link': 'http://www.bmw.de',
                'case_study_link': '/blog/case-study/bmw'
            }
        )
        Client.objects.update_or_create(
            title='Carl Zeiss Meditec',
            defaults={
                'title': 'Carl Zeiss Meditec',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-carl-zeiss-meditec.jpg',
                'link': 'http://www.zeiss.com',
                'case_study_link': '/blog/case-study/carl-zeiss-meditec'
            }
        )
        Client.objects.update_or_create(
            title='Deutsche Bank',
            defaults={
                'title': 'Deutsche Bank',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-deutsche-bank.jpg',
                'link': 'http://www.db.com',
                'case_study_link': '/blog/case-study/deutsche-bank'
            }
        )
        Client.objects.update_or_create(
            title='ESG',
            defaults={
                'title': 'ESG',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-esg.jpg',
                'link': 'http://www.esg.de',
                'case_study_link': '/blog/case-study/esg'
            }
        )
        Client.objects.update_or_create(
            title='DATEV eG',
            defaults={
                'title': 'DATEV eG',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-datev.jpg',
                'link': 'http://www.datev.de',
                'case_study_link': '/blog/case-study/datev'
            }
        )
        Client.objects.update_or_create(
            title='Schneider Electric',
            defaults={
                'title': 'Schneider Electric',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-schneider-electric.jpg',
                'link': 'http://www.schneider-electric.com/',
                'case_study_link': '/blog/case-study/schneider-electric'
            }
        )
        Client.objects.update_or_create(
            title='Adidas',
            defaults={
                'title': 'Adidas',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-adidas.jpg',
                'link': 'http://www.adidas.com',
                'case_study_link': '/blog/case-study/adidas'
            }
        )
        Client.objects.update_or_create(
            title='Fiducia',
            defaults={
                'title': 'Fiducia',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-fiducia.jpg',
                'link': 'http://www.fiducia.de',
                'case_study_link': '/blog/case-study/fiducia'
            }
        )
        Client.objects.update_or_create(
            title='NTT DATA',
            defaults={
                'title': 'NTT DATA',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-nttdata.jpg',
                'link': 'http://www.nttdata.de',
                'case_study_link': '/blog/case-study/nttdata'
            }
        )
        Client.objects.update_or_create(
            title='Giesecke & Devrient',
            defaults={
                'title': 'Giesecke & Devrient',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-gieseche-devrient.jpg',
                'link': 'http://http://www.gi-de.com',
                'case_study_link': '/blog/case-study/gieseche-devrient'
            }
        )
        Client.objects.update_or_create(
            title='Rohde&Schwarz',
            defaults={
                'title': 'Rohde&Schwarz',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-rohde-schwarz.jpg',
                'link': 'http://www.rohde-schwarz.com',
                'case_study_link': '/blog/case-study/rohde-schwarz'
            }
        )
        Client.objects.update_or_create(
            title='C.H.Beck',
            defaults={
                'title': 'C.H.Beck',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-chbeck.jpg',
                'link': 'http://www.beck.de',
                'case_study_link': '/blog/case-study/chbeck'
            }
        )
        Client.objects.update_or_create(
            title='Arithnea',
            defaults={
                'title': 'Arithnea',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-arithnea.jpg',
                'link': 'http://www.arithnea.de',
                'case_study_link': '/blog/case-study/arithnea'
            }
        )
        Client.objects.update_or_create(
            title='Addison-Wesley',
            defaults={
                'title': 'Addison-Wesley',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-addision-wesley.jpg',
                'link': 'http://www.addison-wesley.de/',
                'case_study_link': '/blog/case-study/addision-wesley'
            }
        )
        Client.objects.update_or_create(
            title='Deutsche Börse Group',
            defaults={
                'title': 'Deutsche Börse Group',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-deutshe-borse-group.jpg',
                'link': 'http://deutsche-boerse.com',
                'case_study_link': '/blog/case-study/deutshe-borse-group'
            }
        )
        Client.objects.update_or_create(
            title='O2',
            defaults={
                'title': 'O2',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-o2.jpg',
                'link': 'http://www.o2.com',
                'case_study_link': '/blog/case-study/o2'
            }
        )
        Client.objects.update_or_create(
            title='Audi',
            defaults={
                'title': 'Audi',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-audi.jpg',
                'link': 'http://www.audi.de',
                'case_study_link': '/blog/case-study/audi'
            }
        )
        Client.objects.update_or_create(
            title='ING-DiBa',
            defaults={
                'title': 'ING-DiBa',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-ing-diba.jpg',
                'link': 'http://www.ing-diba.de',
                'case_study_link': '/blog/case-study/ing-diba'
            }
        )
        Client.objects.update_or_create(
            title='Hypovereinsbank',
            defaults={
                'title': 'Hypovereinsbank',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-hypovereinsbank.jpg',
                'link': 'http://www.hypovereinsbank.de',
                'case_study_link': '/blog/case-study/hypovereinsbank'
            }
        )
        Client.objects.update_or_create(
            title='ThyssenKrupp AG',
            defaults={
                'title': 'ThyssenKrupp AG',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-tyrssen-krupp.jpg',
                'link': 'http://www.thyssenkrupp.com/',
                'case_study_link': '/blog/case-study/tyrssen-krupp'
            }
        )
        Client.objects.update_or_create(
            title='Adesso AG',
            defaults={
                'title': 'Adesso AG',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-adesso.jpg',
                'link': 'http://www.adesso.de',
                'case_study_link': '/blog/case-study/adesso'
            }
        )
        Client.objects.update_or_create(
            title='Reply',
            defaults={
                'title': 'Reply',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'image': 'brand-reply.jpg',
                'link': 'http://www.reply.de',
                'case_study_link': '/blog/case-study/reply'
            }
        )

    def generate_business_domains(self):
        BusinessDomain.objects.update_or_create(
            title='Media',
            defaults={
                'title': 'Media',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'percentage': 15,
                'link': '/clients/media',
                'color': '#ef9520'
            }
        )
        BusinessDomain.objects.update_or_create(
            title='Automotive',
            defaults={
                'title': 'Automotive',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'percentage': 20,
                'link': '/clients/automotive',
                'color': '#2a4c8e'
            }
        )
        BusinessDomain.objects.update_or_create(
            title='Financial',
            defaults={
                'title': 'Financial',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'percentage': 20,
                'link': '/clients/financial',
                'color': '#919cb1'
            }
        )
        BusinessDomain.objects.update_or_create(
            title='Entertainment',
            defaults={
                'title': 'Entertainment',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'percentage': 10,
                'link': '/clients/entertainment',
                'color': '#61c29a'
            }
        )
        BusinessDomain.objects.update_or_create(
            title='Retail',
            defaults={
                'title': 'Retail',
                'description': 'All clients have their own demands bu we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'percentage': 35,
                'link': '/clients/retail',
                'color': 'green'
            }
        )

    def generate_events(self):
        images = [
            'http://www.amdbihor.ro/wp-content/uploads/2016/08/Team-outdoor-race-bihor-2016-7-650x400.jpg',
            'http://www.amdbihor.ro/wp-content/uploads/2016/08/Screenshot-2016-08-10-12.39.44.png',
            'https://scontent-frx5-1.xx.fbcdn.net/v/t31.0-8/20424215_1493915730669732_1300636427995537497_o.jpg?oh=f79de664c29fcf46d595f405ccb82d31&oe=5A5F50FB',
        ]
        event, created = Event.objects.update_or_create(
            title='TOR 2017',
            defaults={
                'title': 'TOR 2017',
                'description': '<b>Team Outdoor Race</b><br>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            }
        )
        if created:
            event.images = self.create_images(images)
            event.save()

        images = [
            'https://www.gutekueche.at/img/artikel/1093/fruehstueck.jpg',
            'https://image.stern.de/7287620/uncropped-0-0/b1d92cab843ab893e5b56dd2283b9bb2/ic/fruehstueck.jpg',
            'http://www.thehealthsite.com/wp-content/uploads/2014/06/fruits.jpg',
            'http://www.freepngimg.com/download/fruit/6-2-fruit-png-picture.png',
        ]
        event, created = Event.objects.update_or_create(
            title='Fruhstuck',
            defaults={
                'title': 'Fruhstuck',
                'description': 'Monday morning meeting',
            }
        )
        if created:
            event.images = self.create_images(images)
            event.save()

        images = [
            'https://www.gutekueche.at/img/artikel/1093/fruehstueck.jpg',
            'https://image.stern.de/7287620/uncropped-0-0/b1d92cab843ab893e5b56dd2283b9bb2/ic/fruehstueck.jpg',
            'http://www.thehealthsite.com/wp-content/uploads/2014/06/fruits.jpg',
            'http://www.freepngimg.com/download/fruit/6-2-fruit-png-picture.png',
        ]
        event, created = Event.objects.update_or_create(
            title='Pimpin\' our back yard',
            defaults={
                'title': 'Pimpin\' our back yard',
                'description': 'Put your muscle into it',
            }
        )
        if created:
            event.images = self.create_images(images)
            event.save()

    @staticmethod
    def generate_expertise():
        Expertise.objects.update_or_create(
            title='Java Enterprise',
            defaults={
                'main_item': True,
                'title': 'Java Enterprise',
                'description': 'It\'s a new day, it\'s a new life for meee! We are DialogData!<br>The company was founded 25 years ago. Imagine the experience we gathered all this time!',
                'link': '/jee',
                'style': 'color:white; background: url(\'/medias?name=java-enterprise\') no-repeat; background-size: cover;'
            }
        )
        Expertise.objects.update_or_create(
            title='eCommerce +  hybris',
            defaults={
                'main_item': True,
                'title': 'eCommerce +  hybris',
                'description': 'It\'s a new day, it\'s a new life for meee! We are DialogData!<br>The company was founded 25 years ago. Imagine the experience we gathered all this time!',
                'link': '/hybris',
                'style': 'color: white; background: #ff9000; background: -webkit-linear-gradient(left top, #ff9000, #ffb14c); background: -o-linear-gradient(bottom right, #ff9000, #ffb14c); background: -moz-linear-gradient(bottom right, #ff9000, #ffb14c); background: linear-gradient(to bottom right, #ff9000, #ffb14c);'
            }
        )
        Expertise.objects.update_or_create(
            title='Develop',
            defaults={
                'main_item': False,
                'title': 'Develop',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                'link': '/develop',
                'image': 'develop-icon.svg'
            }
        )
        Expertise.objects.update_or_create(
            title='Consult',
            defaults={
                'main_item': False,
                'title': 'Consult',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                'link': '/consult',
                'image': 'consult-icon.svg'
            }
        )
        Expertise.objects.update_or_create(
            title='Train',
            defaults={
                'main_item': False,
                'title': 'Train',
                'description': 'DialogData is hiring professionals from all across the IT industry. Feel free to get in touch and submit your resume at <a href=\"mailto:recruting@dialogdata.de\">recruting@dialogdata.de</a>',
                'link': '/train',
                'image': 'train-icon.svg'
            }
        )

    def generate_business_domains(self):
        BusinessDomain.objects.update_or_create(
            title='Media',
            defaults={
                'title': 'Media',
                'description': 'All clients have their own demands but we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'percentage': 15,
                'link': '/clients/media',
                'color': '#ef9520'
            }
        )
        BusinessDomain.objects.update_or_create(
            title='Automotive',
            defaults={
                'title': 'Automotive',
                'description': 'All clients have their own demands but we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'percentage': 20,
                'link': '/clients/automotive',
                'color': '#2a4c8e'
            }
        )
        BusinessDomain.objects.update_or_create(
            title='Financial',
            defaults={
                'title': 'Financial',
                'description': 'All clients have their own demands but we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'percentage': 20,
                'link': '/clients/financial',
                'color': '#919cb1'
            }
        )
        BusinessDomain.objects.update_or_create(
            title='Entertainment',
            defaults={
                'title': 'Entertainment',
                'description': 'All clients have their own demands but we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'percentage': 10,
                'link': '/clients/entertainment',
                'color': '#61c29a'
            }
        )
        BusinessDomain.objects.update_or_create(
            title='Retail',
            defaults={
                'title': 'Retail',
                'description': 'All clients have their own demands but we have managed to solve them all. All clients have their own demands bu we have managed to solve them all.',
                'percentage': 35,
                'link': '/clients/retail',
                'color': 'green'
            }
        )
