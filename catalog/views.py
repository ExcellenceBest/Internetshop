from django.shortcuts import render
from django.http import HttpRequest



def main(request: HttpRequest):
    foto = {
        'Болояж на короткие волосы': "https://avatars.mds.yandex.net/i?id=7d1d3280b2c6393280fe8f55a0f3016c676661f66b90c621-5859721-images-thumbs&n=13",
        'Пепелный блонд': 'https://avatars.mds.yandex.net/i?id=e253e5961f68c1179e6f4a04d0c8edc652d9fb33-9875416-images-thumbs&n=13',
        'Айртач': 'https://avatars.mds.yandex.net/i?id=6c547020a3a6195478b19687b849b48255f7ba25-11386386-images-thumbs&n=13',
        '4': 'https://avatars.mds.yandex.net/i?id=7ed4105ed14ed965035779d2c784bf283f60774b-9882341-images-thumbs&n=13',
        '5': 'https://avatars.mds.yandex.net/i?id=7c0e5523a3b670ef674cddc1c6ad91777d09571a-7663003-images-thumbs&n=13',
        '6': 'https://avatars.mds.yandex.net/i?id=ba5e7efc411db4f5664824b19bc6329958aa7ac2-9227286-images-thumbs&n=13'
    }



    context = {
            "data": foto,

        }

    return render(request, template_name='catalog.html', context=context)


def redirect(request: HttpRequest):
    return render(request, '404.html')

