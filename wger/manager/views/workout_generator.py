

from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    get_object_or_404,
    render
)
from wger.manager.forms import WorkoutGeneratorForm

from wger.exercises.models import Exercise

from random import shuffle


def getGeneratorParams(postData):
    return postData['categories'], postData['levels']


def generate_plan(exercise_list, low_range, high_range):
    pairs = []
    exercise_number = 1
    for exercise in exercise_list:
        new_tuple = (exercise_number, exercise.name, str(low_range), str(high_range))
        pairs.append(new_tuple)
        exercise_number += 1
    return pairs

def convertLevel(lev):
    if (lev == "Intermediate"):
        return 2
    elif (lev == "Advanced"):
        return 3
    # Beginner
    return 1

def generate(cat, lev):
    levelVal = convertLevel(lev)

    # first get all workouts of the appropriate category
    exercises = list(Exercise.objects.filter(category__name=cat, language__short_name="en"))
    # debug
    # for exercise in exercises:
    #     if exercise.language.short_name == "en":
    #         print(exercise.name)

    # set the constant values
    num_exercises = levelVal * 3
    rep_range_low = levelVal * 5
    rep_range_high = levelVal * 10
    exercise_set = exercises[:num_exercises]
    shuffle(exercise_set)
    return generate_plan(exercise_set, rep_range_low, rep_range_high)

@login_required
def overview(request):
    """
    An overview of the workout-generator page
    """
    template_data = {}
    # check if POST or GET
    if request.method == 'POST':
        # get the original form with users selections
        form = WorkoutGeneratorForm(request.POST)

        # begin generating the results
        result_data = {}
        result_data['category'], result_data['level'] = getGeneratorParams(request.POST)
        template_data['form'] = form

        # generate workouts
        result_data['workout_plan'] = generate(result_data['category'], result_data['level'])

        # for elem in result_data['workout_plan']:
        #     print(elem)

        # for elem in Exercise.objects.all():
        #     print(elem.main_image)

        template_data['results'] = result_data
    else:
        # method == 'GET'
        form = WorkoutGeneratorForm()
        template_data['form'] = form

    return render(request, 'generator/generator.html', template_data)
