# Python Script Install System
from urllib.request import*
from tkinter import*
site=''
class error(exception):
	pass
def install(self, name):
	try:
		file=open(name,'wb')
		file.write(urlopen(site))
		file.close()
		self.wiz.destroy()
		print('PySIS installed the software')
	except:
		raise error('failed to install file from'+site+'!'\
)
class wizard:
	def __init__(self, website, name='new'):
		global site
		self.wiz=Tk()
		self.wiz.title('download wizard - powered by PySIS')
		site=website
		self.butt=Button(root, title='install software', command=install, args=self, name)
