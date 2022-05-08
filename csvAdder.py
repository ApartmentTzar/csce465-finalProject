import csv
import os.path

file = "sun/2022-04-{:2d}_{:02d}.{:02d}.{:02d}.{:1d}_Anytown_0_0_spectrum.csv"

partial = 3
sec = 29
minute = 39
hour = 17
day = 26
runningTotal = []
peakValues = []
while (partial!=(1+0)) or (sec!=16) or (minute!=42) or (hour!=17) or (day!=26):
    total = 0
    rowCount = 0
    if os.path.isfile(file.format(day, hour, minute, sec, partial)):
        with open(file.format(day, hour, minute, sec, partial), newline='') as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
            for row in reader:
                rowCount += 1
                total += row[1]
                if row[0] == 1.4285724E+03:
                    peakValues.append(row[1])
            runningTotal.append(total/rowCount)

    previousPartial = partial
    previousSec = sec
    previousMin = minute
    previousHour = hour

    partial += 1
    if partial >= 10:
        partial -= 10
    if (previousPartial > 8) and (partial < 3):
        sec += 1
    if sec >= 60:
        sec -= 60
    if (previousSec > 50) and (sec < 10):
        minute += 1
        if minute >= 60:
            minute -= 60
    if (previousMin > 50) and (minute < 10):
        hour += 1
        if hour >= 24:
            hour -= 24
    if (previousHour > 20) and (hour < 5):
        day += 1


output_file = "sunOutput.csv"
with open (output_file, mode='w+') as csvOutput:
    writer = csv.writer(csvOutput, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    i = 0
    for value in runningTotal:
        writer.writerow([i, value, peakValues[i]])
        i+=1
