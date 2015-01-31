from tkinter import *
import alsaaudio
import math

root = Tk()
root.title("Steven's Mix")
root.geometry('200x450+400+600')
root["bg"]='black'

rootFrame = Frame(root,
                  borderwidth=0,
                  padx = 5,
                  pady = 5,
                  background='black'
                  
                  )
rootFrame.pack()

def relinearize(foo):
    #take the linear scale input and curve it so it produces a "linear" volume increase
    return int(50*math.log(0.1*(10+foo),10))

def happy(hi):
    print(hi)

class niceFader(Scale):
    def __init__(self,name,initValue,mixer):
        self.value = DoubleVar()
        self.value.set(initValue) ###
        self.mixer = alsaaudio.Mixer(mixer)
        Scale.__init__(self,
                       rootFrame,
                       from_=1000,
                       to=0,
                       length=400,
                       sliderlength=20,
                       width=8,
                       troughcolor='black',
                       sliderrelief='flat',
                       relief="flat",
                       borderwidth=0,
                       showvalue = 0,
                       background="#eee", #actually slider color
                       variable = self.value,
                       command = (lambda x: self.changeVolume(x))
                       )

        self.name = name
        
        self.volume = relinearize(self.value.get()) ###
        self.mixer.setvolume(self.volume)

    def changeVolume(self,newVal):
        self.volume = relinearize(self.value.get()) ###
        self.mixer.setvolume(self.volume)
        print("newVal:",
              newVal, #since we already pull the new value from the control variable self.value, we can basically throw this away.
              "self.value:",
              self.value.get(),
              "self.volume:",
              self.volume)
              
        

'''
class quietButton(Button):
	def __init__(self):
		Button.__init__(self,
				rootFrame,
				text = "Going to sleep",
				command = self.clickAtQuieting,
				width = 15)
		self.rememberedValue = int()

	def clickAtQuieting(self):
	        #actions performed by the quiet button to make quiet
        	#preps the quiet button for resuming loudness
		self.rememberedValue = masterFader.value.get()
		masterFader.value.set(100)

        masterFader.volume = relinearize(self.value.get()) ###
        masterFader.mixer.setvolume(masterFader.volume)

        self.volume = relinearize(self.value.get()) ###
	        self.mixer.setvolume(self.volume)
        	self.sleepButton["text"] = "Reloudify"
        	self.sleepButton["command"] = self.clickAtLoud

def clickAtWake(self):
        #actions performed by the sleep button when waking up
        #preps the sleep button for sleeping
        stopSleep()
        self.sleepButton["text"] = "Going to sleep"
        self.sleepButton["command"] = self.clickAtSleep
        #do i need to repack the button?


quietButton = Button(
quietButton.pack({"side": "bottom"})
'''



'''
class faderBox(Frame):
    def __init__(self, fader):
        Frame.__init__(self,
                       rootFrame,
                       padx = 20,
                       background='blue'
                       )
        self.fader = fader
        self.fader.pack(side="left", padx=5)
        '''

masterFader = niceFader("Master Mix",800.0,'Master')
serverFader = niceFader("Server",600.0,'PCM')
lineInFader = niceFader("Line In",100.0,'Line')

#masterFader.value.set(30)

'''
faders = [faderBox(masterFader),
          faderBox(serverFader),
          faderBox(lineInFader)]

for fader in faders:
    fader.pack(side='left')
'''

masterFader.pack(side="left", padx=5, pady=5)
serverFader.pack(side="left", padx=5, pady=5)
lineInFader.pack(side="left", padx=5, pady=5)

#print(masterFader.value.get())
#masterFader.value.set(whatever)

root.mainloop()
root.destroy()
