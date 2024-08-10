import pygame
import sys
from pygame import mixer
# Initialize Pygame
pygame.init()

# Create a game window
screen_width, screen_height = 800, 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the caption of the window
pygame.display.set_caption("Amazing Ball Game")

# Displaying font
font = pygame.font.SysFont(None, 36)

# Define initial positions
player_x = 50
player_y = 250
player_width = 150
player_height = 20
player_speed = 5

# Defining ball positions
ball_x = 100
ball_y = 100
ball_radius = 30
ball_dx = 3  # Horizontal velocity
ball_dy = 6  # Vertical velocity

# Define rectangular
rect_x = 0
rect_y = 300
rect_width = 800
rect_height = 100

Score = 0

def displaying_score():
    Score_txt = font.render('score : {} '.format(Score),True,(0,0,0))
    screen.blit(Score_txt,(10,10))

game_over = False

# Game over message function
def show_game_over_message():
    game_over_message = font.render('Game Over! : You earned {} score '.format(Score), True, (0, 0, 0))
    text_rect = game_over_message.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(game_over_message, text_rect)

# Define the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
    

        # Update ball position
        ball_x += ball_dx
        ball_y += ball_dy
        
        # Bounce the ball off the screen edges
        if ball_x - ball_radius < 0 or ball_x + ball_radius > screen_width:
            ball_dx = -ball_dx  # Reverse horizontal direction
        if ball_y - ball_radius < 0 or ball_y + ball_radius > screen_height:
            ball_dy = -ball_dy  # Reverse vertical direction

        # Check for collision with the red rectangle (game over condition)
        if (rect_x < ball_x + ball_radius and
            rect_x + rect_width > ball_x - ball_radius and
            rect_y < ball_y + ball_radius and
            rect_y + rect_height > ball_y - ball_radius):
            print("Game Over! Ball touched the red rectangle.")
            game_over = True
            pygame.mixer.music.load('game-over-arcade-6435.mp3')
            pygame.mixer.music.play()

        # Check if the ball touches the green rectangle and bounce
        if (player_x < ball_x + ball_radius and
            player_x + player_width > ball_x - ball_radius and
            player_y < ball_y + ball_radius and
            player_y + player_height > ball_y - ball_radius):
            ball_dy = -ball_dy  # Reverse vertical direction
            pygame.mixer.music.load('springy-bounce-86214.mp3')
            pygame.mixer.music.play()
            Score+=1

        # Fill the screen with a background color
        screen.fill((255, 255, 255))  # White background

        # Draw the red rectangle
        pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height))

        # Draw the ball
        pygame.draw.circle(screen, (0, 0, 240), (ball_x, ball_y), ball_radius)

        # Draw the green player rectangle
        pygame.draw.rect(screen, (0, 250, 0), (player_x, player_y, player_width, player_height))

        # Displaying score
        displaying_score()

    else:
        # Display the game over message
        show_game_over_message()

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
