from base import *

class Drum(BaseSprite):

    def __init__(self, screen):
        BaseSprite.__init__(self, screen)
        self.imagePath = "data/obj/"
        self.setImage('drum.bmp')
        
class Bone(BaseSprite):

    def __init__(self, screen):
        BaseSprite.__init__(self, screen)
        self.imagePath = "data/obj/"
        self.setImage('buto.bmp')
        
class TinCan(BaseSprite):

    def __init__(self, screen):
        BaseSprite.__init__(self, screen)
        self.imagePath = "data/obj/"
        self.setImage('lata.bmp')

class Bida(BaseSprite):
    
    def __init__(self, screen):
        BaseSprite.__init__(self, screen)
        self.imagePath = "data/bida/"
        self.noMove()
        
class Kalaban(BaseSprite):
    
    def __init__(self, screen):
        BaseSprite.__init__(self, screen)
        self.imagePath = "data/kalaban/"
        self.noMove()