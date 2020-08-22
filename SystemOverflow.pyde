'''
Name: Paul Okenne
Program:
    Thsgame entails an account platform for users to buy games and play purchased games. 
    Key features:
        -User will be able to make unique accounts [Stored in csv file]
    -User’s purchased games will be stored [Stored in csv file]
    -User’s highest score in each game will be stored  [Stored in csv file]
    -Lists of games:   -Soccer pinball
                       -Keep the ball up
                       -Memozories [Memory game: try to recollect patterns]


'''

#|-----------------------------------------------------------------------------------------------------------------------|
#|-----------------------------------------------------------------------------------------------------------------------|
#This section of the code BELOW is designated for the  memozories game
#|-----------------------------------------------------------------------------------------------------------------------|
#|-----------------------------------------------------------------------------------------------------------------------|

def M_sequence():#This function displays a sequence of colours to the user
    global M_sequenceStorage, M_numbSeq, M_sequenceTime
    if len(M_sequenceStorage) == M_numbSeq: #Check if sequence shown has the the correct amount of sequences for the level
        return True
    if millis()/1000 %2==0:    
        frameRate(1)
        if len(M_sequenceStorage) < M_numbSeq: #Check if sequence storage has required sequences
            M_sequenceStorage.append(random.choice([[100, height / 3, -3593922], [300, height / 3, -16317024], [
                                     500, height / 3, -16346319], [100, height / 1.5, -1712372], [300, height / 1.5, -7536498], [500, height / 1.5, -6974059]]))
        rectMode(CENTER)
        fill(255)
        rect(M_sequenceStorage[len(M_sequenceStorage) - 1][0],
             M_sequenceStorage[len(M_sequenceStorage) - 1][1], 50, 50)

    return False


def M_sequenceCheck():#The function determines whether users input is correct
    global M_check, M_savedTime, M_timeCountDown, M_passedTime, M_sequenceStorage, M_numbSeq, M_countState, M_XcountState, M_sequenceTime, M_counter, M_score, M_endGame
    M_counter += 1
    if M_counter == M_numbSeq:
        M_check, M_savedTime, M_timeCountDown, M_passedTime, M_sequenceStorage, M_numbSeq, M_countState, M_XcountState, M_sequenceTime, M_counter, M_score = False, 0, 7, 0, [
        ], M_numbSeq + 1, True, 0, 0, 0, M_score + 1
    else:
        if get(mouseX, mouseY) == M_sequenceStorage[M_counter - 1][2]: #Checks if user click is equal to the correct box according to thegiven sequence 
            pass
        else:
            M_endGame = True #The User has lost
            
#|-----------------------------------------------------------------------------------------------------------------------|
#|-----------------------------------------------------------------------------------------------------------------------|
#The functions BELOW is for the Keep It Up Game
#|-----------------------------------------------------------------------------------------------------------------------|
#|-----------------------------------------------------------------------------------------------------------------------|
class FTU_Ball: #Class FTU_Ball stores properties of the ball

    def __init__(self, x, y, xS, yS, ballMove):#Create an object when postions and speeds are given
        self.x, self.y, self.xS, self.yS, self.ballMove = x, y, xS, yS, ballMove
        self.menu()

    def menu(self):#This function updates the properties of the ball
        self.move()#Move ball
        self.collision()#Check for collisions
        self.display()#Dispaly updated ball postion

    

    def move(self):#The function moves the ball
        global savedX, savedY, FTU_counter, BallStorage, FTU_balls
        if self.ballMove != True and (self.xS == 0) and self.yS == 0:#Check if ball is stationary
            strokeWeight(3)
            stroke(255)
            line(self.x, self.y, mouseX, mouseY)#display a line that shows the user where he/she is aiming
            savedX, savedY = self.x, self.y
            fill('#D10F49')
            text("X " + str(FTU_balls + 1), self.x + 20, self.y + 5)
        if mousePressed and (self.xS == 0) and self.yS == 0:#Check if mouse is pressed and ball is stationary
            self.ballMove = True
        if self.ballMove == True: 
            xDiff = mouseX - self.x #Move the ball in the x-dir
            yDiff = mouseY - self.y#Move the ball in the y-dir
            unitSpeed = sqrt((xDiff ** 2 + yDiff ** 2) / 100)#Unit Speed(Using formula I create to the overall velocity constant)
            self.xS = xDiff / unitSpeed #Update x-dir speed
            self.yS = yDiff / unitSpeed #Update y-dir speed

            self.ballMove = False 

        self.x += self.xS #Move ball x-postion
        self.y += self.yS #Move ball y-postion

    def display(self):#This function displays the ball
        global FTU_Ballx, FTU_Bally, FTU_BallxS, FTU_BallyS, FTU_ballMove, FTU_balls, savedX, savedY, FTU_trailState
        FTU_Ballx, FTU_Bally, FTU_BallxS, FTU_BallyS = self.x, self.y, self.xS, self.yS
        FTU_ballMove = self.ballMove
        if self.ballMove != True and (self.xS == 0) and self.yS == 0: #Check if ball is stationary
            fill('#D10F49')  # Ball is red
        else:fill('#57C14A')  # Bally is green
        strokeWeight(3)
        stroke(0)
        ellipse(self.x, self.y, 20, 20)

    def collision(self):#Collision Detetion
        global FTU_Ballx, FTU_Bally, FTU_BallxS, FTU_BallyS, BrickStorage
        if self.x <= 20:#Error detection with screen boundaries
            self.xS, self.x = self.xS * -1, 22
        if self.x >= width - 30:
            self.xS, self.x = self.xS * -1, width - 32
        if self.y >= height - 75:
            self.xS, self.yS, self.y, self.ballMove = 0, 0, height - 75, False
        if self.y <= 30:
            self.yS, self.y = self.yS * -1, 33

        r = 10
        for index in range(len(BrickStorage) - 1): #The process checks collision with reapeariing bricks
            if dist(self.x, self.y, BrickStorage[index][0] + 15, BrickStorage[index][1] + 15) < 25:
                if (self.y + r < BrickStorage[index][1]) and (self.x >= BrickStorage[index][0] or self.x <= BrickStorage[index][0] + 30):
                    self.yS, BrickStorage[index][
                        2] = self.yS * -1, BrickStorage[index][2] + 1
                if (self.y - r < BrickStorage[index][1]) and (self.x >= BrickStorage[index][0] or self.x <= BrickStorage[index][0] + 30):
                    self.yS, BrickStorage[index][
                        2] = self.yS * -1, BrickStorage[index][2] + 1
                if (self.x + r > BrickStorage[index][0]) and (self.y >= BrickStorage[index][1] or self.y <= BrickStorage[index][1] + 30):
                    self.xS, BrickStorage[index][
                        2] = self.xS * -1, BrickStorage[index][2] + 1
                if (self.x - r < BrickStorage[index][0]) and (self.y >= BrickStorage[index][1] or self.y <= BrickStorage[index][1] + 30):
                    self.xS, BrickStorage[index][
                        2] = self.xS * -1, BrickStorage[index][2] + 1


