

from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    get_object_or_404,
    render
)
from wger.manager.forms import (
    WorkoutGeneratorForm,
    WorkoutScheduleDownloadForm
)

from wger.exercises.models import (
    ExerciseCategory,

    Exercise
)

@login_required
def overview(request):
    """
    An overview of the workout-generator page
    """
    template_data = {}
    data = {}
    if request.method == 'POST':
        data['exercises']= list(Exercise.objects.filter(category__name=request.POST['categories']))
        form = WorkoutGeneratorForm(request.POST, initial=data)
        template_data['form'] = form
        template_data['popup'] = WorkoutScheduleDownloadForm()
    else:
        # method == 'GET'
        form = WorkoutGeneratorForm(initial=data)
        template_data['form'] = form

    return render(request, 'generator/generator.html', template_data)
