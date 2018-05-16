from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from grading.models import MainTask, BonusTask, Student


def index(request):
    return render(request, "grading/index.html")


def newgrade(request):
    if request.POST and request.POST['uniid']:
        return redirect(f"http://dijkstra.cs.ttu.ee/~{request.POST['uniid']}/ui/t2/")
    total = 10
    for task in BonusTask.objects.all():
        total += task.points
    context = {"bonus_tasks": BonusTask.objects.all, "total": total}
    return render(request, "grading/newgrade.html", context=context)


def newgrade(request):
    with open("grading/templates/grading/vue-grade.html") as f:
        return HttpResponse(f.read())


def grades(request):
    return render(request, "grading/grades.html", context={'students': Student.objects.all})


@csrf_exempt
def result(request):
    was_plag = "plag" in request.POST
    loc, uni1, uni2, points, plagcontent = request.POST['location'], request.POST['uniid1'], request.POST['uniid2'], request.POST['points'], request.POST['plagcontent']
    return render(request, "grading/result.html", context={'loc': loc, 'uni1': uni1, 'uni2': uni2, 'points': int(points), 'plag': was_plag, 'plagcontent': plagcontent})