def trail():#This function creates a trail of balls following the head ball
    # Use this function to increase ball count after points are scored
    global FTU_balls, BallStorage, BrickStorage
    for a in range(len(BallStorage) - 1):  # Move last index to the front
        BallStorage[a] = BallStorage[a + 1]

    if len(BallStorage) < (FTU_balls * 5): #This process creates a storage of trail balls 
        BallStorage.append([FTU_Ballx, FTU_Bally])
    else:
        BallStorage[(FTU_balls * 5) - 1] = [FTU_Ballx, FTU_Bally] #Move farest back trail ball to the front

    for a in range(len(BallStorage)):#This process displays trail balls using the ball storage
        if a % 5 == 0:
            ellipse(BallStorage[a][0], BallStorage[a][1], 20, 20)
    
    for a in range(len(BallStorage)):#This process determines if the balls hit the bricks
        for index in range(len(BrickStorage)):
            if dist(BallStorage[a][0], BallStorage[a][1], BrickStorage[index][0] + 15, BrickStorage[index][1] + 15) < 25:
                if (BallStorage[a][1] + 10 < BrickStorage[index][1]) and (BallStorage[a][0] >= BrickStorage[index][0] or BallStorage[a][0] <= BrickStorage[index][0] + 30):
                    BrickStorage[index][2] = BrickStorage[index][2] + 1
                if (BallStorage[a][1] - 10 < BrickStorage[index][1]) and (BallStorage[a][0] >= BrickStorage[index][0] or BallStorage[a][0] <= BrickStorage[index][0] + 30):
                    BrickStorage[index][2] = BrickStorage[index][2] + 1
                if (BallStorage[a][0] + 10 > BrickStorage[index][0]) and (BallStorage[a][1] >= BrickStorage[index][1] or BallStorage[a][1] <= BrickStorage[index][1] + 30):
                    BrickStorage[index][2] = BrickStorage[index][2] + 1
                if (BallStorage[a][0] - 10 < BrickStorage[index][0]) and (BallStorage[a][1] >= BrickStorage[index][1] or BallStorage[a][1] <= BrickStorage[index][1] + 30):
                    BrickStorage[index][2] = BrickStorage[index][2] + 1


def FTU_Bricks(BrickStorage, appendState): #This function stores and displays the bricks
    global FTU_Score, FTU_balls

    if (FTU_balls) <= 2:#Check numbers of ball
        testVar = [random.randint(5, width - 40), random.randint(30, height / 2), 0, [
            random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)]]
    else:
        testVar = [random.randint(5, width - 40), random.randint(30, height / 3), 0]

    for x in range(len(BrickStorage) - 1):#This process ensures that there is not a lot of overlap
        if (testVar[0] >= BrickStorage[x][0] - 30 and testVar[0] <= BrickStorage[x][0] + 40) and (testVar[1] >= BrickStorage[x][1] - 30 and testVar[1] <= BrickStorage[x][1] + 40):
            appendState = False

    if testVar[1] % 30 != 0:#Ensures the bricks are spaced out
        appendState = False
    if appendState == True:BrickStorage.append(testVar)#Add bricks

    try:
        for x in range(len(BrickStorage) - 1): #This process checks if bricks hitpoint has been reached
            if BrickStorage[x][2] >= 10:
                del(BrickStorage[x])#Deletes bricks
                FTU_Score += 1
    except:
        pass
    stroke(1)
    for x in range(len(BrickStorage) - 1): #Display bricks
        fill(BrickStorage[x][3][0], BrickStorage[x][3][1], BrickStorage[x][3][2])
        rect(BrickStorage[x][0], BrickStorage[x][1], 30, 30)


#|-----------------------------------------------------------------------------------------------------------------------|
#|-----------------------------------------------------------------------------------------------------------------------|
#This section of code BELOW is for the Soccer Mania game 
#|-----------------------------------------------------------------------------------------------------------------------|
#|-----------------------------------------------------------------------------------------------------------------------|
class Ball:#This class stores properties of the ball

    def __init__(self, x, y, xS, yS):#Prompt user for postions, and speeds to create a ball object
        self.x, self.y, self.xS, self.yS = x, y, xS, yS
        self.menu()

    def menu(self): #This function updates the properties of the ball
        self.move()#Ball moves
        self.collision()#Collision detection
        self.display()#Display updated ball

    def move(self):#Moves ball
        self.x += self.xS #
        self.y += self.yS

    def display(self):#This function displays the ball
        global ballX, ballY, xSpeed, ySpeed
        ballX, ballY, xSpeed, ySpeed = self.x, self.y, self.xS, self.yS
        image(loadImage("gameBall.png"), ballX, ballY)

    def collision(self):#This function checks collision with the ball
        global SMscoreState, SMenemyS1, SMenemyS2, SMlives

        #The processes below check collisions with soccer field boundaries
        if self.x <= 70 and ((self.y >= 100 and self.y <= 250) or (self.y >= width - 270 and self.y <= width - 95)): 
            self.xS = (self.xS) * -1
        if self.x >= width - 100 and ((self.y >= 100 and self.y <= 250) or (self.y >= width - 270 and self.y <= width - 95)):
            self.xS = (self.xS) * -1
        if self.y <= 100:
            self.yS = (self.yS) * -1
        if self.y >= height - 130:
            self.yS = (self.yS) * -1
        if self.x < 70 and ((self.y >= 100 and self.y <= 250) or (self.y >= width - 270 and self.y <= width - 95)):
            self.x = 75
        if self.x >= width - 100 and ((self.y >= 100 and self.y <= 250) or (self.y >= width - 270 and self.y <= width - 95)):
            self.x = width - 105

        # The processes below are Collisions detection with ball & User & Enemy
        if self.x >= 60 and self.x <= 105 and self.y >= SMuserY - 10 and self.y <= SMuserY + 60:
            if self.xS != 30 and self.xS > 0:
                self.xS = (self.xS + 1) * -1
            elif self.xS != -30 and self.xS < 0:
                self.xS = (self.xS - 1) * -1
            else:
                self.xS = (self.xS) * -1
        if self.x >= width - 240 and self.x <= width - 195 and self.y >= SMenemyY1 - 10 and self.y <= SMenemyY1 + 60:
            if self.xS != 30 and self.xS > 0:
                self.xS = (self.xS + 1) * -1
            elif self.xS != -30 and self.xS < 0:
                self.xS = (self.xS - 1) * -1
            else:
                self.xS = (self.xS) * -1
        if self.x >= width - 140 and self.x <= width - 95 and self.y >= SMenemyY2 - 10 and self.y <= SMenemyY2 + 60:
            if self.xS != 30 and self.xS > 0:
                self.xS = (self.xS + 1) * -1
            elif self.xS != -30 and self.xS < 0:
                self.xS = (self.xS - 1) * -1
            else:
                self.xS = (self.xS) * -1

        # This process checks if user gets scored on
        if (self.x <= 40) and self.y >= height / 2.5 and self.y <= height / 2.5 + 120:
            SMscoreState, SMlives = 1, SMlives - 1
            self.x = width / 2.3
            self.y = height / 2.3

        # This process checks if enemy is scored on
        if (self.x > width - 70) and self.y >= height / 2.5 and self.y <= height / 2.5 + 110:
            self.x, self.y, SMscoreState = width / 2.3, height / 2.3, 2
            if SMenemyS1 < 0:
                SMenemyS1 -= 1
            if SMenemyS2 < 0:
                SMenemyS2 -= 1
            if SMenemyS1 > 0:
                SMenemyS1 += 1
            if SMenemyS2 > 0:
                SMenemyS2 += 1

