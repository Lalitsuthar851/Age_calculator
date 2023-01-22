from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import date
# Create your views here.
def home(request):
    # from datetime import date
    # # d0 = date(2017, 8, 18)


    # d1 = today_ = date.today()
    # delta = d1 - d0
    # print(delta.days)
    if request.method=='POST':
        name=request.POST.get("name",default="")
        age_=request.POST.get("birthday",default="")
        gender_=request.POST.get("gender",default="")
        print(age_)
        try:
            year =int(age_[6:10])
            month = int(age_[3:5])
            date_ = int(age_[:2])
            dob = date(year, month, date_)


            print(dob)
            today_ = date.today()
            age = today_.year - dob.year - ((today_.month, today_.day) < (dob.month, dob.day))



            delta = today_ - dob
            days_till_now=delta.days


            weeks = (today_ - dob).days // 7

            num_months = (today_.year - dob.year) * 12 + (today_.month - dob.month)

            print(num_months)

            # return HttpResponse(f"{age,result,num_months,days_till_now}")
            return render(request,"result.html",{"name":name,"date":dob,"gender":gender_,"age":age,"days":days_till_now,"weeks":weeks,"months":num_months})
        except ValueError:
            return dirHttpResponse("<script>alert('please enter something')</script>")


    return render(request,"index.html")

