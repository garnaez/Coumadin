import decimal

def d(X):
    return decimal.Decimal(str(X))

def INRadjust (CurrentINR,target_inr=1):
    """
    Takes current INR and returns suggested percentage change in coumadin dose.
    The target INR selections are:
    case 0: 1.5-2.5
    case 1:2.0-3.0
    case 2:2.5-3.5
    """
    
    cases = [(1.5,2.5), (2.0, 3.0), (2.5, 3.5)]
    percent_change=0

    try:
        low_range, high_range = cases[int(target_inr)]
    except IndexError:
        print ("Case assignment failed")
        return
    
    delta_low = d(low_range) - d(CurrentINR)
    delta_high = d(CurrentINR) - d(high_range)

#note some weight stuff going on with >=
# str >= int always equal true
# dec >= int always equal true

    if target_inr==1 and (d(3)>=d(CurrentINR)>=d(2)):
        percent_change=0
        return percent_change
    elif target_inr==0 and (d(2.5)>=d(CurrentINR)>=d(1.5)):
        percent_change=0
        return percent_change
    elif target_inr==2 and (d(3.5)>=d(CurrentINR)>=d(2.5)):
        percent_change=0
        return percent_change
    else: pass
    
    if delta_low >= d(0.5):
        percent_change= 0.15
    elif d(0.5) > delta_low >= d(0.25):
        percent_change = .10
    elif d(0.25) > delta_low >d(0.01):
        percent_change =0.05
    elif d(0.5) > delta_high >= d(0.01):
        percent_change = -0.05
    elif d(1) > delta_high >= d(0.5):
        percent_change = -0.10
    elif d(1.5) > delta_high >= d(1):
        percent_change= -0.125
    elif d(2) > delta_high >= d(1.5):
        percent_change = -0.15
    elif d(2.5) > delta_high >= d(2.0):
        percent_change = -0.175
    elif d(3) > delta_high >= d(2.5):
        percent_change = -0.20
    elif d(3.5) > delta_high >= d(3):
        percent_change = -0.25
    elif d(4) > delta_high >= d(3.5):
        percent_change = -0.30
    elif d(4.5) > delta_high >= d(4):
        percent_change = -0.35
    elif delta_high >= d(4.5):
        percent_change = -0.40
    else:
        print ("percent_change assigntment failed.")

    return decimal.Decimal(str(percent_change))
