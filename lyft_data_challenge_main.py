import csv
import datetime
ride_ids = {} 
lifetime_duration = {}
recent_ride_id_date = {}
onboard_date = {} 
ride_timestamps = {} 
currentInfo = {}
data =[]
output =[]
def rideIdsCSV():
    with open('ride_ids.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if not(row[0]=='driver_id'):
                if not(row[2]==''):
                    distance = (int(row[2])/1609.344)
                    duration = (int(row[3])/60)
                    primeTime = int(row[4])
                    revenue = (2+(1.15*distance)+(0.22*duration)+1.75)
                    if primeTime !=0:
                        revenue = (1+(primeTime/100))*revenue
                    if revenue<5:
                        revenue = 5
                    elif revenue > 400:
                        revenue = 400
                    try:
                        currentInfo[row[0]]
                        ride_ids[row[0]]
                        ride_ids[row[0]].append(row[1])
                        
                        data[currentInfo[row[0]]][1]+=distance
                        data[currentInfo[row[0]]][2]+=duration
                        data[currentInfo[row[0]]][3]+=primeTime
                        data[currentInfo[row[0]]][4]+=1
                        data[currentInfo[row[0]]][5]+=revenue
                         
                    except:
                        currentInfo[row[0]]=len(data)
                        ride_ids[row[0]] = [row[1]]
                        data.append([row[0],distance,duration,primeTime,1,revenue])
        
def driverIdsCSV():             
    with open('driver_ids.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if not(row[0]=='driver_id'):
                onboard_date[row[0]]=row[1]
                year = int(row[1][0:4])
                month = int(row[1][5:7])
                day = int( row[1][8:10])
                onboard_date [row[0]]=[year,month,day]

   
def rideTimeStampsCSV():
    with open('ride_timestamps.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            ride_timestamps[row[0]]=row[2]
        for driver_id in ride_ids:
            
            for ride_id in ride_ids[driver_id]:
                try:
                    current = ride_timestamps[ride_id]
                    year = int(current[0:4])
                    month = int(current[5:7])
                    day = int( current[8:10])
                    ride_timestamps[ride_id]=[year,month,day]
                except:
                    pass
def findMostRecentRideId():
    for driver_id in ride_ids:
        try:
            current = ride_timestamps[ride_ids[driver_id][0]]
            for index in range(len(ride_ids[driver_id])):
                
                try:
                    Next = ride_timestamps[ride_ids[driver_id][index]]
                    if current[0]<Next[0]:
                        current = Next
                    elif current[0]==Next[0]:
                        if current[1]<Next[1]:
                            current = Next
                        elif current[1]==Next[1]:
                            if current[2]<Next[2]:
                                current = Next
                    
                except:
                    pass
        except:
            pass
        recent_ride_id_date[driver_id] = current

def findDuration():
    for driver_id in recent_ride_id_date:
        try:
            year = recent_ride_id_date[driver_id][0]-onboard_date[driver_id][0]
            month = recent_ride_id_date[driver_id][1]-onboard_date[driver_id][1]
            days = (recent_ride_id_date[driver_id][2]-onboard_date[driver_id][2])
            duration  = (year*360) + (month*30) + (days)
            if duration >0:
                lifetime_duration[driver_id] = duration
        except:
            pass
            
def finalOutput():
    for i in data:
        try:
            lifetime_duration[i[0]]
            output.append([i[0],i[1]/i[4],i[2]/i[4],i[3]/i[4],i[4],i[5],i[5]/lifetime_duration[i[0]],lifetime_duration[i[0]]])
        except:
            pass
        total_drivers =0
        total_distance = 0
        total_duration = 0
        total_primetime = 0
        total_num_customer = 0
        total_time_company=0
        total_revenue = 0
        total_revenue_per_day = 0
    for i in range(len(output)):
        total_distance += output[i][1]
        total_duration += output[i][2]
        total_primetime += output[i][3]
        total_num_customer += output[i][4]
        total_revenue += output[i][5]
        total_revenue_per_day +=output[i][6]
        total_time_company+=output[i][7]
        total_drivers+=1
    average_distance = total_distance/ total_drivers
    average_duration = total_duration/ total_drivers
    average_primetime = total_primetime/ total_drivers
    average_num_customer = total_num_customer/ total_drivers
    average_time_company= total_time_company/ total_drivers
    average_revenue = total_revenue/total_drivers
    average_revenue_per_day = total_revenue_per_day / total_drivers
    driver_lifetime_value = average_revenue_per_day * average_time_company
    
    with open('output.csv', mode='w') as csv_file:
        fieldnames = ['DRIVER_ID', 'AVERAGE_DISTANCE', 'AVERAGE_DURATION','AVERAGE_PRIMETIME','NUM_CUSTOMERS','TOTAL_REVENUE','REVENUE_PER_DAY','TIME_AT_COMPANY_IN_DAYS']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(output)):
            writer.writerow({'DRIVER_ID':output[i][0],'AVERAGE_DISTANCE':output[i][1],'AVERAGE_DURATION':output[i][2],
                             'AVERAGE_PRIMETIME':output[i][3],'NUM_CUSTOMERS':output[i][4],'TOTAL_REVENUE':output[i][5], 'REVENUE_PER_DAY':output[i][6],'TIME_AT_COMPANY_IN_DAYS':output[i][7]})
            

    with open('overall_info.csv',mode ='w') as csv_file:
        fieldnames = ['Average_Distance','Average_Duration_Working','Average_Primetime',
                      'Average_Num_Customers','Average_Time_At_Lyft','Average_Revenue','Average_Revenue_Per_Day','Driver_Average_LifeTime_Value']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Average_Distance':average_distance,'Average_Duration_Working':average_duration,
                         'Average_Primetime':average_primetime,'Average_Num_Customers':average_num_customer,
                         'Average_Time_At_Lyft':average_time_company,'Average_Revenue':average_revenue,'Average_Revenue_Per_Day':average_revenue_per_day,'Driver_Average_LifeTime_Value':driver_lifetime_value})

def main():
    rideIdsCSV()
    driverIdsCSV()
    rideTimeStampsCSV()
    findMostRecentRideId()
    findDuration()
    finalOutput()

