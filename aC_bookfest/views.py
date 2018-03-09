from django.http import HttpResponseRedirect
from django.shortcuts import render


# def model_form_upload(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = DocumentForm()
#     return render(request, 'form/simple_upload.html', {
#         'form': form
#     })

def post_list(request):
    return render(request, 'alpha/index.html', {})