from ninja import Router

router = Router()

@router.get("/home")
def home(request):
    return "ninja is easier than DRF"