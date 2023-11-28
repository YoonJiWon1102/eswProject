from PIL import Image, ImageDraw, ImageFont

class Background:
  def __init__(self):
    self.backgroundList=[]
    name="background"
    for i in range(10) :
      background = Image.open('images/background/'+name+str(i+1)+'.png').convert('RGBA')
      self.backgroundList.append(background)