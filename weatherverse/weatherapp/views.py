from django.shortcuts import render
from django.contrib import messages
import requests

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'ballari'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f733af53d79626f7924e4e19640924cb'   
    PARAMS = {'units':'metric'}
    try:
          
          data = requests.get(url,params=PARAMS).json()
          description = data['weather'][0]['description']
          icon = data['weather'][0]['icon']
          temp = data['main']['temp']
          bgImg = ""
          condition = data['weather'][0]['main']
        
          if condition == 'Clear':
               bgImg = "https://th.bing.com/th/id/OIP.KdhDA_tBwWNH3AJoRVM9-AHaFJ?pid=ImgDet&w=474&h=329&rs=1"   #Sunny Image
          elif condition == 'Clouds':
               bgImg = "https://media.product.which.co.uk/prod/images/original/gm-36878fbb-cd68-4ccd-890d-81c074deba71-stormy-sky-inline.jpeg"    #Clouds image
          elif condition == 'Thunderstorm':
               bgImg = 'https://th.bing.com/th/id/OIP.BViEdVMtLDYCJ0F0G3kq6AHaGa?rs=1&pid=ImgDetMain' #Thunder
          elif condition == 'Drizzle':
               bgImg = 'https://th.bing.com/th/id/OIP.ZHM0wJc1KuGOk7bV6jy9RgHaE7?rs=1&pid=ImgDetMain' #Drizzle
          elif condition == 'Rain':
               bgImg = 'https://im.whatshot.in/img/2023/Jun/istock-1257951336-cropped-1687246216.jpg'
          elif condition == 'Snow':
               bgImg = 'https://th.bing.com/th/id/R.a8d73a02cab36d6338ef243f298818f3?rik=pl9kVorCdZ%2fkDw&riu=http%3a%2f%2fwallup.net%2fwp-content%2fuploads%2f2016%2f01%2f177192-nature-landscape-snow-winter-forest-trees-sunset-pine_trees.jpg&ehk=pUVrsLKH2tZTzXkep2P3BHDLJRJMaVjUzvKV8X6zXCw%3d&risl=&pid=ImgRaw&r=0'
          elif condition == 'Atmosphere':
               bgImg = 'https://th.bing.com/th/id/OIP.cUJMV5xpK0w6B_CAPOwL6gHaEo?rs=1&pid=ImgDetMain'
          elif condition == 'Smoke':
               bgImg = 'https://i.pinimg.com/originals/48/4f/7c/484f7cf750011fe79829b0d38af67d9f.jpg'

          return render(request,'weatherapp/index.html' , {'description':description , 'icon':icon ,'temp':temp  , 'city':city , 'exception_occurred':False, 'background_image_url':bgImg})
    
    
    except KeyError:
          exception_occurred = True
          messages.error(request,'Entered data is not available to API')   
          return render(request,'weatherapp/index.html' ,{'description':'---', 'icon':'---'  ,'temp':"---", 'city':'---' , 'exception_occurred':exception_occurred, 'background_image_url':'https://th.bing.com/th/id/R.218a2fdade289495bbc6b660a6b8bef2?rik=DPHI3hnwGMdwcg&riu=http%3a%2f%2fwallpapercave.com%2fwp%2fouJpeig.jpg&ehk=kCWtrwmWzJ5RYsWQSfHymFaUGijNia0HD%2fwVDd2k7Ug%3d&risl=&pid=ImgRaw&r=0' } )