#|-----------------------------------------------------------------------------------------------------------------------|
#|-----------------------------------------------------------------------------------------------------------------------|
#This Section of Code is for the user's account and it's properties 
#|-----------------------------------------------------------------------------------------------------------------------|
class Account:
    def __init__(self, username, password, mode):#Objects needs username,pass,and mode to creat an object
        global state, menuGo, loginStatus
        self.username, self.password, self.mode = username, password, mode
        if mode == 'Create': #Check if an account is being created
            check = self.create()
            if check == True:
                mode = 'Login'
            else:
                loginStatus = False

        if mode == 'Login':#Check if an account is being logined to
            check = self.login()
            if check == True:
                print("LOGIN success")
                self.menu()
            else:
                loginStatus = False
                print("Login FAILED")

    def login(self):#This function allows people to enter into their account
        with open('Overflow.csv', 'r') as csvFile:  # Opens csv file
            readCsvFile = csv.DictReader(csvFile)
            for user in readCsvFile: #This process check the csv file to see if input is correct
                if (self.username == user['Username']) and (self.password == user['Password']):
                    self.balance, self.gamesOwned, self.SPB, self.KBU, self.memozories = user['Account Balance'], user[
                        'Games Owned'], user['Soccer Mania'], user['Keep It Up'], user['Memozories Score']
                    return True
            return False

    def create(self):#This function creates a new account for the user
        check = True
        with open('Overflow.csv', 'r') as csvFile:  # Opens csv file and checks if username is present
            readCsvFile = csv.DictReader(csvFile)
            for user in readCsvFile:
                if (self.username == user['Username']):
                    check = False
        if check == True:
            with open('Overflow.csv', 'a') as csvFile:  # Opens csv file and adds user inputed info
                writer = csv.DictWriter(csvFile, fieldnames=[
                                        'Username', 'Password', 'Account Balance', 'Games Owned', 'Soccer Mania', 'Keep It Up', 'Memozories Score'])
                writer.writerow({'Username': self.username, 'Password': self.password, 'Account Balance': 50,
                                 'Games Owned': '', 'Soccer Mania': 'N/A', 'Keep It Up': 'N/A', 'Memozories Score': 'N/A'})
        return check

    def buttonCreate(self, x, y, w, h, Img, name):#This functions creates buttons for games
        fill(0)
        textSize(15)
        strokeWeight(6)
        rect(x, y, w, h)
        fill(255)
        line(x, y + 125, x + 200, y + 125)
        image(Img, x + 5, y + 5)
        text(name, x + 50, y + 145)

        check = False
        #Check if user owns the game
        if name in str(self.gamesOwned):check = True

        if (mouseX >= x and mouseX <= x + w) and (mouseY >= y and mouseY <= y + h): #Check if user is hoverig over box
            strokeWeight(1)
            textSize(25)
            if check == False:#User has not bought game
                fill(0)
                rect(x + 70, y + 50, 55, 25)
                fill(255)
                text("PAY", x + 75, y + 70)
            if check == True:#User has  bought game
                fill(0)
                rect(x + 70, y + 50, 70, 25)
                fill(255)
                text("PLAY", x + 75, y + 70)
        return check  # It needs to return true or false for the mousePressed section
       

    def payment(self, game): #This function allows the user to pay for game
        gameCost = [['Soccer Mania', 29.99], ['Keep It Up', 24.99], ['Memozories', 19.99]]
        for index in range(len(gameCost)):#The process finds the desired games the user wishes to buy and buys it if the balance can buy game
            if gameCost[index][0] == game:
                if float(self.balance) - gameCost[index][1] > 0: #Check if the game can be bought
                    pay = JOptionPane.showConfirmDialog(None, "Game: '" + game + "' \n----------------------------------------\nCurrent Balance: $" + str(float(self.balance)) + "\nGame Cost: $" + str(
                        gameCost[index][1]) + "\n----------------------------------------\nWould you like to pay?", "OVERFLOW PAYMENT", JOptionPane.YES_NO_OPTION)
                    if pay == 0:#Check if user inputed 'yes'
                        self.balance = float(self.balance) - gameCost[index][1]
                        self.gamesOwned += game + ','
                    if pay == -1 or pay == 1:#Check if user inputed 'no'
                        pass
                else:
                    #Dispay error detection
                    JOptionPane.showMessageDialog(None, "Game: '" + game + "' \n----------------------------------------\nCurrent Balance: $" + str(float(self.balance)) + "\nGame Cost: $" + str(
                        gameCost[index][1]) + "\n----------------------------------------\nError Message: INSUFFICIENT FUNDS", "OVERFLOW PAYMENT", JOptionPane.ERROR_MESSAGE)

    def Buttons(self, x, y, w, h, img, str, colour1, colour2): #Buttons for games
        noFill()
        strokeWeight(2)
        rect(x, y, w, h)
        image(img, x + 40, y + 5)
        if (mouseX >= x and mouseX <= x + w) and (mouseY >= y and mouseY <= y + h):
            fill(colour1)
        else:
            fill(colour2)
        text(str, x + 90, y + 35)

    def SM(self): #This function allows the user to play Soccer Mania
        global SMstate, menuOpen, state, SMuserY, SMspeed, xSpeed, ySpeed, SMuserX, SMenemyY1, SMenemyY2, SMenemyS1, SMenemyS2, SMscoreState, SMscore, ballX, ballY, xSpeed, ySpeed, SMlives

        menuOpen = False

        if SMstate == 0: #Game Into page
            background(loadImage("soccerMania.png"))
            strokeWeight(5)
            fill(255)
            textSize(30)
            fill('#64AF5A')
            text("SOCCER MANIA", width / 3, height / 4.5)

            self.Buttons(width / 3, height / 3 + 10, 220, 50,
                         loadImage("playIcon.png"), "PLAY", '#64AF5A', 255) #Play button
            self.Buttons(width / 3, height / 3 + 70, 220, 50,
                         loadImage("infoIcon.png"), "INFO", '#64AF5A', 255)#Info button
            self.Buttons(width / 3, height / 3 + 130, 220, 50,
                         loadImage("exit.png"), "EXIT", '#64AF5A', 255)#Exit button
            image(loadImage("gameBall.png"), width / 2.3, height - 150)

        if SMstate == 2:#Checks if the user chose to exit program
            menuOpen, SMstate, state = True, -1, 3
        if SMstate == 3:#Checks if the user chose to see game info
            JOptionPane.showMessageDialog(
                None, "System Mechanics\nUsing WASD, avoid getting scored on 7 times.\n\nPoints System\n\t-25 points are rewarded when you scored\n\t-15 points are lost when you conced a goal", "Game Info", JOptionPane.PLAIN_MESSAGE)
            SMstate = 0

        if SMstate == 1:#Check if user chose to play game
            background(loadImage("field.png"))
            if SMlives != 0:#Check if user lives is greater than 0
                ball1 = Ball(ballX, ballY, xSpeed, ySpeed)
                if keyPressed and (key == 'w' or key == 'W' or key == UP):
                    SMuserY -= SMspeed
                if keyPressed and (key == 's' or key == 'S' or key == DOWN):
                    SMuserY += SMspeed

                if SMuserY <= 100:
                    SMuserY = 100
                if SMuserY > height - 150:
                    SMuserY = height - 150

                line(100, SMuserY, 100, SMuserY + 50)  # USER

                def enemy(x, y, s, n): #This function creates enemies 
                    global SMenemyY1, SMenemyY2, SMenemyS1, SMenemyS2
                    y += s
                    if y <= 100 or y >= height - 150:
                        s *= -1
                    line(x, y, x, y + 50)
                    if n == 1:
                        SMenemyY1, SMenemyS1 = x, s
                    if n == 2:
                        SMenemyY2, SMenemyS2 = x, s

                SMenemyY1, SMenemyY2 = SMenemyY1 + \
                    SMenemyS1, SMenemyY2 + SMenemyS2
                #The processes BELOW is error detection for the enemies
                if SMenemyY1 <= 100 or SMenemyY1 >= height - 150:
                    SMenemyS1 *= -1
                if SMenemyY2 <= 100 or SMenemyY2 >= height - 150:
                    SMenemyS2 *= -1
                #Display the enemies
                line(width - 200, SMenemyY1, width - 200, SMenemyY1 + 50)
                line(width - 100, SMenemyY2, width - 100, SMenemyY2 + 50)
                
                if SMscoreState == 1:
                    SMscore -= 15
                    ballX, ballY, xSpeed, ySpeed = width / 2, height / \
                        2, random.choice(
                            [xSpeed * -1, xSpeed * 1]), random.choice([ySpeed * -1, ySpeed * 1]) #Give ball random movements
                if SMscoreState == 2:#Check if goals were scored and points are needed 
                    SMscore += 25
                    ballX, ballY, xSpeed, ySpeed = width / 2, height / \
                        2, random.choice(
                            [xSpeed * -1, xSpeed * 1]), random.choice([ySpeed * -1, ySpeed * 1])
                SMscoreState = 0

                stroke("#2DAD32")
                rect(0, height - 60, width, 100)

                fill(0)
                textSize(20)
                text("Score: " + str(SMscore), width / 3 - 10, height - 20)
                # Separator of Score and Highest Score
                line(width / 3.2, height - 60, width / 3.2, height)
                if self.SPB == 'N/A' or (type(self.SPB) == int and self.SPB <= SMscore): #Udate personal best score
                    text("Highest Score: " + str(SMscore), 5, height - 20)

                else:
                    text("Highest Score: " + str(self.SPB), 5, height - 20) #Display Highest score

                text("Conceded Goals: ", width / 2, height - 20)

                counter = 0
                for x in range(SMlives):#Display varying numbers of balls depending if user's conceeded goals
                    if x >= 3:
                        counter += 1
                        image(loadImage("gameBall2.png"),
                              (width / 2 + 145) + 25 * (counter), height - 20)
                    else:
                        image(loadImage("gameBall2.png"),
                              (width / 2 + 145) + 25 * (x + 1), height - 50)

                # Separator of Score and Conceded goals
                line(width / 2.06 + 10, height - 60, width / 2.06 + 10, height)
                stroke(255)
                fill(255)

            else:
                #The processes below displays END SCREEN
                textAlign(CENTER)
                text("\t\tGame Over! \n\tPoints Scored: " + str(SMscore) +
                     "\nPress anything access menu", width / 2, height / 2) 
                textAlign(LEFT)
                if mousePressed:
                    self.SPB = SMscore
                    SMuserX, SMuserY, SMspeed, SMenemyY1, SMenemyY2, SMenemyS1, SMenemyS2 = 100, width / 3, 7, width / 3, width / \
                        3, random.choice([random.randint(5, 10), random.randint(-10, -5)]), random.choice(
                            [random.randint(7, 12), random.randint(-12, -7)])
                    SMscoreState, SMscore, SMlives, SMstate = 0, 0, 6, 0

    def KTU(self):#This function allows the user to play Keep Ball Up
        global menuOpen, KTUstate, state
        menuOpen = False
        print("State: ", KTUstate)
        if KTUstate == 0: #GAME INTRO PAGE
            background(255)
            stroke(0)
            fill('#620118')
            strokeWeight(10)
            rectMode(CORNER)  # BORDER
            rect(0, 0, width, height)

            rectMode(CENTER)  # RECT over the title
            strokeWeight(5)
            rect(width / 2, height / 14 + 60, 300, 60)

            fill(0)
            rectMode(CORNER)
            rect(0, 73, width / 2 - 150, height - 150)  # LEFT BLACK RECT
            # RIGHT BLACK RECT
            rect(width - (width / 2 - 150), 73, width / 2 - 150, height - 150)
            rect(0, 0, width, height / 7)
            rect(0, height - 75, width, 75)

            imageMode(CENTER)
            image(loadImage("ballDeco.png"), (width / 2 - 150) / 2, height / 2)
            image(loadImage("ballDeco.png"), width -
                  ((width / 2 - 150) / 2), height / 2)
            imageMode(CORNER)
            textAlign(CENTER)
            textSize(30)
            text("Keep It Up", width / 2, height / 12 + 70)

            textAlign(LEFT)
            rectMode(CORNER)
            noFill()

            # LEFT VERT LINE
            line(width / 2 - 150, height / 14 + 60,
                 width / 2 - 150, height - 75)
            # RIGHT VERT LINE
            line(width / 2 + 150, height / 14 + 60,
                 width / 2 + 150, height - 75)
            line(0, height - 75, width, height - 75)  # HORIZONTAL LINE DOWN
            line(0, 75, width, 75)  # HORIZONTAL LINE UP

            self.Buttons(
                width / 3, height / 3 + 10, 220, 50, loadImage("KTU_deco.png"), "PLAY", 255, 0) #Play button
            self.Buttons(
                width / 3, height / 3 + 70, 220, 50, loadImage("info.png"), "INFO", 255, 0)#Game info button
            self.Buttons(width / 3, height / 3 + 130, 220, 50,
                         loadImage("exitGame.png"), "EXIT", 255, 0)#Exit info button

        if KTUstate == 2:#Allows user to view Game infor
            JOptionPane.showMessageDialog(
                None, "System Mechanics\nBefore time runs out, you must get the required points.\nVariable amounts of Points are rewared after a box is destroyed.\nTime will added after each goal is met.\n------------------------------------------\nFeatures:\n\tAccurate Aiming System\n\tIncreasing # of balls as required points are met ", "Game Info", JOptionPane.PLAIN_MESSAGE)
            KTUstate = 0
        if KTUstate == 1:#Game can be Played
            background(0)
            stroke(255)
            strokeWeight(10)
            noFill()
            rect(0, 0, width, height)

            global FTU_Ballx, FTU_Bally, FTU_BallxS, FTU_BallyS, FTU_ballMove, FTU_balls, BallStorage, BrickStorage, FTU_Score, FTU_ScoreGoal, FTU_time, FTU_savedTime, FTU_closeGame
            fill(0)
            stroke(0)
            textSize(12)
            ellipseMode(CENTER)

            passTime = millis() / 1000 - FTU_savedTime #Timer

            if FTU_time - int(passTime) >= 0: #Check if counterdown is greater or equal to zero
                fill(255)
                text("Score: " + str(FTU_Score), 50, height - 50)
                text("Score Goal : " + str(FTU_ScoreGoal), 150, height - 50)

                if self.KBU == 'N/A' or (type(self.KBU) == int and self.KBU <= FTU_Score):#Update a Personal Best
                    self.KBU = FTU_Score
                text("Personal Best: " + str(self.KBU), 370, height - 50)#Display personal best

                text("Timer : " + str(FTU_time - int(passTime)), 250, height - 50)#Displays timer

                noCursor()#Remove cursor
                FTU_Ball(FTU_Ballx, FTU_Bally, FTU_BallxS, FTU_BallyS, FTU_ballMove) #Create Ball oject
                trail()#Create trail
                FTU_Bricks(BrickStorage, True)#Create bricks

                if FTU_time - int(passTime) >= 0 and FTU_Score >= FTU_ScoreGoal: #Check if user has reached goal score before the timer ran out
                    FTU_time, FTU_ScoreGoal, FTU_balls = FTU_time + \
                        10, FTU_ScoreGoal + 20, FTU_balls + 1

            else:
                #Display Game Over Screem
                cursor()
                fill(255)
                FTU_Score, FTU_ScoreGoal = 0, 50
                BallStorage, BrickStorage = [], []
                FTU_BallyS, FTU_BallxS = 0, 0
                FTU_ballMove, FTU_balls = False, 1

                textAlign(CENTER)
                textSize(20)
                text("GAME OVER!\nPress anything to access Menu",
                     width / 2, height / 2)
                if mousePressed:
                    KTUstate = 0

    def Memozories(self):#The function allows the user to play Memozories
        global Mstate, state, menuOpen, M_savedTime, M_timeCountDown, M_countState, M_XcountState, M_check, M_score, M_endGame
        menuOpen = False
        frameRate(30)
        if Mstate == 0:#GAME INTRO SCREEN
            background(0)
            fill('#E8C6C0')
            triangle(width / 2 - 200, height / 7, width / 2 + 200,
                     height / 7, width / 2, height - 90)
            textAlign(CENTER)

            rect(width / 2 - 200, 20, 400, 50)

            fill(255)
            text("MEMOZORIES", width / 2, height / 10 - 7)
            textAlign(LEFT)
            rectMode(CORNER)
            self.Buttons(width / 3 - 7, height / 6 + 10, 220, 50,
                         loadImage("colourSplash.png"), "PLAY", 0, 255)#PLAY BUTTON
            self.Buttons(width / 3 - 7, height / 6 + 70, 220, 50,
                         loadImage("info.png"), "INFO", 0, 255)#INFO BUTTON
            self.Buttons(width / 3 - 7, height / 6 + 130, 220, 50,
                         loadImage("exitGame.png"), "EXIT", 0, 255)#EXIT BUTTON
            image(loadImage('brainDeco.png'), width - 200, height - 325)
            image(loadImage('brainDeco.png'), 50, height - 325)#

        if Mstate == 1:#Game can be played
            background(0)

            def colourBox(x, y, c):#This function creates colour boxs for the game
                fill(c[0], c[1], c[2])
                rectMode(CENTER)
                if (mouseX >= x - 75 and mouseX <= x + 75) and (mouseY >= y - 75 and mouseY <= y + 75):
                    strokeWeight(4)
                    if mousePressed:
                        fill(c[0], c[1], c[2], 191)
                else:
                    strokeWeight(2)
                rect(x, y, 150, 150)

            if M_endGame == False: #If the game is still runing
                #Display Colour boxes
                colours = [[201, 41, 62], [7, 5, 160], [6, 147, 49],
                           [229, 223, 12], [141, 0, 142], [149, 149, 149]]
                colourBox(100, height / 3, colours[0])
                colourBox(300, height / 3, colours[1])
                colourBox(500, height / 3, colours[2])
                colourBox(100, height / 1.5, colours[3])
                colourBox(300, height / 1.5, colours[4])
                colourBox(500, height / 1.5, colours[5])

                if M_countState == True:
                    textSize(25)
                    passTime = millis() / 1000 - M_savedTime #Counter
                    # print(passTime)
                    fill(255)
                    textAlign(CENTER)
                    if M_timeCountDown - int(passTime) > 0 and M_timeCountDown - int(passTime) <= 5: #Display when new sequence is coming
                        text("New Sequence In.... " + str(M_timeCountDown -
                                                          int(passTime)) + " seconds", width / 2, height / 9)
                    elif M_XcountState == 1 and M_timeCountDown - int(passTime) == 0: #Check if timer is equal to 0
                        M_countState = False
                    elif M_timeCountDown - int(passTime) <= 0:
                        M_savedTime = millis() / 1000
                        M_XcountState = 1
                fill(255)
                textSize(13)
                text('Score : ' + str(M_score), 50, height - 50)
                if self.memozories == 'N/A' or ( type(self.memozories) == int and self.memozories <= M_score): #Update personal best
                    self.memozories = int(M_score)
                text("Personal Best: " + str(self.memozories), 200, height - 50)#Display personal best
                text('Level of Difficulty: ', 350, height - 50)
                
                for x in range(M_score + 1):#This process displays stars depending on the level
                    image(loadImage('star.png'), 405 + (17 * x), height - 63)

                if M_countState == False:#Display when next sequence will be shown
                    textAlign(CENTER)
                    fill(255)
                    textSize(25)
                    if M_check == False:
                        text("Displaying sequence..", width / 2, height / 9) 
                        M_check = M_sequence()
                    if M_check == True:
                        text("Replicate the displayed sequence", width / 2, height / 9)

            else:
                #Display GAME OVER screen
                textAlign(CENTER)
                textSize(20)
                text("GAME OVER!\nINCORRECT SEQUENCE!\nPoints Scored: " +
                     str(M_score) + "\nPress anything to access Menu", width / 2, height / 3)

        if Mstate == 2:#Displays game info 
            JOptionPane.showMessageDialog(
                None, "System Mechanics:\n\tReplicate the sequences displayed\n------------------------------------------\nFeatures:\n\t-Integrated Timing System", "Game Info", JOptionPane.PLAIN_MESSAGE)
            Mstate = 0

    def earnCoins(self): #This function allows the users to earn coins
        global state
        userSel = JOptionPane.showOptionDialog(None, "Welcome to the Earnings Section\n------------------------------------------\nSelect a way you wish earn coins.",
                                               "Earning Coins", JOptionPane.DEFAULT_OPTION, JOptionPane.INFORMATION_MESSAGE, None, ['Exit', 'Survey', 'Math Problems'], 'Math Problems')
        if userSel == 0 or userSel == -1: #If user chooses to exit, allow user to leave
            state = 3
        if userSel == 1:#User chooses a survey
            surveyT = random.choice(
                ["McDonalds", "Wendys", 'Pizza Hut', 'Burger King', 'Dominos'])
            JOptionPane.showMessageDialog(
                None, 'Survey: ' + surveyT + '\n---------------------------------------\nPlease finish survey to earn $25', "Earning Coins", JOptionPane.PLAIN_MESSAGE)

            surveyQ = ['Enter your First & Last Name: ']
            questions = [['When you want to have a meal in a fast food restaurant, do we come to your mind as the first choice?', ['Yes', 'No']], ['Which fast food restaurant do you visit most frequently? ', ['McDonald’s', 'Wendy’s', 'A&W', 'Pizza Hut', 'KFC', 'Burger King', 'Dominos']],
                         ['What time of the day do you prefer to eat at ?', ['Morning', 'Afternoon', 'Evening', 'Midnight']], [
                             'Does our advertising influence you? ', ['Yes', 'No']], ['Give us a rating in customer service: ', ['1', '2', '3', '4', '5']],
                         ['Rate the cleanliness of our restaurant: ', ['1', '2', '3', '4', '5']], ['Rate the taste of our food: ', ['1', '2', '3', '4', '5']]]

            for numbQ in range(6): #Append random questions to the survey
                randQ = random.choice(questions)
                if randQ not in surveyQ:
                    surveyQ.append(randQ)

            JOptionPane.showInputDialog("Please enter your full name:")#Prompt user for name
            for questions in range(1, len(surveyQ) - 1):#Display Survey Questions
                x = JOptionPane.showInputDialog(None, surveyQ[questions][
                                                0], surveyT + ' Survey', JOptionPane.QUESTION_MESSAGE, None, surveyQ[questions][1], surveyQ[questions][1][0])
            #Display the survey as completed
            JOptionPane.showMessageDialog(
                None, 'Survey: ' + surveyT + '\n-----------------COMPLETED----------------------\nAn earnings of $20 will be transfered to your account', "Earning Coins", JOptionPane.PLAIN_MESSAGE)
            self.balance = str(float(self.balance) + 20)
        if userSel == 2:#User chooses math problems
            JOptionPane.showMessageDialog(
                None, 'Math Problems\n---------------------------------\nAll answers to questions must be correct to earn coins\nTotal Possible Earnings: $10', "Earning Coins", JOptionPane.PLAIN_MESSAGE)
            #Random questions stored
            questions = [[random.randint(0, 50), random.randint(0, 50), random.choice(['sum', 'difference'])], [
                random.randint(0, 20), random.randint(1, 15), random.choice(['product', 'quotient'])]]
            #Display the random question to the user
            answer = JOptionPane.showInputDialog("Problem: Enter the " + str(questions[0][2]) + " of " + str(questions[0][0]) + " and " + str(questions[0][1]) + "\n------------------------------------------\nEnter your answer below:")
            correct = True
            if questions[0][2] == 'sum':#Check if problem is an addition
                if str(questions[0][0] + questions[0][1]) != answer:correct = False #Check if user is correct
            if questions[0][2] == 'difference':#Check if problem is a subraction
                if str(questions[0][0] - questions[0][1]) != answer:correct = False #Check if user is correct

            if correct == True:#Check if user is correct
                answer = JOptionPane.showInputDialog("Problem: Enter the " + str(questions[1][2]) + " of " + str(questions[1][
                                                     0]) + " and " + str(questions[1][1]) + "\n------------------------------------------\nEnter your answer below:")
                
                if questions[1][2] == 'product':#Check if problem is about product
                    if str(questions[1][0] * questions[1][1]) != answer: correct = False
                if questions[1][2] == 'quotient':#Check if problem is  about division
                    if str(questions[1][0] / questions[1][1]) != answer: correct = False
                    try:
                        if  float(questions[1][0]/(questions[1][1])) == float(answer):
                            correct = True
                    except:
                        pass
            if correct == True:#Check if answers are correct
                #Display COMPLETED-CORRECTLY
                JOptionPane.showMessageDialog(
                    None, 'Math Problems\n-----------------COMPLETED-CORRECTLY---------------------\nAn earnings of $10 will be transfered to your account!', "Earning Coins", JOptionPane.PLAIN_MESSAGE)
                self.balance = str(float(self.balance) + 10)
            else:#COMPLETED-INCORRECTLY
                JOptionPane.showMessageDialog(
                    None, 'Math Problems\n-----------------COMPLETED-INCORRECTLY---------------------\nUnfortunately, no coins will be provided for you.', "Earning Coins", JOptionPane.PLAIN_MESSAGE)
        state = 3

    def exit(self):#This function allows the user to exit his/her account and saves the user updated info
        global state, nameString, passString, track, counter, menuGo, user, loginStatus, menuOpen, menuCheck, inputState, inputDot, SMstate
        saveStorage=[]
        
        with open('Overflow.csv', 'r') as csvFile:  # Opens csv file
            readCsvFile = csv.DictReader(csvFile)
            for user in readCsvFile:#Obtain a list of the csv info
                if (self.username == user['Username']) and (self.password == user['Password']): 
                    saveStorage.append([self.username,self.password,self.balance, self.gamesOwned, self.SPB, self.KBU, self.memozories])
                else:saveStorage.append([user['Username'],user['Password'],user['Account Balance'],user['Games Owned'],user['Soccer Mania'],user['Keep It Up'],user['Memozories Score']])
       
        with open('Overflow.csv', 'w') as csvFile:  # Opens csv file
            writer = csv.DictWriter(csvFile, fieldnames=['Username', 'Password', 'Account Balance', 'Games Owned', 'Soccer Mania', 'Keep It Up', 'Memozories Score'])
            writer.writeheader()
            for index in range(len(saveStorage)): #Rewrites csv file with the saveStorage list
                writer.writerow({'Username': saveStorage[index][0], 'Password': saveStorage[index][1], 'Account Balance': saveStorage[index][2],
                            'Games Owned': saveStorage[index][3], 'Soccer Mania': saveStorage[index][4], 'Keep It Up': saveStorage[index][5], 'Memozories Score': saveStorage[index][6]})

        state, nameString, passString, track, counter, menuGo, user, loginStatus, menuOpen, menuCheck, inputState, inputDot = 0, "", "", 1, 0, 0, '', True, False, 1, 0, 0
        
        
        
    def trans(self):#This function  displays transanctions of the user
        global state
        gameCost,moneySpent = [['Soccer Mania', 29.99], ['Keep It Up', 24.99], ['Memozories', 19.99]],0
        for x in range(len(gameCost)): #This process is to obtain an Ingame Total Spending
            if gameCost[x][0] in self.gamesOwned:
                moneySpent+=gameCost[x][1]        
        JOptionPane.showMessageDialog(
                None, 'Welecome to the transanctions section\n---------------------------------\n\tGames bought: '+self.gamesOwned+'\n\tIngame Total Spending: '+str(moneySpent) , "Transanctions", JOptionPane.PLAIN_MESSAGE)
        state = 3

    def menu(self): #This function displays the 
        global menuOpen, menuCheck
        menuOpen = True # MenuOpen controls all buttons of the user's main menu page
        # menu Check is for games and finance
        background("#414143")
        fill(0)
        stroke(255)
        strokeWeight(3)
        textSize(20)
        rect(0, 0, width, height / 7)
        line(0, height / 14, width, height / 14)

        rect(0, height / 7, width / 5, height)

        fill(255)
        text("|-SYSTEM OVERFLOW-|", width / 3, height / 20)

        image(loadImage("account.png"), width - 150, height / 12)
        text(self.username.title(), width - 105, height / 8.5)
        line(450, height / 14, 450, height / 7)  # Seperator

        if (mouseX >= 0 and mouseX < (width / 5))and (mouseY > (height / 7) and mouseY < (height / 2.7)): #Checks if user hovers over the play button
            fill('#64AF5A')
        else:
            fill(255)

        # PLAY GAMES BUTTON #Dimensions: width/5 by (height/2.7)-(height/7)
        image(loadImage("play.png"), 10, height / 6)
        textSize(15)
        textAlign(CENTER)
        text("GAMES", width/10, height / 2.8)
        line(0, height / 2.7, width / 5, height / 2.7)
        textAlign(CORNER)
        fill(255)
        if (mouseX >= 0 and mouseX < (width / 5))and (mouseY > (height / 2.7) and mouseY < (height / 1.85)):fill('#64AF5A')#Checks if user hovers over the Finance button

        # Finance Button Dimensions: width/5 by (height/1.85) - (height/7)
        image(loadImage("cash.png"), 10, height / 2.7)
        text("FINANCE", 20, height / 1.9)
        line(0, height / 1.85, width / 5, height / 1.85)
        
        #Exit Button
        fill(0)
        rect(0,height/1.85,width/5,100)
        imageMode(CENTER)
        image(loadImage("exitMenu.png"),width/10,height/1.85+50)
        imageMode(CORNER)
        fill(255)
        if (mouseX >= 0 and mouseX < (width / 5))and (mouseY > (height / 1.85) and mouseY < (height / 1.85)+100):fill('#64AF5A') #Checks if user hovers over the exit button
        textAlign(CENTER)
        textSize(17)
        text("EXIT",width/10,height/1.85+90)
        textSize(15)
        textAlign(CORNER)
        

        #Cash Balance Display
        line(width / 5, height / 14, width / 5, height / 7)
        image(loadImage("cashSymbol.png"), 10, height / 13)
        fill('#64AF5A')
        textSize(20)
        text(str(format(float(self.balance), '.2f')), 50, height / 8.5)

        if menuCheck == 1:
            self.buttonCreate(
                width / 4.3, height / 4, 200, 150, loadImage("soccer.png"), "Soccer Mania") #Soccer Mania Button
            self.buttonCreate(
                width / 1.6, height / 4, 200, 150, loadImage("ball.png"), "Keep It Up")#Keep It Up Button
            self.buttonCreate(
                width / 4.3, height / 4 + 200, 200, 150, loadImage("Mcolours.png"), "Memozories")#Memozories Button
            self.buttonCreate(
                width / 1.6, height / 4 + 200, 200, 150, loadImage("comingSoon.png"), "Mitzer")#Mitzer Button
        if menuCheck == 2:
            def fButtons(x, y, w, h, img, str, colour1, colour2):#This function creates buttons
                fill(0, 0, 0)
                strokeWeight(2)
                rect(x, y, w, h)
                imageMode(CENTER)
                image(img, x + w / 2, y + h / 2)
                rectMode(CENTER)
                rect(x + w / 2, y + h, 150, 50)
                if (mouseX >= x and mouseX <= x + w) and (mouseY >= y and mouseY <= y + h):#Checks if user hovers over the  button
                    fill(colour1)
                else:
                    fill(colour2)
                textAlign(CENTER)
                text(str, x + w / 2, y + h)
                textAlign(CORNER)
                imageMode(CORNER)
                rectMode(CORNER)

            fButtons(width / 4, height / 3, 200, 300,loadImage("cashBag.png"), "Earn Coins", '#64AF5A', 255)#Display the Button : Earn Coins
            fButtons(width / 4 + 250, height / 3, 200, 300,loadImage("trans.png"), "Transactions", '#64AF5A', 255)#Display the Button : Earn Coins

