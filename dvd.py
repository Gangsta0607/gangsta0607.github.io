import pyxel
import random

class App:
	def __init__(self):
		self.x = 1 #random.random() * 10
		self.y = 1 #random.random() * 10
		self.color = 1
		self.direction = [1, 1]
		self.ewidth = 30
		self.eheight = 20
		self.height = 180
		self.width = 240
		self.win = False

		pyxel.FONT_WIDTH = self.ewidth / 2
		pyxel.FONT_HEIGHT = self.eheight / 2
		pyxel.init(self.width, self.height, title="DVD")
		pyxel.run(self.update, self.draw)

	def update(self):
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()
		if (self.x + self.ewidth >= self.width) or self.x == 0:
			self.direction[0] *= -1
			self.color = (self.color + 1) % 16
		if (self.y + self.eheight >= self.height) or self.y == 0:
			self.direction[1] *= -1
			self.color = (self.color + 1) % 16
		self.x += self.direction[0]
		self.y += self.direction[1]
		if self.color == 0: self.color += 1
		if self.x == 0 and self.y == 0: self.win = True


	def draw(self):
		if self.win:
			pyxel.text(self.height / 2, self.width / 2, "WIN", 2)
		pyxel.cls(0)
		pyxel.elli(self.x, self.y, self.ewidth, self.eheight, self.color)
		pyxel.text(self.x + self.ewidth / 3, self.y + self.eheight / 3, "DVD", 0)
		#pyxel.text(0, 0, f"{self.x} {self.y}", 1)

App()