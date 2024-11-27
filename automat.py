# Data om gyldige panttyper
pantdata = {
        'A': {
            'takst': 1.00,
            'info': 'Glasflasker på 0,5 liter'
        },
        'B': {
            'takst': 1.50,
            'info': 'Plastflasker under 1 liter'
        },
        'C': {
            'takst': 3.00,
            'info': 'Glasflasker over 0,5 liter eller plastflasker på 1 liter eller derover'
        }
    }

# Log af modtagne pantenheder i denne session
session = []

# Kode for nedlukning af maskinen. Konfigureres ved opstart.
nedlukningskode = None

# Modtager bogstavkoden for den pantede enhed og gemmer den i loggen for den aktive session
def modtag(panttype):
    if panttype.upper() in pantdata.keys():
        session.append(panttype.upper())

# Konfigurerer takst og beskrivelse for panttype G
def konfigurer_g():
    print('Konfiguration af automat')

    while 'G' not in pantdata.keys():
        g_config_takst = input('Indtast takst for panttype G: ')
        if g_config_takst.isnumeric():
            pantdata['G'] = {'takst': float(g_config_takst)}
    g_config_info = input('Indtast beskrivelse for panttype G: ')
    pantdata['G']['info'] = g_config_info

# Genstarter og nulstiller pantautomaten
def reboot():
    pantdata.pop('G')
    opstart()
# Styrer opstarts- og konfigureringssekvensen for pantautomaten
def opstart():
    global nedlukningskode
    if nedlukningskode == None:
        nedlukningskode = input('Pantautomat startet\nVælg nedlukningkode: ')
    konfigurer_g()

# Beregner den totale værdi af de pantede enheder i den aktive session
def beregn_session_total():
    total = 0
    for enhed in session:
        total += pantdata[enhed]['takst']
    return total

# Denne funktion nulstiller den nuværende session og returnerer beløbet til udbetaling
def udbetal():
    til_udbetaling = beregn_session_total()
    session.clear()
    return til_udbetaling
