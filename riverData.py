import csv

class data:
    monthName = ""
    Q = 0.0
    Qs = 0.0
    Qc = 0.0

    def __init__(self,monthName,Q,Qs,Qc):
        self.monthName = monthName
        self.Q = Q
        self.Qs = Qs
        self.Qc = Qc

def get_file_names():
    readFileName = raw_input("Give input file name ")
    writeFileName = raw_input("Give output file name ")
    fileName = [readFileName,writeFileName]
    return fileName

def extractNumbers(readFileName):
    dataList = []
    with open(readFileName) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if (str(row[1]) != "0") and (str(row[2]) != "0") and (str(row[3]) != "0"):
                riverData = data(str(row[0]),str(row[1]),str(row[2]),str(row[3]))
                dataList.append(riverData)
    return dataList

def print_River_Data(writeFileName,dataList):
    write = open(writeFileName,'w')
    for list in dataList:
        write.write(list.monthName)
        write.write('\t')
        write.write(list.Q)
        write.write('\t')
        write.write(list.Qs)
        write.write('\t')
        write.write(list.Qc)
        write.write('\n')

def average(dataList):
    avg = []
    i = 0
    Qavg = 0.0
    QsAvg = 0.0
    QcAvg = 0.0
    for list in dataList:
        Qavg = float(list.Q) + Qavg
        QsAvg = float(list.Qs) + QsAvg
        QcAvg = float(list.Qc) + QcAvg
        i += 1
    print("Q average:" ,Qavg/i)
    print("Qs average:" ,QsAvg/i)
    print("Qc average:" ,QcAvg/i)

def main():
    file_names = get_file_names()
    readFileName = file_names[0]
    writeFileName = file_names[1]

    dataList = extractNumbers(readFileName)

    print_River_Data(writeFileName,dataList)
    average(dataList)

if __name__ == "__main__":
    main()