#|-----------------------------------------------------------------------------------------------------------------------|
#|-----------------------------------------------------------------------------------------------------------------------|
#This Section of Code is for the intro page, the login page,, and the signup page
#|-----------------------------------------------------------------------------------------------------------------------|

def intro(): #This function displays a button:  to login and signup
    global loginX, loginY, loginW, loginH, createX, createY, createW, createH
    fill(255)
    textSize(40)
    Image = loadImage("Image.png")
    background(Image)
    text("System Overflow", width / 4.5, height / 5.5)

    # Button for Login Existing Account
    noFill()
    stroke(255)
    strokeWeight(5)
    loginX, loginY, loginW, loginH = width / 4, height / 2.5, 300, 50
    rect(loginX, loginY, loginW, loginH)
    textSize(20)
    text("Login Existing Account", loginX + loginW / 7, loginY + loginH / 1.5)

    # Button for New Account Creation
    createX, createY, createW, createH = width / 4, height / 1.5, 300, 50
    rect(createX, createY, createW, createH)
    textSize(20)
    text("Create New Account", createX + createW / 7, createY + createH / 1.5)

def login(String):#This function allows the user to login or Sign-up
    global nameString, passString, menuGo, state, track, counter, user, loginStatus, inputState, inputDot
    fill(255)

    #Displays varying images depending if user chooses to login or Sign-up
    if String == "Login":Image = loadImage("blue.png")
    elif String == "Sign-up":Image = loadImage("Sign-Up.png")
    background(Image)
    textSize(40)
    text("System Overflow", width / 4.5, height / 5.5)

    textSize(25)
    strokeWeight(2)
    text(String, width / 2.25, height / 3.5)
    line((width / 2.25) - 20, (height / 3.5) + 5,
         (width / 2.25) + 95, (height / 3.5) + 5)

    # Username Inputs
    fill(0)  # Black Username Box
    loginX, loginY, loginW, loginH = width / 4, height / 3, 120, 25
    rect(loginX, loginY, loginW, loginH)

    textSize(17)
    fill(255)
    text("**PRESS ENTER AFTER EACH ENTRY**", width - 340, height / 18)

    inputDot = random.choice([0, 1]) #Circular Dot
    if inputDot == 1:
        stroke(0)
        fill(255)
    if inputDot == 0:
        stroke(255)
        fill(0)

    ellipseMode(CORNER)

    if inputState == 0: #Circular Dot on username
        ellipse(loginX + loginW + (2 * loginW) + 5, loginY + 5, 15, 15)
    else:#Circular Dot on Password
        ellipse(loginX + loginW + (2 * loginW) + 5, loginY + 55, 15, 15)

    fill(255)  # Username Clear Box
    stroke(255)
    textSize(20)
    text("Username: ", loginX + loginW / 15, loginY + loginH / 1.2)
    noFill()
    rect(loginX + (loginW), loginY, 2 * loginW, loginH)

    fill(255)  # USERNAME ENTRY
    textSize(20)
    text(str(nameString), (loginX + (loginW)) +
         loginW / 15, loginY + loginH / 1.2)

    fill(0)  # PASSWORD BLACK Box
    rect(loginX, loginY + 50, loginW, loginH)

    fill(255)  # PASSWORD Clear Box
    textSize(20)
    text("Password: ", loginX + loginW / 15, loginY + (loginH + 45))

    noFill()  # PASSWORD ENTRY
    rect(loginX + (loginW), loginY + 50, 2 * loginW, loginH)
    fill(255)
    textSize(20)
    text(str(passString), (loginX + (loginW)) +
         loginW / 15, loginY + loginH + 50)

    if menuGo == 1:

        # Here I will check if pass and username are in csv file with the class atribute 
        if String == "Sign-up":
            user = Account(nameString, passString, 'Create')
        else:
            user = Account(nameString, passString, 'Login')
        if loginStatus == False:
            #Display INVALID entry
            textSize(20)
            fill(0)
            strokeWeight(5)
            rect(width / 5 - 10, height / 2, 430, 100)
            fill(255)
            if String == "Sign-up": 
                text("Message: Username's taken", width / 3.3, height / 1.8)
            else:
                text("Message: Invalid Entry", width / 2.8, height / 1.8)
            text("Press anywhere to return to Menu", width / 4, height / 1.6)
            track = 0
        else:
            nameString, passString, track, counter, menuGo, state, inputState, inputDot = "", "", 1, 0, 0, 3, 0, 0


