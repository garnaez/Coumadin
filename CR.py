import inr
import math
import decimal
def CoumadinRegimen (CurrentINR,
                     UnitDose,
                     Monday,
                     Tuesday,
                     Wednesday,
                     Thursday,
                     Friday,
                     Saturday,
                     Sunday,
                     ManualPercentChange = None,
                     TargetINR = None
                    ):
              
    """Accept Coumadin dosing regimen and return new dosing regimen.

    This function is an attemp to merge the coumadinRegimen functions.
    It accepts
    1. CurrentINR: the patient's current INR
    2. UnitDose: ths is the smallest increment that you can change a patient's
        dose. Ie if you are using 2mg tablets then the smaller change would
        be splitting the tablet which would be 1mg which is what you enter.
    3. Monday-Sunday: Just enter the actual coumadin dose
    4. ManualPercentChange: Allows the doctor to change the percent adjustment
    5. TargetINR: not implemented yet, but will adjust suggest precent
        adjustments depending on what your goal is, 2, 2.5, 3, which would
        represent 1.5-2.5,2-3, and 2.5-3.5
    """


    CurrentWeekDose = {"Monday":Monday,
                           "Tuesday":Tuesday,
                           "Wednesday":Wednesday,
                           "Thursday":Thursday,
                           "Friday":Friday,
                           "Saturday":Saturday,
                           "Sunday":Sunday}
  
    CoumadinValuesList  = CurrentWeekDose.values()
    CurrentTotal = sum(CoumadinValuesList)
    CurrentDoseUnit = CurrentTotal/UnitDose #This is needed since we are trying to be decide how to spread the increments (pill), not actual mg

    if ManualPercentChange == None:
        PercentChange = inr.INRadjust(CurrentINR,TargetINR)
    elif ManualPercentChange == '':
        PercentChange = inr.INRadjust(CurrentINR,TargetINR)
    else:
        PercentChange = decimal.Decimal(ManualPercentChange)/decimal.Decimal(100)
        
    UnitIncrease = decimal.Decimal(str(CurrentDoseUnit))*(PercentChange)
    NewUnitTotal = CurrentDoseUnit + UnitIncrease
    NewDoseUnitRounded = math.ceil(NewUnitTotal)
    NewTotal = decimal.Decimal(str(NewDoseUnitRounded))*UnitDose
    Regimen = divmod(NewDoseUnitRounded,7) #This is the key math to figure out who to distribute the new doses

    WeekReference = { 0:"No left over doses",
                      1:"Monday",
                      2:"Monday Thursday",
                      3:"Monday Wednesday Friday",
                      4:"Monday Wednesday Friday Saturday",
                      5:"Monday Wednesday Friday Saturday Sunday",
                      6:"Monday Tuesday Wednesday Friday Saturday Sunday"
                      }

    WeekOrderedlist = 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday'


    if Regimen[1] == 0:
        SingleTextLineOfRegimen = str((UnitDose * decimal.Decimal(str(Regimen[0])))) + "mg of coumadin every day."
    else:
        SingleTextLineOfRegimen = str((UnitDose * decimal.Decimal(str(Regimen[0]))))\
                                  +"mg of coumadin every day except "\
                                  + str ((UnitDose*decimal.Decimal(str(Regimen[0]))+UnitDose))\
                                  + "mg on "\
                                  + WeekReference[Regimen[1]]
    return CurrentTotal, NewTotal, PercentChange, SingleTextLineOfRegimen
