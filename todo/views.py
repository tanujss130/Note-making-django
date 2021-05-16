from django.shortcuts import render,redirect,HttpResponse
from .models import Todo
from .forms import Todoform
# Create your views here.

def insert(request):
    todo =  Todo.objects.all()
    if request.method == 'POST':
        new_todo = Todo(
        title = request.POST['title']
        #,
        # notes = request.POST['notes'] 
        )
        new_todo.save()
        return redirect('/')

    return render(request, 'index.html', {'todos': todo})


def show_data(request,id):
    todo = Todo.objects.filter(id=id)
    # print(todo.title)
    return render(request,'index1.html',{'todos':todo})

def edit(request,id):
    # return redirect('todo:insert')
    mydata=Todo.objects.get(id=id)
    if request.method == 'POST':
        form_data=Todoform(request.POST,instance=mydata)
        if form_data.is_valid():
            s=form_data.save(commit=False)
            s.save()
            return redirect('/')
    else :
        form_data=Todoform(instance=mydata)
        return render(request,'form.html',{'todos':form_data})

def delete(request,id):
	todo = Todo.objects.get(id=id)
	todo.delete()
	return redirect('/')

def back(request):
    return redirect('/')
