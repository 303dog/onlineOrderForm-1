from django.shortcuts import render, render_to_response


def not_found_view(request):
    response = render_to_response('my404.html')
    response.status_code = 404

    return response

