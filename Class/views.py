from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from accounts.models import Student, User
import json
# Create your views here.

class AddClassDetails(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        teacher = request.data['teacher']
        class_teacher = User.objects.get(username=teacher)
        if class_teacher.student==True:
            return Response({'success':False,'message':'Invalid Username'},status=status.HTTP_400_BAD_REQUEST)
        year = request.data['year']
        subjects = request.data['subjects']
        class_object = Class()
        class_object.class_teacher = class_teacher
        class_object.year = year
        class_object.subjectlist = subjects
        class_object.save()
        return Response({'success':True,'message':'Class details added successfully','class_id':class_object.class_id},status=status.HTTP_200_OK)

class AddStudentMarks(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            if request.user.student==True:
                return Response({'sucess':False,'message':"Only teachers can add the marks"},status=status.HTTP_401_UNAUTHORIZED)
            class_id = request.data['class_id']
            class_object = Class.objects.filter(class_id=class_id)
            student = request.data['student']
            try:
                student_object = Student.objects.get(user=User.objects.get(username=student))
            except:
                return Response({'sucess':False,'message':'Invalid username'},status=status.HTTP_400_BAD_REQUEST)
            roll_no = request.data['roll_no']
            marks = request.data['marks']
            d = class_object[0].students
            st_data = {
                "Student_id":"stu_"+str(student_object.student_id),
                "Marks":marks
            }
            d[roll_no]=st_data
            class_object.update(students = d)
            return Response({'success':True,'message':'Student added'},status=status.HTTP_200_OK)
        except Exception:
            return Response({'sucess':False,'message':'Invalid Class id'},status=status.HTTP_400_BAD_REQUEST)

class GetScore(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            if request.user.student==True:
                return Response({'sucess':False,'message':"Only teachers can view the marks"},status=status.HTTP_401_UNAUTHORIZED)
            class_id = request.data['class_id']
            subject = request.data['subject']
            marks = Class.objects.get(class_id=class_id).students
            l=[]
            try:
                for x in marks:
                    d={}
                    d['student']=marks[x]["Student_id"]
                    d['marks']=marks[x]["Marks"][subject]
                    l.append(d)
            except:
                pass
            return Response({'sucess':True,'subject':subject,'data':l},status=status.HTTP_200_OK)
        except:
            return Response({'sucess':False,'message':'Invalid Class id'},status=status.HTTP_400_BAD_REQUEST)