#|-----------------------------------------------------------------------------------------------------------------------|
#|-----------------------------------------------------------------------------------------------------------------------|
#This Section of Code is for the setup(),draw(),mousePress(),keyPressed()
#|-----------------------------------------------------------------------------------------------------------------------|
# MAIN
import os
import os.path
import csv
import time
import random
from javax.swing import JOptionPane
state, nameString, passString, track, counter, menuGo, user, loginStatus, menuOpen, menuCheck, inputState, inputDot, SMstate = 0, "", "", 1, 0, 0, '', True, False, 1, 0, 0, - \
    1


def setup():
    size(622, 619)
    #Global Variables for SM Ball Coordinates
    global ballX, ballY, xSpeed, ySpeed, SMuserY, SMspeed, SMuserX, SMenemyY1, SMenemyS1, SMenemyY2, SMenemyS2, SMscoreState, SMscore, SMlives
    ballX, ballY, xSpeed, ySpeed = width / 2, height / 2, random.choice([random.randint(
        3, 10), random.randint(-10, -3)]), random.choice([random.randint(3, 10), random.randint(-10, -3)])
    SMuserX, SMuserY, SMspeed, SMenemyY1, SMenemyY2, SMenemyS1, SMenemyS2 = 100, width / 3, 7, width / 3, width / \
        3, random.choice([random.randint(5, 10), random.randint(-10, -5)]
                         ), random.choice([random.randint(7, 12), random.randint(-12, -7)])
    SMscoreState, SMscore, SMlives = 0, 0, 6

    # Global Variables for KTU Game Values
    global KTUstate, FTU_Ballx, FTU_Bally, FTU_BallxS, FTU_BallyS, FTU_ballMove, FTU_balls, BallStorage, BrickStorage
    FTU_Ballx, FTU_Bally, BallStorage, BrickStorage = random.randint(
        40, width - 40), height - 75, [], []
    FTU_BallyS, FTU_BallxS = 0, 0
    FTU_ballMove, FTU_balls, KTUstate = False, 1, -1

    global FTU_savedEntries, savedX, savedY, FTU_Score, FTU_ScoreGoal, FTU_time, FTU_savedTime, FTU_closeGame
    FTU_Score, FTU_ScoreGoal, FTU_time, FTU_savedTime = 0, 50, 70, 0
    FTU_closeGame = False

    # Global Variables for Memozories Game values
    global Mstate, M_savedTime, M_timeCountDown, M_passedTime, M_sequenceStorage, M_numbSeq, M_countState, M_XcountState, M_sequenceTime, M_check, M_score, M_counter, M_endGame
    Mstate, M_savedTime, M_timeCountDown, M_passedTime, M_sequenceStorage, M_numbSeq, M_countState = - \
        1, 0, 7, 0, [], 2, True
    M_XcountState, M_sequenceTime, M_check, M_counter, M_score, M_endGame = 0, 0, False, 0, 0, False


