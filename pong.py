import pygame
import sys
import random
import math

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

FRAME_DELAY = 5
ROUND_WIN_DELAY = 500

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100

BLACK = (0, 0, 0)
GRAY = (120, 120, 120)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (129, 203, 248)
BROWN = (222, 184, 135)

PLAYER_MOVEMENT_UNITS = 5
COMPUTER_MOVEMENT_UNITS = 6
BALL_DEFAULT_SPEED = 3

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 10
        self.color = WHITE
        self.speed = BALL_DEFAULT_SPEED
        self.direction_x = 1
        self.direction_y = 1

    def flip_direction_x(self):
        self.direction_x *= -1

    def flip_direction_y(self):
        self.direction_y *= -1

    def throw_in(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.direction_x = 1 if random.randint(0,1) % 2 else -1
        self.speed = BALL_DEFAULT_SPEED

    def move(self):
        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed

    def keep_on_screen(self):
        if self.y - self.radius < 0 or self.y + self.radius > SCREEN_HEIGHT:
            self.direction_y *= -1

    def leaves_screen(self):
        return self.x + self.radius < 0 or self.x - self.radius > SCREEN_WIDTH

class Paddle:
    def __init__(self, x, color = WHITE):
        self.x = x
        self.y = SCREEN_HEIGHT // 2
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.goal_line_x = x + PADDLE_WIDTH if x < SCREEN_WIDTH // 2 else x
        self.color = color
        self.score = 0
        self.predicted_y = None

    def collides_with_ball(self, ball):
        left_side_hit, left_side_overlap = self.__collides_with_ball(ball, self.x)
        if left_side_hit:
            return left_side_hit, left_side_overlap

        right_side_hit, right_side_overlap = self.__collides_with_ball(ball, self.x + self.width)
        return right_side_hit, right_side_overlap

    def __collides_with_ball(self, ball, x):
        a = 1
        b = -2 * ball.y
        c = ball.y**2 + x**2 - 2 * x * ball.x + ball.x**2 - ball.radius**2
        discriminant = b**2 - 4 * a * c
        if discriminant < 0:
            # No solution, the ball does not reach the goal line
            return (False, False)
        elif discriminant == 1:
            # One solution, the ball's edge collides with the paddle
            y = (-b + (math.sqrt(discriminant))) / (2 * a)
            return (True, self.y < y < self.y + self.height)
        else:
            # Two solutions, the ball and the paddle have two intersection
            # points, this is due to the increments of the ball movement
            sqrt_discriminant = math.sqrt(discriminant)
            y0 = (-b + (sqrt_discriminant)) / (2 * a)
            y1 = (-b - (sqrt_discriminant)) / (2 * a)
            return (True, self.y < y0 < self.y + self.height or self.y < y1 < self.y + self.height)
        

def computer_predict(ball, computer):
    predicted_dir = ball.direction_y
    y = ball.y
    for x in range(ball.x + ball.radius, computer.x, ball.speed):
        if y - ball.radius < 0 or y + ball.radius > SCREEN_HEIGHT:
            predicted_dir *= -1
        y += ball.speed * predicted_dir
    return y

def ai_move(ball, computer):
    if not round_winner and ball.direction_x == 1 and ball.x > SCREEN_WIDTH // 2:
        predicted_y = computer.predicted_y or computer_predict(ball, computer)
        if predicted_y > 0 and predicted_y < SCREEN_HEIGHT and (predicted_y < computer.y or predicted_y > computer.y + computer.height):
            computer.y += COMPUTER_MOVEMENT_UNITS * (-1 if predicted_y < computer.y else 1)

def display_text(text, x, y):
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(text, False, WHITE)
    screen.blit(textsurface, (x, y))    

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong Game | codingboost.com')
pygame.font.init()

ball = Ball()
ball.throw_in()
player = Paddle(x = 30, color = LIGHT_BLUE)
computer = Paddle(x = SCREEN_WIDTH - 60, color = BROWN)
round_winner = None
tick = 0
last_key = 1
while True:
    pygame.time.delay(FRAME_DELAY)
    screen.fill(BLACK)

    ball.move()
    ball.keep_on_screen()

    if round_winner and ball.leaves_screen():
        round_winner.score += 1
        round_winner = None
        ball.throw_in()
        pygame.time.delay(ROUND_WIN_DELAY)
        continue
    
    player_goal_reached, player_defended = player.collides_with_ball(ball)
    # The ball crosses the goal line
    if player_goal_reached:       
        # The round hasn't been won yet, the player hits the ball back
        if not round_winner and player_defended:
            ball.flip_direction_x()
            if last_key:
                ball.direction_y = last_key
        # The round hasn't been won yet, the player fails to hit back, computer scores
        elif not round_winner and not player_defended:
            round_winner = computer
        # The round has been won, though the paddle hits the ball
        elif round_winner and player_defended:
            ball.flip_direction_y()
        
    computer_goal_reached, computer_defended = computer.collides_with_ball(ball)
    if computer_goal_reached:
        if not round_winner and computer_defended:
            ball.flip_direction_x()
        elif not round_winner and not computer_defended:
            round_winner = player
        elif round_winner and computer_defended:
            ball.flip_direction_y()
            
    # Speed up the game by one unit in every 1000 ticks
    tick += 1
    if tick % 1000 == 0:
        ball.speed += 1

    # Computer movement
    ai_move(ball, computer)

    display_text('Player', 150, 0)
    display_text(str(player.score), 180, 45)
    display_text('Computer', 400, 0)
    display_text(str(computer.score), 460, 45)
    pygame.draw.rect(screen, player.color, (player.x, player.y, player.width, player.height), 0)
    pygame.draw.rect(screen, computer.color, (computer.x, computer.y, computer.width, computer.height), 0)
    pygame.draw.circle(screen, ball.color, (ball.x, ball.y), ball.radius)
    for i in range(1, SCREEN_HEIGHT // 10):
        if i % 2 == 0:
            pygame.draw.rect(screen, GRAY, (SCREEN_WIDTH // 2, i * 10, 10, 10), 0)
    pygame.display.update()

    # Event handling
    last_key = None
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        goal_reached, overlap = player.collides_with_ball(ball)
        if goal_reached and player.y - PLAYER_MOVEMENT_UNITS < ball.y + ball.radius:
            continue
        player.y = 0 if player.y - PLAYER_MOVEMENT_UNITS < 0 else player.y - PLAYER_MOVEMENT_UNITS 
        last_key = -1
        
    if keys[pygame.K_DOWN]:
        goal_reached, overlap = player.collides_with_ball(ball)
        if goal_reached and player.y + player.height + PLAYER_MOVEMENT_UNITS > ball.y - ball.radius:
            continue
        player.y = SCREEN_HEIGHT - player.height if player.y + player.height + PLAYER_MOVEMENT_UNITS > SCREEN_HEIGHT else player.y + PLAYER_MOVEMENT_UNITS
        last_key = 1
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
