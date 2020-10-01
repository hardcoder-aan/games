import pygame
import math

pygame.init()

body = pygame.display.set_mode((500, 400))

# setting icon and set_caption

pygame.display.set_caption("Mini Archer")
icon = pygame.image.load("arrowIcon.png")
pygame.display.set_icon(icon)

# setting score

score = 0
font = pygame.font.Font("freesansbold.ttf", 20)

textX = 10
textY = 10


def show_score(x, y):
	sc_val = font.render("SCORE: " + str(score), True, (0, 0, 0))
	body.blit(sc_val, (x, y))


# setting timer

time = 180
timeX = 280
timeY = 10

def timer(x, y):
	time_limit = font.render("TTIME LEFT: " + str(time), True, (30, 200, 0))
	body.blit(time_limit, (x, y))

# setting Game over

font2 = pygame.font.Font("freesansbold.ttf", 30)
overX = 130
overY = 170

def game_over(x, y):
	g_over = font2.render("GAME OVER", True, (0, 0, 0))
	body.blit(g_over, (x, y))

# initial attributes of bow

bowimg = pygame.image.load("bow.png")
bowX = 2
bowY = 10
speed = 0.2

# initial attributes of arrow

arrowimg = pygame.image.load("arrow2.png")
arrowX = 2
arrowY = 10
arrow_speed = 0
arrow_state = "ready"

# initial attributes of apple

appleimg = pygame.image.load("apple.png")
appleX = 451
appleY = 0
apple_speed = 0.1

# function for apple

def apple(x, y):
	body.blit(appleimg, (x, y))

# function for arrow

def arrow(x, y):
	global arrow_state
	arrow_state = "shot"
	body.blit(arrowimg, (x, y))

# function for bow

def bow(x, y):
	body.blit(bowimg, (x, y))


# defining distance function between arrow and apple

def distance(appleX, appleY, arrowX, arrowY):
	dis = math.sqrt(math.pow(appleX - arrowX, 2) + math.pow(appleY - arrowY, 2))
	if dis <= 16:
		return True
	else:
		return False

run =True

# gane mainloop

while run:
	body.fill((255, 255, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	# setting the bow movable with key commands

	key_press = pygame.key.get_pressed()
	if key_press[pygame.K_DOWN]:
		bowY += speed
	if key_press[pygame.K_UP]:
		bowY -= speed

	# key press for shooting arrow

	if key_press[pygame.K_SPACE]:
		if arrow_state == "ready":
			arrowX = bowX
			arrowY = bowY
			arrow(arrowX, arrowY)
			arrow_speed = 0.6

	arrowX += arrow_speed

	# blitting arrow image to the screen by calling arrow function

	if arrow_state == "shot":
		arrow(arrowX, arrowY)

	# settin arrow to bow if it goes out of the screen

	if arrowX >= 500:
		arrowX = bowX
		arrowY = bowY
		arrow_state = "ready"

	# setting boundaries for bow

	if bowY >= 352:
		bowY = 352
	if bowY <= 0:
		bowY = 0
		

	# setting apple movable

	appleY += apple_speed

	# apple should come back to screen after going out

	if appleY >= 400:
		appleY = 0

	# arrow hitting apple

	collision = distance(appleX, appleY, arrowX, arrowY)
	if collision:
		arrowX = bowX
		arrowY = bowY
		arrow_state = "ready"
		appleX = 451
		appleY = 0
		score += 1

	# calling functions for apple, bow and score

	bow(bowX, bowY)
	apple(appleX, appleY)
	show_score(textX, textY)
	timer(timeX, timeY)

	time -= .001

	if time <= 0:
		speed = 0
		apple_speed = 0
		arrow_speed = 0
		time = 0
		game_over(overX, overY)
		
	
	pygame.display.update()

