from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from subreddit.models import Worker
from .forms import NewWorkerForm


@login_required
def ucp_index(request):
    context = {
        "username": request.user.username,
        "worker_list": Worker.objects.filter(profile=request.user)
    }
    return render(request, "ucp/index.html", context=context)


@login_required
def ucp_worker_register(request):
    if request.method == "POST":
        form = NewWorkerForm(request.POST)
        if form.is_valid():
            ip_addr = form.cleaned_data.get("ip_addr")
            new_worker = Worker(ip=ip_addr, working=False)
            new_worker.save()
            new_worker.profile.add(request.user)
            new_worker.save()
            new_uuid = new_worker.id
            return redirect(f"/ucp/worker/{new_uuid}")
    else:
        form = NewWorkerForm()
    return render(request, "ucp/registerworker.html", context={"form": form})

@login_required
def ucp_worker_view(request, id="xxx"):
    worker = get_object_or_404(Worker, id=id)
    if worker.profile is request.user:
        raise PermissionDenied
    context = {
        "worker_ip": worker.ip,
        "worker_id": worker.id,
        "worker_working": worker.working,
    }
    return render(request, "ucp/workerdetails.html", context=context)
