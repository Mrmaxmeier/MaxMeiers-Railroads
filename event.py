from curses import *
from grid import *
import sys,time
class Event:
	def __init__(self,uiobject,gameobject):
		self.uiobj = uiobject
		self.gameobj = gameobject
	def parseevent(self,event):
		if self.uiobj.inmenu == 0:#Ingame
			if event == KEY_LEFT:
				self.gameobj.move_highlight("LEFT")
			elif event == KEY_RIGHT:
				self.gameobj.move_highlight("RIGHT")
			elif event == KEY_UP:
				self.gameobj.move_highlight("UP")
			elif event == KEY_DOWN:
				self.gameobj.move_highlight("DOWN")
			#elif event == ord("R") or event == ord("r"):
			#	self.uiobj.refresh("all") --UnWanted
			elif event == ord("M") or event == ord("m"):
				self.uiobj.inmenu = 1
				self.gameobj.pause()
				self.uiobj.refresh("all")
			elif event == ord("B") or event == ord("b"):
				self.uiobj.inmenu = 2
				self.uiobj.refresh("all")
			#elif event == ord("N") or event == ord("n"):
			#	for route in self.gameobj.routelist:
			#		route.next()
			#	self.uiobj.refresh("all")
			elif event == ord("T") or event == ord("t"):
				self.uiobj.inmenu = 3
				self.gameobj.pause()
				self.uiobj.refresh("all")
		elif self.uiobj.inmenu == 1:#Menu
			if event == ord("E") or event == ord("e") or event == ord("M") or event == ord("m"):# or event == ord("Q") or event == ord("q"):
				self.uiobj.inmenu = 0
				self.gameobj.resume()
				self.uiobj.refresh("all")
			elif event == ord("S") or event == ord("s"):
				self.gameobj.storage.save()
				self.gameobj.newsstrings.append(["Game Saved!",5])
				self.uiobj.inmenu = 0
				self.gameobj.resume()
				self.uiobj.refresh()
			elif event == ord("L") or event == ord("l"):
				self.gameobj.storage.load()
				self.gameobj.newsstrings.append(["Game Loaded!",5])
				self.uiobj.inmenu = 0
				self.gameobj.resume()
				self.uiobj.refresh()
		elif self.uiobj.inmenu == 2:#BuildMode
			if event == ord("E") or event == ord("e") or event == ord("Q") or event == ord("q"):
				self.uiobj.inmenu = 0
				self.uiobj.refresh("all")
			if event in [ord("W"),ord("w"),ord("D"),ord("d"),ord("A"),ord("a"),ord("S"),ord("s")]:
				if event   == ord("W") or event == ord("w"): cdir = UP
				elif event == ord("D") or event == ord("d"): cdir = RIGHT
				elif event == ord("A") or event == ord("a"): cdir = LEFT
				elif event == ord("S") or event == ord("s"): cdir = DOWN
				cfield = self.gameobj.storage.grid.dict[self.gameobj.highlighted[0],self.gameobj.highlighted[1]]
				if cfield.isRail(cdir):
					self.gameobj.gain_money(19)
					cfield.destroyRail(cdir)
				elif cfield.isRail(cdir) == False:
					if self.gameobj.spend_money(20):
						cfield.buildRail(cdir)
			elif event == ord("\n"):
				cfield = self.gameobj.storage.grid.dict[self.gameobj.highlighted[0],self.gameobj.highlighted[1]]
				cfield.toggleStation()
				self.uiobj.refresh("all")
			if event == KEY_LEFT:
				self.gameobj.move_highlight("LEFT")
			elif event == KEY_RIGHT:
				self.gameobj.move_highlight("RIGHT")
			elif event == KEY_UP:
				self.gameobj.move_highlight("UP")
			elif event == KEY_DOWN:
				self.gameobj.move_highlight("DOWN")
		elif self.uiobj.inmenu == 3:#TrainManager
			if event == ord("Q") or event == ord("q"):
				self.uiobj.inmenu = 0
				self.gameobj.resume()
				self.uiobj.refresh("all")
			elif event == ord("E") or event == ord("e"):
				self.uiobj.inmenu = 4
				self.uiobj.refresh()
			elif event == ord("N") or event == ord("n"):
				self.game.ctrain += 1
				self.game.ctrain = self.game.ctrain%len(self.game.trainlist)
			elif event == ord("P") or event == ord("p"):
				self.game.ctrain += -1
				self.game.ctrain = self.game.ctrain%len(self.game.trainlist)
		elif self.uiobj.inmenu == 4:#TrainCreator
			if event == ord("Q") or event == ord("q"):
				self.uiobj.inmenu = 0
				self.gameobj.resume()
				self.uiobj.refresh("all")
			