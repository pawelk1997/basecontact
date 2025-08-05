from faker import Faker

fake = Faker("pl_PL")

def create_contacts(typ, ilosc):
    kontakty = []
    for i in range(ilosc):
        imie = fake.first_name()
        nazwisko = fake.last_name()
        telefon_prywatny = fake.phone_number()
        email = fake.email()

        if typ == "base":
            kontakt = BaseContact(imie, nazwisko, telefon_prywatny, email)
        elif typ == "business":
            firma = fake.company()
            stanowisko = fake.job()
            telefon_sluzbowy = fake.phone_number()
            kontakt = BusinessContact(imie, nazwisko, telefon_prywatny, email, firma, stanowisko, telefon_sluzbowy)
        else:
            raise ValueError("Jako typu kontaktu użyj 'base' lub 'business'!")
        
        kontakty.append(kontakt)
    return kontakty

class BaseContact:
    def __init__(self, imie, nazwisko, telefon_prywatny, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon_prywatny = telefon_prywatny
        self.email = email

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.email}"
    
    def __repr__(self):
        return f"BaseContact(imie={self.imie}, nazwisko={self.nazwisko}, email={self.email})"
    
    def contact(self):
        print(f"Wybieram numer {self.telefon_prywatny} i dzwonię do {self.imie} {self.nazwisko}")

    @property
    def label_length(self):
        return len(f"{self.imie} {self.nazwisko}")

class BusinessContact(BaseContact):
    def __init__(self, imie, nazwisko, telefon_prywatny, email, firma, stanowisko, telefon_sluzbowy):
        super().__init__(imie, nazwisko, telefon_prywatny, email)
        self.firma = firma
        self.stanowisko = stanowisko
        self.telefon_sluzbowy = telefon_sluzbowy

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.firma} {self.stanowisko} {self.telefon_sluzbowy}"
    
    def __repr__(self):
        return f"BusinessContact(imie={self.imie}, nazwisko={self.nazwisko} firma={self.firma}, stanowisko={self.stanowisko}, telefon_sluzbowy={self.telefon_sluzbowy})"
    
    def contact(self):
        print(f"Wybieram numer {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko}")

# Przykład działania "BaseContact"

baza = create_contacts("base", 2)
print("Kontakty prywatne:")
for i in baza:
    print(i)
    i.contact()
    print("Długość imienia i nazwiska: ", i.label_length)
    print("***")

# Przykład działania "BusinessContact"

baza = create_contacts("business", 2)
print("Kontakty biznesowe:")
for i in baza:
    print(i)
    i.contact()
    print("Długość imienia i nazwiska: ", i.label_length)
    print("***")