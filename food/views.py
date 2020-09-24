from django.shortcuts import render
from .models import Food
import numpy as np


# Create your views here.
def randreci(request):

    Foods = Food.objects.all()
    random = set(np.random.randint(0, len(Foods), 20))

    radomFoods = []
    for idx in random:
        reci = ""
        for reciname in Foods[int(idx)].reci.split(','):
            reciname = reciname.strip()
            if reciname == "gaji":
                reci += '가지 '
            elif reciname == "gazzi":
                reci += '갈치 '
            elif reciname == "gamja":
                reci += '감자 '
            elif reciname == "goguma":
                reci += '고구마 '
            elif reciname == "godeunge":
                reci += '고등어 '
            elif reciname == "gochu":
                reci += '고추 '
            elif reciname == "nazzi":
                reci += '낙지 '
            elif reciname == "dangeun":
                reci += '당근 '
            elif reciname == "daepa":
                reci += '대파 '
            elif reciname == "pig":
                reci += '돼지고기 '
            elif reciname == "dubu":
                reci += '두부 '
            elif reciname == "mu":
                reci += '무 '
            elif reciname == "tomato":
                reci += '토마토 ' 
            elif reciname == "baechu":
                reci += '배추 '
            elif reciname == "buchu":
                reci += '부추 '
            elif reciname == "soseji":
                reci += '소세지 '
            elif reciname == "applge":
                reci += '사과 '
            elif reciname == "busut":
                reci += '버섯 '
            elif reciname == "dak":
                reci += '닭 '
            elif reciname == "beef":
                reci += '소고기 '
            elif reciname == "spam":
                reci += '스팸 '
            elif reciname == "eohobak":
                reci += '애호박 '
            elif reciname == "yangbaechu":
                reci += '양배추 '
            elif reciname == "yangpa":
                reci += '양파 '
            elif reciname == "hobak":
                reci += '호박 '
            elif reciname == "oe":
                reci += '오이 '
            elif reciname == "ojinge":
                reci += '오징어 '
            elif reciname == "oksusu":
                reci += '옥수수 '
            elif reciname == "chamchi":
                reci += '참치 '
            elif reciname == "kongnamul":
                reci += '콩나물 '
            elif reciname == "egg":
                reci += '달걀 '

        radomFoods.append({
            'name': Foods[int(idx)].name, 
            'image': Foods[int(idx)].image,
            'cookingOrder': Foods[int(idx)].cookingOrder,
            'reci': reci
        }) 

    context = {
        'Foods': radomFoods,
    }
    return render(request, 'food/randreci.html', context)


def recoreci(request):
    
    return render(request, 'food/recoreci.html')

