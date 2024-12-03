from django.http import HttpResponse

def index (request):
    return HttpResponse("""
                        <center>
                         <a href="/admin">Admin</a> <br>
                         <a href="polls">Votação</a>
                        """)