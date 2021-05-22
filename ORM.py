employees = Employee.objects.all().order_by('esal')
employees = Employee.objects.all().order_by('-esal')
employees = Employee.objects.all().order_by('-esal')[0]
employees = Employee.objects.all().order_by('-esal')[1]
employees = Employee.objects.all().order_by('-esal')[0:3]

#How to delete all Recordes

Employee.objects.all().delete()

e = Employee.objects.filter(eno = 123)
e.delete()

#How to detete multiple records

e = Employee.objects.filter(esal_gte = 15000)
e.delete()

#how to update a record

e = Employee.objects.filter(eno = 123)
e.ename = "rohit"
e.save()

#How to add a record

e = Employee(eno = 12,ename = "rohit",esal = 1234)
e.save()

#How to count 

Employee.objects.all().count()

#Aggregate Function..
#Avg(),Max(),Min(),Sum(),Count()
from django.db.models import AVg,Sum,Max(),Min(),Count()

avg1 = Employee.objects.all().aggregate(Avg('esal'))
max1 = Employee.objects.all().aggregate(Sum('esal'))


#How to select only sum Column in queryset.
q1 = Employee.objects.all().only('ename','esal','eno')

#OR operation..

employees = Employee.objects.filter(ename_startswith='A')|Employee.objects.
filter(esal_lte=15000)

#and operations..

employees = Employee.objects.filter(ename_startswith='A'),Employee.objects.
filter(esal_lte=15000)

#range..
employees = Employee.objects.filter(esal_range(12000,15000))

#in

Employee.objects.filter(id_in=[1,2,3])

#icontains..
Employee.objects.get(ename_icontians="rohit")










