import psutil
import sys
import warnings
from argparse import ArgumentParser

#Add an argument parser
parser = ArgumentParser()
parser.add_argument('-w',action="store_false",default=True,help='option to display runtime warnings')
args = vars(parser.parse_args())

#Parse out the value for warnings boolean.
warns = args.get('w')

#Conditional for warnings display.
if warns is True:
	#Disable warnings 
	if not sys.warnoptions:
		warnings.simplefilter("ignore")

print("This is a script to check cpu temperature...")

#Get sensor data from psutil.
tempsDict = psutil.sensors_temperatures()
#Parse out cpu temps.
general = tempsDict.get('acpitz')
#Parse out individual core temperatures.
individualCores = tempsDict.get('coretemp')

#print the current temps of each of the cpu cores.
print("Core 0 = {} degrees centigrade.".format(individualCores[0][1]))

print("Core 1 = {} degrees centigrade.".format(individualCores[1][1]))

print("Core 2 = {} degrees centigrade.".format(individualCores[2][1]))

print("Core 3 = {} degrees centigrade.".format(individualCores[3][1]))
##print(cputemp())


