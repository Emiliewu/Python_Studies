from django.shortcuts import render, redirect

def index(request):
  ##  the first method to get the number of visits
  # if 'num_visits' not in request.session:
  #   request.session['num_visits'] = 1
  # else:
  #   request.session['num_visits'] += 1
  ## the second method to get the number of visits
  num_visits = request.session.get('num_visits', 1)
  request.session['num_visits'] = num_visits + 1
  counter = request.session.get('counter', 1)
  request.session['counter'] = counter + 1
  context = {
    'num_visits': num_visits,
    'counter': counter
  }
  return render(request, "index.html", context)
def destroy_session(request):
  request.session['num_visits']= 0
  return redirect("/")
def increment_by_two(request):
  request.session['num_visits'] += 1
  return redirect("/")
def set_num(request):
  if request.method == "POST":
    user_num = int(request.POST['user_num'])
  if user_num > 0:
    request.session['num_visits'] += user_num-1
    return redirect("/")
  else:
    return redirect("/")