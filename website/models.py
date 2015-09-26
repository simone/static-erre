# Create your models here.

from django.utils.translation import gettext_lazy as _

class MenuItem:
    def __init__(self, name, url, *submenu):
        self.name = name
        self.url = url
        self.submenu = submenu
        print(name, url, submenu)

m = MenuItem

SERVICES = (
    m(_('24 ore su 24'), 'service-24-hours.html'),
    m(_('Trasferimenti aeroportuali'), 'service-transfer.html'),
    m(_('Ovunque è necessario'), 'service-wherever-you-need.html'),
    m(_('Veicoli accessibili per i disabili'), 'service-wheelchair.html'),
    m(_('Black luxury car service'), 'service-black-luxury-car.html')
)

MENU = (
    m(_('Home'), 'index.html'),
    m(_('Chi Siamo'), 'who-we-are.html'),
    m(_('Servizi'), 'services.html', *SERVICES),
    #m(_('Autovetture'), 'our-fleet.html'),
    m(_('Contatti'), 'contacts.html', m(_('Invia una richiesta'), 'contacts.html#contact'), m(_('Seguici'), '#follow-us')),
)

PAGES = {}

class Page:
    def __init__(self, url, name, description, keywords):
        self.url = url
        self.name = name
        self.description = description
        self.keywords = keywords
        PAGES[url] = self

P404 = Page('404.html', _('Pagina non trovata'), '', '')

Page('index.html', _('Home'), _('NCC 4 Roma vi porta a visitare per Roma in auto, risolve tutti i problemi logistici, spostamenti dagli aereoporti, visite a Roma e nei dintorni'), _('noleggio con conducente roma autisti fidati'))
Page('who-we-are.html', _('Chi siamo'), _('La capacità di muoverci dentro Roma con la maneggevolezza di un Taxi ma con un parco auto di lusso, sintomo della cura che abbiamo per coloro che ci scelgono.'), _('keys'))
#Page('our-fleet.html', _('Autovetture'), _('Le nostre autovetture sono ben tenute, pulite, eleganti, spaziose, sileziose, confortevoli e piacevolmente rilassanti.'), _('automobili noleggio con conducente'))
Page('services.html', _('Servizi'), _('Tutti i nostri servizi pensati esclusivamente per voi, non ci sono paragoni.'), _('servizi auto noleggio con conducente'))
Page('specials.html', _('Offerte Speciali'), _('Le offerte speciali della nostra attività, in giro per roma e dintorni accompagnati da un autista fidato.'), _('offerte speciali noleggio con conducente roma'))
Page('contacts.html', _('Contatti'), _('In questa sezione puoi prendere contatto con noi, prenotare visite guidate, trasferimenti dagli aereoporti'), _('contatti telefono email ncc roma noleggio autista auto'))
Page('search.html', _('Ricerca'), _("Puoi trovare tutte le informazioni che ti occorrono spostarti a Roma tramite i nostri servizi usando il motore di ricerca di NCC 4 ROMA"), _('ricerca noleggio conducente roma'))
Page('results.html', _('Risultati'), _("Risutati della ricerca per noleggio con conducente a Roma"), _('risultati noleggio con conducente roma'))
Page('privacy.html', _('Informativa sulla privacy'), _("informativa sulla privacy conducente a Roma"), _('privacy'))

Page('service-transfer.html', _('trasferimenti aeroportuali'), _(""), _('trasferimenti collegamenti roma ciampino fiumicino roma aziende'))
Page('service-24-hours.html', _('24 ore su 24'), _(""), _(''))
Page('service-black-luxury-car.html', _('Autovetture nere e eleganti'), _(""), _(''))
Page('service-wheelchair.html', _('Autovetture attrezzate per i disabili'), _(""), _(''))
Page('service-wherever-you-need.html', _('Ovunque è necessario'), _(""), _(''))




