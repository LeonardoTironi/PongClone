import sys, pygame, random

if __name__ == "__main__":
    WIDTH = 900
    HEIGHT = 500
    BACKGROUND_COLOR = (0,0,0)
    UNITS_COLOR = (255,255,255)
    player_velocity = 0
    ball_x_velocity = random.choice((2,-2))
    ball_y_velocity = random.choice((2,-2))
    player_points   = 0
    computer_points = 0
    computer_velocity = 0
    
    #The basic Pygame code
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Pong Clone')
    
    #Define the units
    player = pygame.Rect(10,HEIGHT/2-50,15,100) #Player
    computer = pygame.Rect(WIDTH-25,HEIGHT/2-50,15,100) #Computer
    ball = pygame.Rect(WIDTH/2-5,HEIGHT/2-5,32,32) #Ball

    #The player points
    font = pygame.font.SysFont('lucidasansroman', 32)
    playerText = font.render(f'{player_points}', True, UNITS_COLOR)
    playerTextRect = playerText.get_rect()
    playerTextRect.left = 60
    playerTextRect.top = 10
    #The computer points
    computerText = font.render(f'{computer_points}', True, UNITS_COLOR)
    computerTextRect = computerText.get_rect()
    computerTextRect.right = WIDTH-60
    computerTextRect.top = 10
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Moviment
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player_velocity += -3
                if event.key == pygame.K_s:
                    player_velocity += 3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player_velocity += 3
                if event.key == pygame.K_s:
                    player_velocity += -3
        #Show the screen and the points
        screen.fill(BACKGROUND_COLOR)
        screen.blit(playerText, playerTextRect)
        screen.blit(computerText, computerTextRect)

        #Ping Pong
        if ball.colliderect(player) or ball.colliderect(computer):
            ball_x_velocity=-ball_x_velocity*(1.02) #Makes it faster
        
        #Keep the ball inside the screen
        if ball.top <= 0 or ball.bottom>=HEIGHT:
            ball_y_velocity=-ball_y_velocity

        #Points
        if ball.left<0:
            computer_points+=1
            ball.center = (WIDTH/2, HEIGHT/2)
            ball_x_velocity = random.choice((2,-2))
            ball_y_velocity = random.choice((2,-2))
            computerText = font.render(f'{computer_points}', True, UNITS_COLOR)

        elif ball.right>WIDTH:
            player_points+=1
            ball.center = (WIDTH/2, HEIGHT/2)
            ball_x_velocity = random.choice((2,-2))
            ball_y_velocity = random.choice((2,-2))
            playerText = font.render(f'{player_points}', True, UNITS_COLOR)
        ball.x+=ball_x_velocity
        ball.y+=ball_y_velocity
        
        #player moviment
        player.y+=player_velocity
        if player.y<0:
            player.y=0
        elif player.bottom>HEIGHT:
            player.y=HEIGHT-100

        #Computer moviment
        if computer.bottom-50<ball.bottom:
            computer.y+=3
        elif computer.top+50>ball.bottom:
            computer.y-=3
        computer.y+=computer_velocity
        if computer.y<0:
            computer.y=0
        elif computer.bottom>HEIGHT:
            computer.y=HEIGHT-100


        #Draw the units
        pygame.draw.ellipse(screen, UNITS_COLOR,ball) #Ball
        pygame.draw.rect(screen, UNITS_COLOR, player) #Player
        pygame.draw.rect(screen, UNITS_COLOR, computer) #Computer
        center_line = pygame.draw.aaline(screen, UNITS_COLOR, (WIDTH/2-1,0),(WIDTH/2-1,HEIGHT),3) # Center Line

        #Update the screen
        pygame.display.update() 
        clock.tick(120)
