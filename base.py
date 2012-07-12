import os, pygame
from pygame.locals import *
from settings import *

class BaseSprite(pygame.sprite.Sprite):
    
    spriteCount = 0
    
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.x = 0
        self.y = 0
        self.image = None
        self.rect = None
        self.lastState = None
        self.hidden = False
        self.autoMoving = False
        self.moveString = ""
        self.counter = 0
        BaseSprite.spriteCount += 1
    
    def loadImage(self, imageFullPath):
        try:
            image = pygame.image.load(imageFullPath)
            image = image.convert()
            colorKey = image.get_at((0,0))
            image.set_colorkey(colorKey, pygame.RLEACCEL)
            return image, image.get_rect()
        except Exception as e:
            print "Can't load image %s" % e
            
    def show(self, coordinate = (0,0)):
        if not self.hidden:
            self.screen.blit(self.image, coordinate)
        
    def showAndSet(self, coordinate = (0,0)):
        if not self.hidden:
            self.x, self.y = coordinate
            self.screen.blit(self.image, coordinate)
        
    def setImage(self, img):
        self.image, self.rect = self.loadImage("%s%s" % (self.imagePath, img))
        
    def isCollidedTo(self, obj):
        if not self.hidden:
            lowerX1 = obj.x + obj.rect.width - 1
            lowerY1 = obj.y + obj.rect.height - 1
            lowerX2 = self.x + self.rect.width - 1
            lowerY2 = self.y + self.rect.height - 1
            
            if (lowerX1 < self.x) or (obj.x > lowerX2) or (lowerY1 < self.y) or (obj.y > lowerY2):
                return False    
                
            return True
        else:
            return False
    
    def noMove(self):
        self.setImage("nokey.bmp")
        
    def moveRight(self):
    
        if not self.x >= GAME_WIDTH - self.rect.width:    
            self.x += WALKING_SPEED
            
        self.show((self.x,self.y))

        if (self.x % 2) == 0:
            self.setImage("right/right1.bmp")    
        else:
            self.setImage("right/right2.bmp")    
    
    def moveLeft(self):
    
        if not self.x <= 0:
            self.x -= WALKING_SPEED
            
        self.show((self.x,self.y))

        if (self.x % 2) == 0:
            self.setImage("left/left1.bmp")    
        else:
            self.setImage("left/left2.bmp")            
        
    def moveDown(self):
    
        if not self.y >= GAME_HEIGHT - self.rect.height:
            self.y += WALKING_SPEED
        
        self.show((self.x,self.y))

        if (self.y % 2) == 0:
            self.setImage("down/down1.bmp")    
        else:
            self.setImage("down/down2.bmp")            

    def moveUp(self):
    
        if not self.y <= 0:
            self.y -= WALKING_SPEED
            
        self.show((self.x,self.y))

        if (self.y % 2) == 0:
            self.setImage("up/up1.bmp")    
        else:
            self.setImage("up/up2.bmp")
    
    def hide(self):
        self.showAndSet((0 - self.rect.width, 0 - self.rect.height))
        self.hidden = True