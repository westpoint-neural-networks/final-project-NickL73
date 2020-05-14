from tkinter import *
import predictor

#Estblish the window
window = Tk()
window.configure(bg="#a83240")

#Create the variables that will make our dataset
OK_SCORE = IntVar()
BY_SCORE = IntVar()
DOWN = IntVar()
DISTANCE = IntVar()
QUARTER = StringVar()
MINUTES = IntVar()
SECONDS = IntVar()
YTG = IntVar()
PREDICTED_PLAY = StringVar()
PLAY_PROBABILITY = StringVar()

#Set their default values to the beginning of a game
OK_SCORE.set("0")
BY_SCORE.set(0)
DOWN.set(1)
DISTANCE.set(10)
QUARTER.set(1)
MINUTES.set(15)
SECONDS.set(0)
YTG.set(80)
PREDICTED_PLAY.set("KICKOFF")
PLAY_PROBABILITY.set("100%")

#Add all entry labels and widgets
okScoreLabel = Label(window, text="Oklahoma Score")
byScoreLabel = Label(window, text="Baylor Score")
downLabel = Label(window, text="Down")
distanceLabel = Label(window, text="Distance")
quarterLabel = Label(window, text="Quarter")
minutesLabel = Label(window, text="Minutes Remaining")
secondsLabel = Label(window, text="Seconds Remaining")
ytgLabel = Label(window, text="Yards to Goal")

okScoreEntry = Entry(window, width=4, justify="center", textvariable=OK_SCORE)
byScoreEntry = Entry(window, width=4, justify="center", textvariable=BY_SCORE)
downEntry = OptionMenu(window, DOWN, 1, 2, 3, 4)
distanceEntry = Entry(window, width=4, justify="center", textvariable=DISTANCE)
quarterEntry = OptionMenu(window, QUARTER, 1, 2, 3, 4, "OT")
minutesEntry = Entry(window, width=4, justify="center", textvariable=MINUTES)
secondsEntry = Entry(window, width=4, justify="center", textvariable=SECONDS)
yardsEntry = Entry(window, width=4, justify="center", textvariable=YTG)

#arrange all of the widgets and make them pretty
labels = [okScoreLabel, byScoreLabel, downLabel, distanceLabel, quarterLabel, minutesLabel, secondsLabel, ytgLabel]
entries = [okScoreEntry, byScoreEntry, downEntry, distanceEntry, quarterEntry, minutesEntry, secondsEntry, yardsEntry]

for i in range(0, len(entries)):
	labels[i].grid(row=i,column=0, padx=5, pady=5)
	entries[i].grid(row=i, column=1, padx=5, pady=5)
	labels[i].configure(font="Courier", bg="#a83240", fg="white")
	entries[i].configure(font="Courier", highlightthickness=0)

#Show the predicted play in top right corner
playLabel = Label(window, textvariable=PREDICTED_PLAY, font=("Courier", 32))
playLabel.configure(bg="#a83240", fg="white")
playLabel.grid(row=2, column=2, padx=10)
probLabel = Label(window, textvariable=PLAY_PROBABILITY, font=("Courier", 24))
probLabel.configure(bg="#a83240", fg="white")
probLabel.grid(row=3, column=2, padx=10)

#Create the function that will set the resepctive variables from the entry 
def setVariables():
	oks = okScoreEntry.get()
	OK_SCORE.set(oks)
	bys = byScoreEntry.get()
	BY_SCORE.set(bys)
	distance = distanceEntry.get()
	DISTANCE.set(distance)
	minutes = minutesEntry.get()
	MINUTES.set(minutes)
	seconds = secondsEntry.get()
	SECONDS.set(seconds)
	yards = yardsEntry.get()
	YTG.set(yards)

#Create function that takes variables and makes them ints for use in prediction
def getVariables():
	setVariables()
	oks = int(OK_SCORE.get())
	bys = int(BY_SCORE.get())
	down = int(DOWN.get())
	distance = int(DISTANCE.get())
	quarter = 1 #placeholder
	if QUARTER.get() == "OT":
		quarter = 5
	else: quarter = int(QUARTER.get())
	minutes = int(MINUTES.get())
	seconds = int(SECONDS.get())
	yards = int(YTG.get())
	variables = [oks, bys, down, distance, quarter, minutes, seconds, yards]
	return variables

#Pass all of the variables into the ensemble model to get prediction
def getProbabilities():
	new_data = getVariables()
	oks, bys, down, distance, quarter, minutes, seconds, yards = new_data
	#[OFFENSE_SCORE, DEFENSE_SCORE, PERIOD, MINUTES, SECONDS, YARDS_TO_GOAL, DOWN, DISTANCE]
	runProb, passProb = predictor.getPrediction(oks, bys, quarter, minutes, seconds, yards, down, distance)
	if runProb >= passProb:
		PREDICTED_PLAY.set("RUN")
		PLAY_PROBABILITY.set(str(round(runProb*100, 2)) + "%")
	else:
		PREDICTED_PLAY.set("PASS")
		PLAY_PROBABILITY.set(str(round(passProb*100, 2))+"%")


#submitBtn = Button(window, text="Get Next Play", command= getPrediction)
submitBtn = Button(window, text="GET NEXT PLAY", height=2, width=25,command=getProbabilities)
submitBtn.grid(row=5, column=2, padx=5)
submitBtn.configure(font="Courier")


#Launch the GUI on an endless loop
window.title("Scott Prediction System")
window.mainloop()