#Import packages
import pandas

#Extract pbp data in all games across all seasons within the study period
pbp_raw = 

#Rename the columns
pbp_raw_colnames = ['time', 'visitor_play','visitor_score','score','home_play','home_score']
pbp_raw.columns = pbp_raw_colnames

pbp_raw['all_play'] = pbp_raw['visitor_play'] + pbp_raw['home_play']


#Define functions that extract involved player(s) in each play

#make shots (e.g., shots = free throw, 2-pt dunk, 2-pt layup, 2-pt hook shot, 2-pt jump shot, 3-pt jump shot)
def make_shot(shot,play):
  search = "makes " + shot
  if search in play:
    play = play.strip()
    end = play.find(search)-1
    name = play[0:end]
    return name
  else: return

#miss shots (e.g., shots = free throw, 2-pt dunk, 2-pt layup, 2-pt hook shot, 2-pt jump shot, 3-pt jump shot)
def miss_shot(shot,play):
  search = "misses " + shot
  if search in play:
    play = play.strip()
    end = play.find(search)-1
    name = play[0:end]
    return name
  else: return 
  

#offensive/defensive rebound (e.g., offdef = Offensive, Defensive)
def ofrb(off_def, play):
  search = off_def + " rebound"
  if search in play:
    play = play.strip()
    start = len(search)+4
    name = play[start: ]
    return name 
  else: return

#assist (e.g., from_to = from, to)
def assist(from_to, play):
  if "assist" in play:
    if from_to == "from":
      play = play.strip()
      start = play.find("assist by") + len("assist by")
      end = len(play)-1
      name = play[start:end]
      return name
    elif from_to == "to":
      search = "makes "
      play = play.strip()
      end = play.find(search)-1
      name = play[0:end]
      return name
    else: return
  else: return
  
  
#Create a dataframe
pbp = pbp_raw


#Create a loop to fill in the dataframe
shots = ["free throw","2-pt dunk","2-pt layup","2-pt hook shot","2-pt jump shot","3-pt jump shot"]

for shot in shots:
  make_shot = "makes " + shot
  pbp[make_shot] = pbp['all_play'].apply(lambda x: make_shot(shot,x))
  miss_shot = "misses " + shot
  pbp[miss_shot] = pbp['all_play'].apply(lambda x: miss_shot(shot,x))
      
      
