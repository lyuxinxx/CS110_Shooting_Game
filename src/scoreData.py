import json

class ScoreData():
    def __init__(self):
        try:
            self.file = open("src/scoreData.json",'r')
            self.best = int(self.file.read())
            self.file.close()
        except:
            self.best = 0
        
        
    def update(self):
        self.file = open("src/scoreData.json","w")
        self.file.write(str(self.best))
        self.file.close()
        
