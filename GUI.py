import decimal
from tkinter import *
import CR

TargetINR = ["1.5-2.5","2.0-3.0","2.5-3.5"]
class Main:
    def __init__(self, parent):
        self.parent = parent

        Label(parent, text="Select Target INR").grid(row=2)
        self.INRList= Listbox(parent,selectmode=SINGLE,
                         height=3,
                         takefocus=0,
                         exportselection=0)
        self.INRList.grid(row=2,column=1)
        [self.INRList.insert(END, item) for item in TargetINR]
        self.INRList.select_set(1)

        Label(parent, text="Current INR?").grid(row=3)
        self.INREntry = Entry(parent)
        self.INREntry.grid(row=3,column=1)
 
        Label (parent, text="Coumadin increment?").grid(row=4)
        self.UnitDose= Entry(parent)
        self.UnitDose.grid(row=4,column=1)
        
        Label (parent, text = "Monday's dose?").grid(row=5)
        self.MondayEntry = Entry(parent)
        self.MondayEntry.grid(row=5,column=1)
        
        Label (parent, text = "Tuedays's dose?").grid(row=6)
        self.TuesdayEntry = Entry(parent)
        self.TuesdayEntry.grid(row=6,column=1)
        
        Label (parent, text = "Wednesday's dose?").grid(row=7)
        self.WednesdayEntry = Entry(parent)
        self.WednesdayEntry.grid(row=7,column=1)
        
        Label (parent, text = "Thursday's dose?").grid(row=8)
        self.ThursdayEntry = Entry(parent)
        self.ThursdayEntry.grid(row=8,column=1)
        
        Label (parent, text = "Friday's dose?").grid(row=9)
        self.FridayEntry = Entry(parent)
        self.FridayEntry.grid(row=9,column=1)

        Label (parent, text = "Saturday's dose?").grid(row=10)
        self.SaturdayEntry = Entry(parent)
        self.SaturdayEntry.grid(row=10,column=1)
        
        Label (parent, text = "Sunday's dose?").grid(row=11)
        self.SundayEntry = Entry(parent)
        self.SundayEntry.grid(row=11,column=1)
        
        Label (parent, text = "Manual Percent Change?").grid(row=12)
        self.ManualPercentChangeEntry = Entry(parent)
        self.ManualPercentChangeEntry.grid(row=12,column=1)
        
        SubmitButton = Button(parent, text="Submit?", background="green")
        SubmitButton.grid(row=13,columnspan=2)
        SubmitButton.bind("<Button-1>", self.SubmitClick)
        SubmitButton.bind("<Return>", self.SubmitClick)

        Label(parent, text = "Current Total Dose").grid(row=15)
        self.CurrentTotalDoseText = Text(parent, width=20,height=1)
        self.CurrentTotalDoseText.grid(row=15,column=1)


        Label(parent, text = "Percent Change").grid(row=16)
        self.PercentChangeText = Text(parent,width=20,height=1)
        self.PercentChangeText.grid(row=16,column=1)

        Label(parent, text = "New Current Dose").grid(row=17)
        self.NewTotalDoseText = Text(parent,width=20,height=1)
        self.NewTotalDoseText.grid(row=17,column=1)

        Label(parent, text = "New Coumadin Regimen").grid(row=18,columnspan=2)
        self.NewRegimenText = Text(parent, width="60", height="5")
        self.NewRegimenText.grid(row=19,columnspan=2)

        ExitButton = Button(parent, text="EXIT?", background="red")
        ExitButton.grid(row=100,columnspan=2)
        ExitButton.bind("<Button-1>", self.ExitClick)
        ExitButton.bind("<Return>", self.ExitClick)
       
    def SubmitClick (self,event):
        CurrentINR = decimal.Decimal(self.INREntry.get())
        UnitDose = decimal.Decimal(self.UnitDose.get())
        Monday = decimal.Decimal(self.MondayEntry.get())
        Tuesday = decimal.Decimal(self.TuesdayEntry.get())
        Wednesday = decimal.Decimal(self.WednesdayEntry.get())
        Thursday = decimal.Decimal(self.ThursdayEntry.get())
        Friday = decimal.Decimal(self.FridayEntry.get())
        Saturday = decimal.Decimal(self.SaturdayEntry.get())
        Sunday = decimal.Decimal(self.SundayEntry.get())
        ManualPercentChange = self.ManualPercentChangeEntry.get()
        TargetINRSelection = self.INRList.curselection() #Dont'covert this to a float as you can leave it empty


        OUTPUT = CR.CoumadinRegimen(CurrentINR,UnitDose,
                                    Monday,Tuesday,Wednesday,
                                    Thursday,Friday,Saturday,
                                    Sunday,ManualPercentChange,
                                    TargetINRSelection[0])


        self.CurrentTotalDoseText.delete(1.0,END)
        self.CurrentTotalDoseText.insert(END,str(OUTPUT[0])+"mgs")

        self.PercentChangeText.delete(1.0,END)
        self.PercentChangeText.insert(END,str(OUTPUT[2]*100)+"%")

        self.NewTotalDoseText.delete(1.0,END)
        self.NewTotalDoseText.insert(END,str(str(OUTPUT[1])+"mgs"))

        self.NewRegimenText.delete(1.0,END)
        self.NewRegimenText.insert(END,str(OUTPUT[3]))

    def ExitClick(self,event):
        self.parent.destroy()


root = Tk()
root.title("Coumadin Regimen Calculator")
main = Main(root)
root.mainloop()
