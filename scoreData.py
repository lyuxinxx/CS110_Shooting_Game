import json

class ScoreData():
    def __init__(self):
        self.file = open("scoreData.json","r")
        self.best = json.loads(self.file.read())
        self.file.close()
        
    def update(self):
        self.file = open("scoreData.json","w")
        self.file.write(str(self.best))
        self.file.close()
        
