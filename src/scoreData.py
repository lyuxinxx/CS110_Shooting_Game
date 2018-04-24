import json

class ScoreData():
    '''
        This class is used to store and get score data.
    '''
    def __init__(self):
        '''
            read in data, if file not found, best equals 0
        '''
        try:
            self.file = open("src/scoreData.json",'r')
            self.best = int(self.file.read())
            self.file.close()
        except:
            self.best = 0
        
        
    def update(self):
        '''
            update best score
        '''
        self.file = open("src/scoreData.json","w")
        self.file.write(str(self.best))
        self.file.close()
        
