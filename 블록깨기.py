import pygame
import random
import sys

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블록깨기 게임")

# 색상 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# 패들 설정
paddle_width, paddle_height = 100, 20
paddle_speed = 7  # 패들 속도를 낮춰 게임 플레이 조절
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - 30

# 공 설정
ball_radius = 10
ball_speed_x = 4
ball_speed_y = -4
ball_x = WIDTH // 2
ball_y = HEIGHT - 40

# 블록 설정
block_width, block_height = 50, 20
blocks = []
num_blocks_x = WIDTH // block_width
num_blocks_y = 4
for i in range(num_blocks_x):
    for j in range(num_blocks_y):
        block_x = i * block_width
        block_y = j * block_height + 30
        blocks.append(pygame.Rect(block_x, block_y, block_width, block_height))

# 폰트 설정
font = pygame.font.Font(None, 36)

# 게임 루프
clock = pygame.time.Clock()
running = True

while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 움직임
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT]:
        paddle_x += paddle_speed
    
    # 패들이 화면 밖으로 나가지 않도록 제한
    paddle_x = max(0, min(WIDTH - paddle_width, paddle_x))

    # 공 움직임
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 공이 화면의 경계를 벗어나지 않도록 반사
    if ball_x < ball_radius or ball_x > WIDTH - ball_radius:
        ball_speed_x = -ball_speed_x
    if ball_y < ball_radius:
        ball_speed_y = -ball_speed_y
    elif ball_y > HEIGHT:
        # 공이 화면 하단을 벗어나면 게임 오버
        running = False
        print("게임 오버!")

    # 공과 패들의 충돌 검사
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)
    if paddle_rect.colliderect(ball_rect):
        # 공이 패들에 닿으면 반사
        ball_speed_y = -ball_speed_y

    # 공과 블록의 충돌 검사
    for block in blocks[:]:
        if block.colliderect(ball_rect):
            ball_speed_y = -ball_speed_y
            blocks.remove(block)

    # 화면 지우기
    screen.fill(BLACK)

    # 패들 그리기
    pygame.draw.rect(screen, BLUE, paddle_rect)

    # 공 그리기
    pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_radius)

    # 블록 그리기
    for block in blocks:
        pygame.draw.rect(screen, WHITE, block)

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 수를 낮추어 게임이 느리게 실행되도록 설정
    clock.tick(30)

# 게임 종료 시 Pygame 종료
pygame.quit()
