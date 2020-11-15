from django.shortcuts import render,redirect
from .models import TodoList, Category
from django.urls import reverse


#To save and delete todos in our database
def index(request): #the index view
    todos = TodoList.objects.all() #quering all todos with the object manager
    categories = Category.objects.all() #getting all categories with object manager

    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save() #saving the todo 
            return redirect(reverse('todolist')) #reloading the page
        
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            print(checkedlist)
            for todo_id in checkedlist:
                print(todo_id)
                todo = TodoList.objects.filter(id=int(todo_id)) #getting todo id
                print(todo)
                todo.delete() #deleting todo
    return render(request, "index.html", {"todos": todos, "categories":categories})