def draw():
    global state, user, SMstate
    #Run function depending on state.
    if state == 0:intro()
    if state == 1:login("Login")
    if state == 2:login("Sign-up")
    if state == 3:user.menu()
    if state == 4:user.SM()
    if state == 5:user.KTU()
    if state == 6:user.Memozories()
    if state == 7:user.earnCoins()
    if state == 8:user.trans()
    if state==9:user.exit()

def mousePressed():
    global state, menuGo, nameString, passString, track, counter, menuGo, state, loginStatus, menuOpen, menuCheck, user, inputState, inputDot, SMstate, KTUstate, FTU_savedTime
    global Mstate, M_savedTime, M_timeCountDown, M_passedTime, M_sequenceStorage, M_numbSeq, M_countState, M_XcountState, M_sequenceTime, M_check, M_score, M_counter, M_endGame
    changeXState, changeYState = '', ''
    if state == 0:
        if (mouseX >= loginX and mouseX <= loginX + loginW) and (mouseY >= loginY and mouseY <= loginY + loginH): #Check if user is hovering over login input
            changeXState = True
        if (mouseX >= createX and mouseX <= createX + createW) and (mouseY >= createY and mouseY <= createY + createH):#Check if user is hovering over signup input
            changeYState = True
    if changeXState == True:
        state = 1
    if changeYState == True:
        state = 2
    changeXState == False
    changeYState == False

    if loginStatus == False:
        state, nameString, passString, track, counter, menuGo, loginStatus, inputState, inputDot = 0, "", "", 1, 0, 0, True, 0, 0

    if SMstate == 0:#Soccer Mania has been selected to play
        if (mouseX >= width / 3 and mouseX <= width / 3 + 220) and (mouseY >= height / 3 + 10 and mouseY <= height / 3 + 10 + 50): #Play Game
            SMstate = 1
        if (mouseX >= width / 3 and mouseX <= width / 3 + 220) and (mouseY >= height / 3 + 70 and mouseY <= height / 3 + 70 + 50):#Display Info of the game
            SMstate = 3
        if (mouseX >= width / 3 and mouseX <= width / 3 + 220) and (mouseY >= height / 3 + 130 and mouseY <= height / 3 + 180):#Exit game
            SMstate = 2

    if menuOpen == True:
        # PLAY BUTTON #Dimensions: width/5 by (height/2.7)-(height/7)
        if (mouseX >= 0 and mouseX < (width / 5))and (mouseY > (height / 7) and mouseY < (height / 2.7)):
            menuCheck = 1

        # Finance Button Dimensions: width/5 by (height/1.85) - (height/2.7)
        if (mouseX >= 0 and mouseX < (width / 5))and (mouseY > (height / 2.7) and mouseY < (height / 1.85)):
            menuCheck = 2
            
        #EXIT BUTTON
        if (mouseX >= 0 and mouseX < (width / 5))and (mouseY > (height / 1.85) and mouseY < (height / 1.85)+100):
            state=9
        if menuCheck == 1:
            if (mouseX >= width / 4.3 and mouseX <= width / 4.3 + 200) and (mouseY >= height / 4 and mouseY <= height / 4 + 150):
                check = user.buttonCreate(
                    width / 4.3, height / 4, 200, 150, loadImage("soccer.png"), "Soccer Mania")
                if check == True:
                    SMstate, state = 0, 4  # Run Soccer Mania Game
                if check == False:
                    user.payment("Soccer Mania")

            if (mouseX >= width / 1.6 and mouseX <= width / 1.6 + 200) and (mouseY >= height / 4 and mouseY <= height / 4 + 150):
                check = user.buttonCreate(
                    width / 1.6, height / 4, 200, 150, loadImage("ball.png"), "Keep It Up")
                if check == True:
                    state, KTUstate = 5, 0
                if check == False:
                    user.payment("Keep It Up")
            if (mouseX >= width / 4.3 and mouseX <= width / 4.3 + 200) and (mouseY >= height / 4 + 200 and mouseY <= height / 4 + 200 + 150):
                check = user.buttonCreate(
                    width / 4.3, height / 4 + 200, 200, 150, loadImage("Mcolours.png"), "Memozories")
                if check == True:
                    state, Mstate = 6, 0
                if check == False:
                    user.payment("Memozories")
        if menuCheck == 2:#Opens the financial section
            if (mouseX >= width / 4 and mouseX <= width / 4 + 200) and (mouseY >= height / 4 and mouseY <= height / 4 + 300): #RUN EARNING COINS PROGRAM
                state = 7
            if (mouseX >= width / 4 + 250 and mouseX <= width / 4 + 250 + 200) and (mouseY >= height / 4 and mouseY <= height / 4 + 300):#RUN TRANSACTIONS PROGRAM
                state = 8

    if KTUstate == 0:
        # Play Keep it Up
        if mousePressed and (mouseX >= width / 3 and mouseX <= width / 3 + 220) and (mouseY >= height / 3 + 10 and mouseY <= height / 3 + 60):
            KTUstate, FTU_savedTime = 1, millis() / 1000
        # Info
        if mousePressed and (mouseX >= width / 3 and mouseX <= width / 3 + 220) and (mouseY >= height / 3 + 70 and mouseY <= height / 3 + 120):
            KTUstate = 2
        # EXIT
        if mousePressed and (mouseX >= width / 3 and mouseX <= width / 3 + 220) and (mouseY >= height / 3 + 130 and mouseY <= height / 3 + 180):
            KTUstate, menuOpen, state = -1, True, 3

    if Mstate == 0:
        # Play Memozories
        if mousePressed and (mouseX >= width / 3 and mouseX <= width / 3 + 220) and (mouseY >= height / 6 + 10 and mouseY <= height / 6 + 60):
            Mstate = 1
        # Info
        if mousePressed and (mouseX >= width / 3 and mouseX <= width / 3 + 220) and (mouseY >= height / 6 + 70 and mouseY <= height / 6 + 120):
            Mstate = 2
        # EXIT
        if mousePressed and (mouseX >= width / 3 and mouseX <= width / 3 + 220) and (mouseY >= height / 6 + 130 and mouseY <= height / 6 + 180):
            Mstate, menuOpen, state = -1, True, 3

    if M_endGame == True: #Check is memozories game is over
        Mstate, M_savedTime, M_timeCountDown, M_passedTime, M_sequenceStorage, M_numbSeq, M_countState = 0, 0, 7, 0, [
        ], 2, True
        M_XcountState, M_sequenceTime, M_check, M_counter, M_score, M_endGame = 0, 0, False, 0, 0, False
    if M_check == True:
        M_sequenceCheck()


def keyPressed():
    global state, track, nameString, passString, counter, menuGo, inputState, SMstate

    if track == 1:#Allows user to enter in the username box
        if key == RETURN or key == ENTER:
            inputState, track = 2, 2
        elif key == BACKSPACE or key == DELETE:
            nameString = nameString[:-1]
        elif key == ' ':
            nameString += ' '
        else:
            try:
                nameString += key
            except:
                pass

    if track == 2:#Allows user to enter in the Password box
        if key == RETURN or key == ENTER:
            if counter == 0:
                pass
            else:
                menuGo = 1
            counter = 1
        elif key == BACKSPACE or key == DELETE:
            passString = passString[:-1]
        elif key == ' ':
            passString += ' '
        else:
            try:
                passString += key
            except:
                pass
