from PIL import Image, ImageDraw, ImageFont

class Character:
  def __init__(self):
    self.cat_left = Image.open('images/character/cat (2).png')
    self.angry = Image.open('images/character/cat_angry.png')
    self.x_position = 120
    self.y_position = 210
    self.speed = 5
    self.state = None

  def move(self, up_down, left_right):
    if up_down == 'up':
        if self.y_position - self.spd < 0:
          pass #밖으로 안나가게 처리함
        else :
           self.y_position -= self.spd
    elif up_down == 'down':
       if self.y_position + self.spd > 215:
        pass
       else:
         self.y_position += self.spd
    if left_right == 'left':
      if(self.x_position - self.speed < 0 ):
        pass
      else:
        self.x_position += self.speed
    elif left_right == 'right' :
      if(self.x_position +self.speed > 215):
        pass
      else:
        self.x_position += self.speed