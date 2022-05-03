import model

def izpis_igre(igra):
    return (
        "=========================================\n" +
        "Število preostalih poskusov: {}\n".format(model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()) +
        "Pravilni del gesla: {}\n".format(igra.pravilni_del_gesla()) +
        "Nauspeli poskusi: {}\n".format(igra.nepravilni_ugibi()) +
        "========================================="
    )
    
def izpis_zmage(igra):
    return "Čestitam uganil si geslo {}".format(igra.geslo)

def izpis_poraza(igra):
    return "Kaki retard. Geslo je {}".format(igra.geslo)

def zahtevaj_vnos():
    return input("Črka: ") #ko od igralca zahtevas vnos

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        stanje = igra.ugibaj(crka)
        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break

    
