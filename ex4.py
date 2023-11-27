class documentaire:
    _nomber = 1

    def __init__(self, titre=0, date=0):
        self.titre = titre
        self.date = date
        self.id = documentaire._nomber
        documentaire._nomber += 1

    def tostring(self):
        return "titre:"+ str(self.titre) +"\ndate:" +str(self.date)+"\nid:" + str(self.id)

    def getnomber(self):
        return self._nomber

    def gettitre(self):
        return self.titre

    def set_titre(self, titre):
        self.titre = titre

    def getdate(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def equals(self, yahya):
        return self.id == yahya.id


class exemplaire(documentaire):
    _nomber = 1

    def __init__(self, titre=0, date=0, numero=0, date_dachat=0):
        super().__init__(titre, date)
        self.numero = numero
        self.date_dachat = date_dachat
        documentaire._nomber += 1

    def getnumero(self):
        return self.numero

    def set_numero(self, numero):
        self.numero = numero

    def getdate_dachat(self):
        return self.date_dachat

    def set_date_dachat(self, date_dachat):
        self.date_dachat = date_dachat

    def tostring(self):
        return super().tostring() + "\nnumero:"+str(self.numero) +"\ndate_dachat:"+ str(self.date_dachat)
