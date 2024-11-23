from django.shortcuts import render, redirect, get_object_or_404
from .models import user_prof

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')

        if name and image:  # Ensure both name and image are provided
            user = user_prof.objects.create(name=name, image=image)
            user.save()

        return redirect('home')

    all_user = user_prof.objects.all()
    return render(request, 'user_details.html', {'all_user': all_user})

def delete_user(request, id):
    user = get_object_or_404(user_prof, id=id)
    user.delete()
    return redirect('home')

