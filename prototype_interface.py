import automat

# Denne funktion samler al information til brugeren i en tekst
def generer_bruger_info():
    return generer_flaske_info()

# Denne funktion genererer information om sessionens afleverede flasker
def generer_flaske_info():
    return automat.session

# Denne funktion genererer teksten til udskrift på kvittering
def generer_kvittering_tekst():
    out = ''
    for type in automat.pantdata.keys():
        if type in automat.session:
            out += str(automat.pantdata[type]['info'] + ' ')
            out += str(automat.session.count(type))
            out += str(automat.session.count(type)) + ' X ' + str(automat.pantdata[type]['takst']) + ' kr.\n'

    return out
    return automat.beregn_session_total()

if __name__ == '__main__':
    aktiv = True
    forrigeHandlingUdbetal = False
    automat.opstart()
    while aktiv:
        print(generer_bruger_info())
        if forrigeHandlingUdbetal == False:
            print('Antal pantgenstande afleveret: '+str(len(generer_bruger_info())))
        forrigeHandlingUdbetal = False
        print('Pant til udbetaling: '+str(automat.beregn_session_total()))
        # Simuleret pantindkast/udbetal-tryk
        handling = input('Indkast pant eller udbetal. ')

        if handling == 'udbetal':
            print(automat.beregn_session_total())
            print(generer_kvittering_tekst())
            automat.udbetal()

        elif (handling.upper() in automat.pantdata.keys()):
            automat.modtag(handling)

        elif handling == 'shutdown':
            if input('Nedlukningskode? ') == automat.nedlukningskode:
                aktiv = False

        elif handling == 'reboot':
            if input('Nedlukningskode? ') == automat.nedlukningskode:
                automat.reboot()

        else:
            print('Handling ikke mulig.')