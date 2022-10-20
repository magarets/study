import pandas as pd
import sys
open_path = './class.txt'
write_path = './result.txt'

def getData(f):
    data = []
    #filedata = f.readline()

    for raw in f:
        data.append(raw.strip().split(' '))
    return data

def getAverage(mid_score, final_score): # 점수의 평균을 구하는 함수
    return (int(mid_score) + int(final_score)) / 2

def writeData(name, average, grade): # .txt 파일로 저장하는 함수

    f = open(write_path, "w", encoding='UTF-8')

    f.write('\t\t' + '<Result>' + '\n\n')
    f.write('\t' + 'Average Score' + '\t\t' + 'Grade' + '\n')
    for value, data in enumerate(average):
        f.write(name[value] + '\t\t' + str(data) + '\t\t' + grade[value] + '\n')
    f.write('\n') # newline

    maxScore = max(average)
    minScore = min(average)

    whoisMax = name[average.index(maxScore)]
    whoisMin = name[average.index(minScore)]

    f.write('Highest Average Score / Name : ' + str(maxScore) + ' / ' + whoisMax + '\n')
    f.write('Lowest Average Score / Name : ' + str(minScore) + ' / ' + whoisMin + '\n')

def getGrade(average): # 점수에 따른 등급을 구하는 함수
    grade = []
    for data in average:
        if 90 <= data and data <= 100:
            grade.append('A')
        elif 80 <= data and data < 90:
            grade.append('B')
        elif 70 <= data and data < 80:
            grade.append('C')
        elif 60 <= data and data < 70:
            grade.append('D')
        else:
            grade.append('F')
    return grade
def main():

    f = open(open_path, "r")
    name = []
    average = []
    garde = []

    data = getData(f)

    for value, raw in enumerate(data):
        if value == 0:
            continue
        name.append(raw[0])
        average.append(getAverage(int(raw[1]), int(raw[2])))

    grade = getGrade(average)
    writeData(name, average, grade)

if __name__ == '__main__':
    main()