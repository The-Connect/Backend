from ninja import Router

router = Router()

@router.get("/home")
def home(request):
    return "JC ninja is easier than DRF"