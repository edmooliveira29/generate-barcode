from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    def validate_and_create(self, http_request: HttpRequest):
        # body = http_request.body
        # product_code = body["product_code"]
        print("Estou aqui", http_request)
        print("Estou aqui", self)
        return HttpResponse(status_code=200, body={"hello": "world"})