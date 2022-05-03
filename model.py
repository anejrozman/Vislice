import random
STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"
ZMAGA = "W"
PORAZ = "X"

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        self.crke = [] if crke is None else crke
    
    def napacne_crke(self):
        napacne = []
        for crka in self.crke:
            if crka not in self.geslo:
                napacne.append(crka)
        return napacne

    def pravilne_crke(self):
        pravilne = []
        for crka in self.crke:
            if crka in self.geslo:
                pravilne.append(crka)
        return pravilne

    def stevilo_napak(self):
        st_napacnih_ugibov = 0
        for crka in self.crke:
            if crka not in self.geslo:
                st_napacnih_ugibov += 1
        return st_napacnih_ugibov

    def zmaga(self):          
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True

    def poraz(self):        
        return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        pravilni_del = ""
        for crka in self.geslo:
            if crka not in self.crke:
                pravilni_del += "_ "
            else:
                pravilni_del += crka + " "
        return pravilni_del.strip() #odreže preseldek na koncu
    
    def nepravilni_ugibi(self):
        nepravilni = ""
        for crka in self.crke:
            if crka not in self.geslo:
                nepravilni += crka + " "
        return nepravilni.strip()
    
 # za napravilni ugibi je tudi metoda .join() zapisali bi tko: " ".join(self.napacne_crke)

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else: 
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA

with open("besede.txt", encoding="utf-8") as f:
    bazen_besed = [vrstica.strip().upper() for vrstica in f]

def nova_igra():
    return Igra(random.choice(bazen_besed))







