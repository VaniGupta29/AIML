#Hours Studied	
#Previous Scores	
#Extracurricular Activities	
#Sleep Hours	
#Sample Question Papers Practiced	
#Performance Index
print("Welcome to my project student performance")
HoursStudied = int(input("Enter the Hours Studied::"))
PreviousScores = int(input("Enter the Previous Score:: "))
ExtracurricularActivities= int(input("Enter the Extracurricular Activities::"))
SleepHours=int(input("Enter the Sleep Hours"))
SampleQuestionPapersPracticed= int(input("Enter the Sample Question Papers Practiced"))
print(HoursStudied,PreviousScores,ExtracurricularActivities,SleepHours,SampleQuestionPapersPracticed)
import pickle
with open("C:\\Users\\user\\Desktop\\Vani_Linear_Regression\\model\\StudentPerformanceModel.pkl",'rb')as file:
    model = pickle.load(file)
prediction = model.predict([[HoursStudied,PreviousScores,ExtracurricularActivities,SleepHours,SampleQuestionPapersPracticed]])[0]

print("Your Performance Score is :: ", prediction )



