from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import util

def index(request):
    query = request.GET.get('q')
    if query:
        return redirect('entry', name=query)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    content = util.get_entry(name)
    return render(request, "encyclopedia/entry.html", {
        "content": content,
        "name": name.capitalize()
    }) 