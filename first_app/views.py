from django.http import HttpRequest, HttpResponse


def greeting(request: HttpRequest) -> HttpResponse:
    template: str = f"""
    <h1>Hello from the Django</h1>
    <h2>It's our first view</h2>
    <h4>My name is ivencic</h4>
    <h6>For now i'm in Germany</h6>
    
    {request.headers}
    """
    return HttpResponse(template)

