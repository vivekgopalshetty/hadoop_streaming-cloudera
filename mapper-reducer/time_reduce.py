#!/usr/bin/python
# coding: utf-8

import sys
quad = []
tab = []
index=-1
count=0

theft="THEFT"
for i in range(8):
    quad.append([])
    tab.append([])
    
for input_line in sys.stdin:
    line = input_line.strip().split("\t") # Time \t Tuple
    time = str(line[0]) #time
    count=count+1 #print 'count"+str(count)

    hour = 0 + float(time)

    if hour>=0 and hour<3:
        quad[0].append(line[1])
    elif hour>=3 and hour<6:
        quad[1].append(line[1])
    elif hour>=6 and hour<9:
        quad[2].append(line[1])
    elif hour>=9 and hour<12:
        quad[3].append(line[1]
    elif hour>=12 and hour<15:
        quad[4].append(line[1])
    elif hour>=15 and hour<18:
        quad[5].append(line[1])
    elif hour>=18 and hour<21:
        quad[6].append(line[1])
    elif hour>=21 and hour<24:
        quad[7].append(line[1])

for i in range(0,8):
    theft_c = 0
    criminal_c=0
    burglary_c=0
    assault_c=0
    narcotics_c=0
                       
    if i==0:
        time_slot="00:00 – 02:59"
    if i==1:
        time_slot="03:00 – 05:59"
    if i==2:
        time_slot="06:00 – 08:59"
    if i==3:
        time_slot="09:00 – 11:59"
    if i==4:
        time_slot="12:00 – 14:59"
    if i==5:
        time_slot="15:00 – 17:59"
    if i==6:
        time_slot="18:00 – 20:59"
    if i==7:
        time_slot="21:00 – 23:59"

for j in range(len(quad[i])):
    crime_array = quad[i][j].strip().split(",") 
    crime_type = str(crime_array[5])
                       
    if crime_type == "THEFT":
        theft_c = theft_c + 1
    elif crime_type=="CRIMINAL DAMAGE":
        criminal_c = criminal_c + 1
    elif crime_type=="BURGLARY":
        burglary_c = burglary_c + 1
    elif crime_type=="ASSAULT":
        assault_c = assault_c + 1
    elif crime_type=="NARCOTICS":
        narcotics_c = narcotics_c + 1

    total_crimes = theft_c + criminal_c + burglary_c + assault_c + narcotics_c
    print '\n\nFor Time slot { ' + time_slot + ' } Occurrence of Crimetypes are: '
    print '-------------------------------------------------------------'
    print '\t\tTHEFT\t\t\t: '+str(theft_c)
    print '\t\tCRIMINAL DAMAGE\t\t: '+str(criminal_c)
    print '\t\tBURGLARY\t\t: '+str(burglary_c)
    print '\t\tASSAULT\t\t\t: '+str(assault_c)
    print '\t\tNARCOTICS\t\t: '+str(narcotics_c)
                       
    most = max(int(theft_c),int(criminal_c), int(burglary_c),int(assault_c), int(narcotics_c))
    if most==theft_c:
        most_crime="THEFT"
    elif most==criminal_c:
        most_crime="CRIMINAL DAMAGE" 
    elif most==burglary_c:
        most_crime="BURGLARY"
    elif most==assault_c:
        most_crime="ASSAULT"
    elif most==narcotics_c:
        most_crime="NARCOTICS"
    print '\n\t\t=> Total Crimes ccurred and reported in above time slot is : ' + str(total_crimes) + ' reports.'
    print '\n\t\t=> Also the most ccurred crime in above time slot is :' + most_crime + str(most) + ' times.'
    tab[i].append(theft_c)
    tab[i].append(criminal_c)
    tab[i].append(burglary_c)
    tab[i].append(assault_c)
    tab[i].append(narcotics_c)
    print('\n\n**************************************************************************************************')

print('\n\t\t\tTHEFT\t\tCRIMINAL\tBURGLARY\tASSAULT\t\tNARCOTICS')
for i in range(0,8):
 print ("\nSlot"+str(i+1)+"\t\t\t"+str(tab[i][0])+"\t\t"+str(tab[i][1])+"\t\t"+str(tab[i][2])+"\t\t"+str(tab[i][3])+"\t\t"+str(tab[i][4]))
                       
print ('\n\t* Total number of Tuples analysed are : ' + str(count)) 
print('\n**************************************************************************************************\n\n' )
