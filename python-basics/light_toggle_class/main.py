class Light:
    def __init__(self, isOn=False):
        self.isOn = isOn 
    def on(self):
        self.isOn = True
    def off(self):
        self.isOn = False
    def status(self):
        return self.isOn
    
light = Light()
light.on()
print("Light Turned On?: ",light.status())
light.off()
print("Light Turned On?: ",light.status())