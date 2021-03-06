from django.shortcuts import render

# Create your views here.
from courses.models import Course, Module

def index(request):
    """
    View that renders all available courses.

    Parameters
    ----------
    request:
        The client http request for the page.

    Returns
    -------
    render(): The courses index page with all the courses on it.
    """

    courses = Course.objects.all()[:20]

    context = {
        'title': "Home",
        'courses': courses,
    }

    return render(request, "courses_index.html", context)


def course_overview_by_id(request, id):
    """
    View that renders course that matches the provided id.

    Parameters
    ----------
    request:
        The client http request for the page.
    
    id(int):
        The id of the course looking to render.

    Returns
    -------
    render(): The course overview page for the given course id
    """
    course = Course.objects.get(id=id)
    modules = Module.objects.filter(course=id).order_by("number")
    context = {
        'course': course,
        'modules': modules
    }
    return render(request, "course_overview.html", context)

def course_overview_by_code(request, code, number):
    """
    View that renders course that matches the provided code.

    Parameters
    ----------
    request:
        The client http request for the page.
    
    code(str):
        The code of the course looking to render.

    Returns
    -------
    render(): The course overview page for the given course id
    """
    course = Course.objects.filter(number = number).get(code = code.upper())
    course_id = course.id 
    modules = Module.objects.filter(course=course_id).order_by("number")
    context = {
        'course': course,
        'modules': modules
    }
    return render(request, "course_overview.html", context)


def module_by_id(request, id):
    """
    View that renders module that matches the provided id.

    Parameters
    ----------
    request:
        The client http request for the page.
    
    id(int):
        The id of the module looking to render.

    Returns
    -------
    render(): The module details page for the given module id
    """
    module = Module.objects.get(id=id)
    context = {
        'module': module
    }
    return render(request, "module.html", context)


def module_by_name(request, code, number, module_number):
    """
    View that renders module that matches the provided id.

    Parameters
    ----------
    request:
        The client http request for the page.
    
    id(int):
        The id of the module looking to render.

    Returns
    -------
    render(): The module details page for the given module id
    """
    module = Module.objects.get(number=module_number)
    context = {
        'module': module
    }
    return render(request, "module.html", context)

