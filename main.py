### 1. pygame 선언 및 패키지 임포트
import pygame
import random
from datetime import datetime
from datetime import timedelta

pygame.init()

### 2. pygame에 사용되는 전역변수 선언
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
size = [800, 800]
screen = pygame.display.set_mode(size)

done = False
play = True
clock = pygame.time.Clock()
last_moved_time = datetime.now()

# 키 방향에 대한 딕셔너리 선언
KEY_DIRECTION = {
    pygame.K_UP: 'N',
    pygame.K_DOWN: 'S',
    pygame.K_LEFT: 'W',
    pygame.K_RIGHT: 'E',
}

# 배경화면 바꾸기
SnakeLevel = (1)
SnakeLevel = str(SnakeLevel)
myfont = pygame.font.SysFont('malgungothic', 20)


### 3. 게임 구동에 필요한 함수와 클래스 선언

# 블럭을 그리기 위한 함수 선언
def draw_block(screen, color, position):
    block = pygame.Rect((position[1] * 20, position[0] * 20),  # 20을 곱하는 이유는 블록의 크기를 20픽셀로 설정
                        (20, 20))
    pygame.draw.rect(screen, color, block)


# 뱀에 관한 클래스 선언
class Snake:
    def __init__(self):  # 생성자 함수 : 뱀이 새로 만들어 질 때 기본으로 가지는 값 설정
        self.positions = [(0, 2), (0, 1), (0, 0)]  # 뱀의 위치
        self.direction = ''

    def draw(self):
        for position in self.positions:
            draw_block(screen, GREEN, position)

    def move(self):
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'N':
            self.positions = [(y - 1, x)] + self.positions[:-1]
        elif self.direction == 'S':
            self.positions = [(y + 1, x)] + self.positions[:-1]
        elif self.direction == 'W':
            self.positions = [(y, x - 1)] + self.positions[:-1]
        elif self.direction == 'E':
            self.positions = [(y, x + 1)] + self.positions[:-1]

    def grow(self):
        tail_position = self.positions[-1]
        y, x = tail_position
        if self.direction == 'N':
            self.positions.append((y - 1, x))
        elif self.direction == 'S':
            self.positions.append((y + 1, x))
        elif self.direction == 'W':
            self.positions.append((y, x - 1))
        elif self.direction == 'C':
            self.positions.append((y, x + 1))


# 사과에 관한 클래스 선언
class Apple:
    def __init__(self, position=(5, 5)):
        self.position = position

    def draw(self):
        draw_block(screen, RED, self.position)


### 4. pygame 무한루프(본체) 함수 선언
def runGame():
    global done, last_moved_time, text, SnakeLevel, play
    # 게임 시작 시, 뱀과 사과를 초기화
    snake = Snake()  # 뱀 클래스를 활용해 뱀 객체 1개 생성
    apple = Apple()  # 사과 클래스를 활용해 사과 객체 1개 생성

    while not done:
        clock.tick(10)  # 초당 프레임 수

        if play == True:
            image = pygame.image.load('space.jpg')
            image = pygame.transform.scale(image, size)
            screen.blit(image, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    play = False
                if event.type == pygame.KEYDOWN:
                    if event.key in KEY_DIRECTION:
                        snake.direction = KEY_DIRECTION[event.key]

            if timedelta(seconds=0.1) <= datetime.now() - last_moved_time:
                snake.move()
                last_moved_time = datetime.now()

            if snake.positions[0] == apple.position:
                snake.grow()
                apple.position = (random.randint(0, 19), random.randint(0, 19))
                text = myfont.render(SnakeLevel, False, (0, 0, 0))
                SnakeLevel = str(int(SnakeLevel) + 1)

            if snake.positions[0] in snake.positions[1:]:
                play = False

            # frame 마다 업데이트
            snake.draw()
            apple.draw()
            text = myfont.render('SnakeLevel : Lv.' + SnakeLevel, True, (255, 255, 255))
            screen.blit(text, (90, 10))
            pygame.display.update()

        else:
            image = pygame.image.load('gameover.jpg')
            image = pygame.transform.scale(image, size)
            screen.blit(image, (0, 0))
            text = myfont.render('snake game', True, (255, 255, 255))
            screen.blit(text, (90, 30))

            text = myfont.render('   Snake Lv.' + SnakeLevel, True, (255, 255, 255))
            screen.blit(text, (90, 60))

            text = myfont.render('press space to restart', True, (255, 255, 255))
            screen.blit(text, (90, 330))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        play = True
                        snake = Snake()  # 뱀 클래스를 활용해 뱀 객체 새롭게 1개 생성
                        apple = Apple()  # 사과 클래스를 활용해 사과 새롭게 객체 1개 생성
                        SnakeLevel = str(int(1))  # 스네이크 레벨 초기화

        pygame.display.update()


### 5. 프로그램 컨트롤 타워

runGame()
pygame.quit()