import pyxel as px

class App:
  def __init__(self):
    px.init(128,128)
    px.run(update(),draw())

  def update(self):
    pass

  def draw(self):
    pass
