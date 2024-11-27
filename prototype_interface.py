import automat

# Denne funktion samler al information til brugeren i en tekst
def generer_bruger_info():
    return generer_flaske_info()

# Denne funktion genererer information om sessionens afleverede flasker
def generer_flaske_info():
    return automat.session

# Denne funktion genererer teksten til udskrift på kvittering
def generer_kvittering_tekst():
    return automat.beregn_session_total()

if __name__ == '__main__':
    aktiv = True
    automat.opstart()
    while aktiv:
        print(generer_bruger_info())

        # Simuleret pantindkast/udbetal-tryk
        handling = input('Indkast pant eller udbetal. ')

        if handling == '':
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