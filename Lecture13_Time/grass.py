from pico2d import *
import server
import collision

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        # 볼들과 잔디의 충돌을 누가? 잔디가 체크한다 -> 충돌을 누가 체크하는지가 충돌체크에서 굉장히 중요한 부분
        for ball in server.balls:
            if collision.collide(ball, self):
                ball.stop()

        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 0, 0, 1600-1, 50