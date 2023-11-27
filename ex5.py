class rectangle:
    _nomber = 0

    def __init__(self, largeur=0, longueur=0):
        self.largeur = largeur
        self.longueur = longueur
        rectangle._nomber += 1

    # def __init__(self,v1)
    #   self.largeur=largeur
    #   self.longueur=longueur
    # rectangle._nomber += 1

    def getnomber(self):
        return self._nomber

    def getlargeur(self):
        return self.largeur

    def set_largeur(self, largeur):
        self.largeur = largeur

    def getlongueur(self):
        return self.longueur

    def set_longueur(self, longueur):
        self.longueur = longueur

    def equals(self, vect2D):
        if self.largeur == vect2D.largeur and self.longueur == vect2D.longueur:
            return True
        else:
            return False

    def primetre(self):
        return self.longueur * self.largeur

    def surface(self):
        return (self.largeur + self.longueur) * 2
    def tostring(self):
        return "  largeur " + str(self.largeur) +  " \nlongueur  " + str(self.longueur) + "\nequals:  " + str(self.equals(self)) + "\nprimetre:   " + str(self.primetre()) + "\nsurface:   " + str(self.surface())



class parallelepipede(rectangle):
    _nomber = 1

    def __init__(self, largeur=0, longueur=0, hauteur=0, nbrparallelepipedes=0):
        super().__init__(largeur, longueur)
        self.hauteur = hauteur
        self.nbrparallelepipedes = nbrparallelepipedes
        self._nomber += 1

    def gethauteur(self):
            return self.hauteur

    def set_hauteur(self, hauteur):
            self.hauteur = hauteur

    def getnbrparallelepipedes(self):
            return self.nbrparallelepipedest

    def surface(self):
            return super().surface() * self.hauteur

    def volume(self):
            return super().surface() * self.hauteur
    def volume (self):
        return self.largeur * self.longueur * self.hauteur


    def tostring(self):
            return super().tostring() + "\nhauteur  " + str(self.hauteur) + "\nnbrparallelepipedes   " + str(self.nbrparallelepipedes)+"\nvolume:  "+str(self.volume())





