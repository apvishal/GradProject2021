

from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    get_object_or_404,
    render
)
@login_required
def overview(request):
    """
    An overview of the workout-generator page
    """

    template_data = {}

    return render(request, 'generator/generator.html', template_data)
