from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    global direct  # 1 = 오른쪽 2 = 왼쪽
    global mousex, mousey
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mousex = event.x
            mousey = event.y
            #     x, y = event.x, KPU_HEIGHT - 1 - event.y    # 0부터 시작하기 때문에 - 1을 해줌
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)

# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
mousex = 0
mousey = 0
direct = 1
# hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    # delay(0.05)
    if direct == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    if direct == 2:     # 이미지 뒤집기
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    if mousex != x:
        if mousex > x:
            x += 2
            direct = 1
        elif mousex < x:
            x -= 2
            direct = 2
    if KPU_HEIGHT - 1 - mousey != y:
        if KPU_HEIGHT - 1 - mousey > y:
            y += 1
        elif KPU_HEIGHT - 1 - mousey < y:
            y -= 1
    # FlipImage = character.transpose(Image.FL)
    # FlipImage.show()
    cursor.draw(mousex, KPU_HEIGHT - 1 - mousey)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




