import psutil
import sys
import warnings



if not sys.warnoptions:
	warnings.simplefilter("ignore")

print("This is a script to check cpu temperature...")

#Print all cpu data.
#print(psutil.sensors_temperatures())
#print("****************************************")
tempsDict = psutil.sensors_temperatures()
general = tempsDict.get('acpitz')
individualCores = tempsDict.get('coretemp')
#print("++++++++++++++++++++++++++++++++++")
#print(general)
generalArr = general[0]
#print(generalArr)
currentTemp = generalArr[1]
#print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
#print(currentTemp)

#print("-----------------------------------------------")
#print(individualCores)

#print the current temps of each of the cpu cores.
#print(individualCores[0][1],individualCores[1][1],individualCores[2][1],individualCores[3][1])

print("Core 0 = {} degrees centigrade.".format(individualCores[0][1]))

print("Core 1 = {} degrees centigrade.".format(individualCores[1][1]))

print("Core 2 = {} degrees centigrade.".format(individualCores[2][1]))

print("Core 3 = {} degrees centigrade.".format(individualCores[3][1]))
##print(cputemp())


