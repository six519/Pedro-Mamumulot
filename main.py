import os, pygame
from pygame.locals import *
from settings import *
from sprites import *
from random import randrange

class MainGame(object):
	
	def __init__(self):
		self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
		self.clock = pygame.time.Clock()
		self.backGroundPath = "data/bg/"
		self.gameRunning = True
		self.bida = Bida(self.screen)
		self.drum1 = Drum(self.screen)
		self.drum2 = Drum(self.screen)
		self.drum3 = Drum(self.screen)
		self.drum4 = Drum(self.screen)
		self.lata1 = TinCan(self.screen)
		self.lata2 = TinCan(self.screen)
		self.lata3 = TinCan(self.screen)
		self.buto1 = Bone(self.screen)
		self.buto2 = Bone(self.screen)
		self.kalaban1 = Kalaban(self.screen)
		self.kalaban2 = Kalaban(self.screen)
		self.stage = 0
		self.score = 0
		self.lives = 5
		
	def generateRandomState(self):
		return randrange(4)
		
	def run(self):
		pygame.init()
		pygame.display.set_caption(GAME_TITLE)
		self.gameRunning = True
		
		
		while self.gameRunning:
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT or event.key == pygame.K_ESCAPE:
					return
				elif event.type == pygame.KEYUP:
					if self.stage > 0:
						self.bida.noMove()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						if self.stage == 0:
							self.stage = 1
														
			if self.stage > 0:
				key_pressed = pygame.key.get_pressed()
				pygame.display.set_caption("%s (Score: %s | Lives: %s)" % (GAME_TITLE, self.score, self.lives))
			
				if key_pressed[pygame.K_RIGHT]:
					if not self.bida.isCollidedTo(self.drum1) and not self.bida.isCollidedTo(self.drum2) and not self.bida.isCollidedTo(self.drum3) and not self.bida.isCollidedTo(self.drum4):
						self.bida.moveRight()
						
					self.bida.lastState = STATE_RIGHT
				elif key_pressed[pygame.K_LEFT]:
					if not self.bida.isCollidedTo(self.drum1) and not self.bida.isCollidedTo(self.drum2) and not self.bida.isCollidedTo(self.drum3) and not self.bida.isCollidedTo(self.drum4):
						self.bida.moveLeft()
						
					self.bida.lastState = STATE_LEFT
				elif key_pressed[pygame.K_UP]:
					if not self.bida.isCollidedTo(self.drum1) and not self.bida.isCollidedTo(self.drum2) and not self.bida.isCollidedTo(self.drum3) and not self.bida.isCollidedTo(self.drum4):
						self.bida.moveUp()
						
					self.bida.lastState = STATE_UP
				elif key_pressed[pygame.K_DOWN]:
					if not self.bida.isCollidedTo(self.drum1) and not self.bida.isCollidedTo(self.drum2) and not self.bida.isCollidedTo(self.drum3) and not self.bida.isCollidedTo(self.drum4):
						self.bida.moveDown()
					
					self.bida.lastState = STATE_DOWN

			#Room load here
			if self.stage == 0:
				self.loadRoomMain()
			if self.stage == 1:
				self.loadRoom1()			
			
			self.clock.tick(FPS)
			pygame.display.flip()	
	
	def loadBackground(self,image):
		try:
			bg = pygame.image.load("%s%s" % (self.backGroundPath,image))
			bg = bg.convert()
			self.screen.blit(bg, (0,0))
			return bg
		except Exception as e:
			print "Error %s" % e
			self.gameRunning = False
					
	def loadRoomMain(self):
		#load main background
		self.stage = 0
		self.loadBackground('main.bmp')
	
	def setSpriteState(self, spriteString):
		if self.generateRandomState() == STATE_RIGHT:
			exec("self.%s.lastState = STATE_RIGHT" % spriteString)
			exec('self.%s.moveString = "self.%s.moveRight()"' % (spriteString, spriteString))
		elif self.generateRandomState() == STATE_LEFT:
			exec("self.%s.lastState = STATE_LEFT" % spriteString)
			exec('self.%s.moveString = "self.%s.moveLeft()"' % (spriteString, spriteString))
		elif self.generateRandomState() == STATE_UP:
			exec("self.%s.lastState = STATE_UP" % spriteString)
			exec('self.%s.moveString = "self.%s.moveUp()"' % (spriteString, spriteString))
		elif self.generateRandomState() == STATE_DOWN:
			exec("self.%s.lastState = STATE_DOWN" % spriteString)
			exec('self.%s.moveString = "self.%s.moveDown()"' % (spriteString, spriteString))
		
	def loadRoom1(self):			
		self.stage = 1	
		self.loadBackground('room1.bmp')
		self.drum1.showAndSet((390,87))
		self.drum2.showAndSet((126,189))
		self.drum3.showAndSet((180,30))
		self.drum4.showAndSet((330,300))
		self.lata1.showAndSet((168,342))
		self.lata2.showAndSet((252,207))
		self.lata3.showAndSet((468,24))
		self.buto1.showAndSet((468, 354))
		self.buto2.showAndSet((39, 258))
		
		if not self.kalaban1.autoMoving:
			self.kalaban1.showAndSet((300, 180))
			self.setSpriteState("kalaban1")
			self.kalaban1.autoMoving = True
		
		exec(self.kalaban1.moveString)
		self.kalaban1.counter += 1
		
		if self.kalaban1.counter == RANDOM_COUNTER:
			self.kalaban1.counter = 0
			self.setSpriteState("kalaban1")
		
		if self.kalaban1.isCollidedTo(self.drum1) or self.kalaban1.isCollidedTo(self.drum2) or self.kalaban1.isCollidedTo(self.drum3) or self.kalaban1.isCollidedTo(self.drum4) or self.kalaban1.isCollidedTo(self.kalaban2):
			if self.kalaban1.lastState == STATE_RIGHT:
				self.kalaban1.x -= WALKING_SPEED 
			elif self.kalaban1.lastState == STATE_LEFT:
				self.kalaban1.x += WALKING_SPEED 
			elif self.kalaban1.lastState == STATE_UP:
				self.kalaban1.y += WALKING_SPEED 
			elif self.kalaban1.lastState == STATE_DOWN:
				self.kalaban1.y -= WALKING_SPEED
			self.setSpriteState("kalaban1")

		if not self.kalaban2.autoMoving:
			self.kalaban2.showAndSet((408, 207))
			self.setSpriteState("kalaban2")
			self.kalaban2.autoMoving = True
		
		exec(self.kalaban2.moveString)
		self.kalaban2.counter += 1
		
		if self.kalaban2.counter == RANDOM_COUNTER:
			self.kalaban2.counter = 0
			self.setSpriteState("kalaban2")
		
		if self.kalaban2.isCollidedTo(self.drum1) or self.kalaban2.isCollidedTo(self.drum2) or self.kalaban2.isCollidedTo(self.drum3) or self.kalaban2.isCollidedTo(self.drum4) or self.kalaban2.isCollidedTo(self.kalaban1):
			
			if self.kalaban2.lastState == STATE_RIGHT:
				self.kalaban2.x -= WALKING_SPEED 
			elif self.kalaban2.lastState == STATE_LEFT:
				self.kalaban2.x += WALKING_SPEED 
			elif self.kalaban2.lastState == STATE_UP:
				self.kalaban2.y += WALKING_SPEED 
			elif self.kalaban2.lastState == STATE_DOWN:
				self.kalaban2.y -= WALKING_SPEED
			
			self.setSpriteState("kalaban2")
		
		if self.bida.isCollidedTo(self.drum1) or self.bida.isCollidedTo(self.drum2) or self.bida.isCollidedTo(self.drum3) or self.bida.isCollidedTo(self.drum4):
			if self.bida.lastState == STATE_RIGHT:
				self.bida.x -= WALKING_SPEED 
			elif self.bida.lastState == STATE_LEFT:
				self.bida.x += WALKING_SPEED 
			elif self.bida.lastState == STATE_UP:
				self.bida.y += WALKING_SPEED 
			elif self.bida.lastState == STATE_DOWN:
				self.bida.y -= WALKING_SPEED
				
		self.bida.show((self.bida.x, self.bida.y))
				
		if self.bida.isCollidedTo(self.buto2):
			self.score += SCORE_PLUS
			self.buto2.hide()
		
		if self.bida.isCollidedTo(self.buto1):
			self.score += SCORE_PLUS
			self.buto1.hide()
			
		if self.bida.isCollidedTo(self.lata1):
			self.score += SCORE_PLUS
			self.lata1.hide()	

		if self.bida.isCollidedTo(self.lata2):
			self.score += SCORE_PLUS
			self.lata2.hide()
			
		if self.bida.isCollidedTo(self.lata3):
			self.score += SCORE_PLUS
			self.lata3.hide()
			
		if self.bida.isCollidedTo(self.kalaban1) or self.bida.isCollidedTo(self.kalaban2):
			self.bida.x = 0
			self.bida.y = 0
			self.lives -= 1 				
		
if __name__ == "__main__":
	game = MainGame()
	game.run()
