from django.shortcuts import render

finches = [
  {'name': 'Misa' , 'species': 'Purple Finch', 'description': 'aggressive', 'age': 2},
  {'name': 'Harry' , 'species': 'Evening Grosbeak', 'description': 'gentle', 'age': 3},
]

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
      'finches': finches
   })