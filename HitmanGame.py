import pygame, simpleGE, random, time

# to start of this is VERY unoptimized as i couldnt figure out how to clone a sprite to use for a card twice at a time

# better instructions, if you dont have angel card and draw hitman you lose
# for seeingeye card my intention was to make 3 cards and have their images change to the image of the 3 cards but i did not have time to do that so its prints for now
# same for an ending screen, instead it prints the result and goes to instructions scene

class Instructions(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        size = (640, 480)
        
        self.screen = pygame.display.set_mode(size)
        self.background = pygame.Surface(self.screen.get_size())
        
        bgColor = (17,17,17)
        self.background.fill(bgColor)
        
        self.response = "Quit"
        
        self.instrlbl = simpleGE.MultiLabel()
        self.instrlbl.textLines = [
            "Card game",
            "Dont draw the hitman card",
            "Play an angel card to",
            "survive hitman card"
        ]
        
        self.instrlbl.center = (320,200)
        self.instrlbl.size = (400,250)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.center = (140,360)
        self.btnPlay.text = "Play"
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.center = (520,360)
        self.btnQuit.text = "Quit"
        
        
        self.sprites = [self.instrlbl,
                        self.btnPlay,
                        self.btnQuit,
                        ]
                
    def process(self):
        if self.btnPlay.clicked:
            self.reponse = "Settings"
            settings = Settings()
            settings.start()
            self.stop()
        
        if self.btnQuit.clicked:
            self.reponse = "Quit"
            self.stop()


class Settings(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        bgColor = (17,17,17)
        self.background.fill(bgColor)
        
        self.cardsliderInfo = simpleGE.Label()
        self.cardsliderInfo.text = "Cards in the deck"
        self.cardsliderInfo.center = (120,40)
        self.cardsliderInfo.size = (200,40)
        self.cardsliderInfo.bgColor = (bgColor)
        
        self.cardSlider = simpleGE.Scroller()
        self.cardSlider.value = 30
        self.cardSlider.minValue = 20
        self.cardSlider.maxValue = 40
        self.cardSlider.center = (120,80)
        self.cardSlider.size = (140,40)
        
        self.hitmanSliderInfo = simpleGE.Label()
        self.hitmanSliderInfo.text = "Hitmans in deck"
        self.hitmanSliderInfo.center = (120,160)
        self.hitmanSliderInfo.size = (200,40)
        self.hitmanSliderInfo.bgColor = (bgColor)
        
        self.hitmanSlider = simpleGE.Scroller()
        self.hitmanSlider.value = 2
        self.hitmanSlider.minValue = 2
        self.hitmanSlider.maxValue = 4
        self.hitmanSlider.center = (120,200)
        self.hitmanSlider.size = (140,40)
        
        self.angelInDeckInfo = simpleGE.Label()
        self.angelInDeckInfo.text = "Start with angel in hand"
        self.angelInDeckInfo.center = (120,280)
        self.angelInDeckInfo.size = (250,40)
        self.angelInDeckInfo.bgColor = (bgColor)
        
        self.angelInDeck = simpleGE.Button()
        self.angelInDeck.text = "Yes"
        self.angelInDeck.center = (120, 320)
        self.angelInDeck.size = (200,40)
        self.angel = True
        self.redcolor = (255,0,0)
        self.greencolor = (0,255,0)
        self.angelInDeck.bgColor = (self.greencolor)
        
        self.playBtn = simpleGE.Button()
        self.playBtn.center = (480,240)
        self.playBtn.size = (200,150)
        self.playBtn.bgColor = (self.redcolor)
        self.playBtn.text = "Play"
        

        self.sprites = [self.cardSlider,
                        self.cardsliderInfo,
                        self.hitmanSliderInfo,
                        self.hitmanSlider,
                        self.angelInDeck,
                        self.angelInDeckInfo,
                        self.playBtn]
        self.cardsInDeck = self.cardSlider.value
        
    def process(self):
        if self.angelInDeck.clicked:
            if self.angel == True:
                self.angelInDeck.bgColor = (self.redcolor)
                self.angel = False
                self.angelInDeck.text = "No"
            else:
                self.angel = True
                self.angelInDeck.bgColor = (self.greencolor)
                self.angelInDeck.text = "Yes"
        if self.playBtn.clicked:
            cards = self.cardSlider.value
            hitman = self.hitmanSlider.value
            angel = self.angel
            
            
            game = Game(cards, hitman, angel)
            game.start()
            self.stop()
    

class CPU(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)

        
        original_image = pygame.image.load("hitman.png").convert_alpha()
        scaled_image = pygame.transform.smoothscale(original_image, (360, 200))  
        
        self.scaled_image_path = "hitman_scaled.png"
        pygame.image.save(scaled_image, self.scaled_image_path)
        self.setImage(self.scaled_image_path)
        self.setSize(360, 200) 
        self.x = 340
        self.y = 175


class angelCard1(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("angelCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
class angelCard2(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("angelCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000

class angelCard3(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("angelCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000

class angelCard4(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("angelCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
class angelCard5(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("angelCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
        
class hitmanCard(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("hitmancard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
        
class arsonCard1(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("arsonCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
class arsonCard2(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("arsonCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000

class arsonCard3(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("arsonCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
class arsonCard4(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("arsonCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000

class arsonCard5(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("arsonCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
        
class bottomlayerCard1(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("bottomlayerCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
class bottomlayerCard2(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("bottomlayerCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000

class bottomlayerCard3(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("bottomlayerCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
class bottomlayerCard4(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("bottomlayerCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000

class bottomlayerCard5(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("bottomlayerCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
class mineCard1(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("mineCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
class mineCard2(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("mineCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000

class mineCard3(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("mineCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
class mineCard4(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("mineCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
    
class mineCard5(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("mineCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
        
class shuffleCard1(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.visible = False
        self.setImage("shuffleCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
class shuffleCard2(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.visible = False
        self.setImage("shuffleCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000

class shuffleCard3(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.visible = False
        self.setImage("shuffleCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
class shuffleCard4(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.visible = False
        self.setImage("shuffleCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000

class shuffleCard5(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.visible = False
        self.setImage("shuffleCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
        
        
class seeingeyeCard1(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("seeingeyeCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
    
class seeingeyeCard2(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("seeingeyeCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000

class seeingeyeCard3(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("seeingeyeCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
class seeingeyeCard4(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("seeingeyeCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000

class seeingeyeCard5(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("seeingeyeCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
        
class copycatCard1(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("copycatCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
class copycatCard2(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("copycatCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
    
class copycatCard3(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("copycatCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
    
class copycatCard4(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("copycatCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000

    
class copycatCard5(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("copycatCard.png")
        self.setSize(125,125)
        self.x = -1000
        self.y = -1000
        
# 5 cases for each card
        

class deck(simpleGE.Sprite):
    # when i was first making this i didnt realize you could set a clicked boolean for sprites, thats why theres a green square for the actual deck as a button
    def __init__(self, scene):
        super().__init__(scene)
        original_image = pygame.image.load("deckofcards.png").convert_alpha()
        scaled_image = pygame.transform.smoothscale(original_image, (55, 55))  
        self.scaled_image_path = "deckofcards_scaled.png"
        pygame.image.save(scaled_image, self.scaled_image_path)
        self.setImage(self.scaled_image_path)
        self.setSize(55, 55)
        self.x = 185
        self.y = 245
        self.imageAngle = 35


class table(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        original_image = pygame.image.load("pokertable.png").convert_alpha()
        scaled_image = pygame.transform.smoothscale(original_image, (580, 480)) 
        self.scaled_image_path = "pokertable_scaled.png"
        pygame.image.save(scaled_image, self.scaled_image_path)
        self.setImage(self.scaled_image_path)
        self.setSize(580, 480)
        self.x = 315
        self.y = 300



class Game(simpleGE.Scene):
    def __init__(self, cards, hitman, angel):
        super().__init__()
        self.cards = cards
        self.deckList = []
        self.listOfCards = ["angel", "arson", "bottomlayer", "mine", "shuffle", "seeingeye", "copycat"]
        self.finalList = ["arson", "bottomlayer", "mine", "shuffle", "seeingeye", "copycat"]
        self.hitmanInDeck = hitman
        self.angelInDeck = angel
        self.PlayerList = []
        self.CPUlist = []
        self.whatdidcpudo = ""
        self.Turn = True
        self.initialcheck = True
        self.initialcheckNPC = True
        self.adjustedCards = self.cards - self.hitmanInDeck
        for i in range(self.hitmanInDeck):
            self.deckList.append("hitman")
        if self.angelInDeck:
            self.PlayerList.append("angel")
            self.CPUlist.append("angel")
        while self.initialcheck:
            self.choice = random.choice(self.listOfCards)
            self.PlayerList.append(self.choice)
            if len(self.PlayerList) == 6:
                self.initialcheck = False
                
            
        while len(self.CPUlist) < 6:
            self.choice = random.choice(self.listOfCards)
            self.CPUlist.append(self.choice)
            
        for i in range(self.adjustedCards):
            self.choice = random.choice(self.listOfCards)
            self.deckList.append(self.choice)
            random.shuffle(self.deckList)
        self.CPUlistLen = len(self.CPUlist)
        for item in self.deckList:
            print(item)   
        
        
        
        self.angelCard1 = angelCard1(self)
        self.angelCard2 = angelCard2(self)
        self.angelCard3 = angelCard3(self)
        self.angelCard4 = angelCard4(self)
        self.angelCard5 = angelCard5(self)

        self.hitmanCard = hitmanCard(self)

        self.arsonCard1 = arsonCard1(self)
        self.arsonCard2 = arsonCard2(self)
        self.arsonCard3 = arsonCard3(self)
        self.arsonCard4 = arsonCard4(self)
        self.arsonCard5 = arsonCard5(self)

        self.bottomlayerCard1 = bottomlayerCard1(self)
        self.bottomlayerCard2 = bottomlayerCard2(self)
        self.bottomlayerCard3 = bottomlayerCard3(self)
        self.bottomlayerCard4 = bottomlayerCard4(self)
        self.bottomlayerCard5 = bottomlayerCard5(self)

        self.mineCard1 = mineCard1(self)
        self.mineCard2 = mineCard2(self)
        self.mineCard3 = mineCard3(self)
        self.mineCard4 = mineCard4(self)
        self.mineCard5 = mineCard5(self)

        self.shuffleCard1 = shuffleCard1(self)
        self.shuffleCard2 = shuffleCard2(self)
        self.shuffleCard3 = shuffleCard3(self)
        self.shuffleCard4 = shuffleCard4(self)
        self.shuffleCard5 = shuffleCard5(self)

        self.seeingeyeCard1 = seeingeyeCard1(self)
        self.seeingeyeCard2 = seeingeyeCard2(self)
        self.seeingeyeCard3 = seeingeyeCard3(self)
        self.seeingeyeCard4 = seeingeyeCard4(self)
        self.seeingeyeCard5 = seeingeyeCard5(self)

        self.copycatCard1 = copycatCard1(self)
        self.copycatCard2 = copycatCard2(self)
        self.copycatCard3 = copycatCard3(self)
        self.copycatCard4 = copycatCard4(self)
        self.copycatCard5 = copycatCard5(self)
        
        
        self.table = table(self)
        self.bot = CPU(self)
        self.deck = deck(self)
        self.cpuText = simpleGE.Label()
        self.cpuText.center = (300, 60)
        self.cpuText.text = f"Cards: {self.CPUlistLen}"
        self.cpuText.size = (100,40)
        
        self.deckBtn = simpleGE.Button()
        self.deckBtn.center = (185,245)
        self.deckBtn.size = (60,60)
        self.deckBtn.bgColor = (24,60,52)
        self.deckBtn.text = ""
        self.angel = "copycat"
        
        self.cpuDecision = simpleGE.Label()
        self.cpuDecision.center = (500, 50)
        self.cpuDecision.size = (225,80)
        self.cpuDecision.text = f"CPU played {self.whatdidcpudo}"
        
        self.cardsinDeck = simpleGE.Label()
        self.cardsinDeck.text = f"Cards In Deck: {self.cards}"
        self.cardsinDeck.center = (100, 450)
        self.cardsinDeck.size = (180,50)
        self.sprites = [
            self.bot,
            self.table,
            self.deckBtn,
            self.deck,
            self.hitmanCard,
            self.cpuText,
            self.cardsinDeck,
            self.shuffleCard1, self.shuffleCard2, self.shuffleCard3, self.shuffleCard4, self.shuffleCard5,
            self.angelCard1, self.angelCard2, self.angelCard3, self.angelCard4, self.angelCard5,
            self.arsonCard1, self.arsonCard2, self.arsonCard3, self.arsonCard4, self.arsonCard5,
            self.bottomlayerCard1, self.bottomlayerCard2, self.bottomlayerCard3, self.bottomlayerCard4, self.bottomlayerCard5,
            self.mineCard1, self.mineCard2, self.mineCard3, self.mineCard4, self.mineCard5,
            self.seeingeyeCard1, self.seeingeyeCard2, self.seeingeyeCard3, self.seeingeyeCard4, self.seeingeyeCard5,
            self.copycatCard1, self.copycatCard2, self.copycatCard3, self.copycatCard4, self.copycatCard5,
            self.cpuDecision
        ]
        
        self.card_data = {
    "shuffle": [
        self.shuffleCard1, self.shuffleCard2, self.shuffleCard3, self.shuffleCard4, self.shuffleCard5
    ],
    "angel": [
        self.angelCard1, self.angelCard2, self.angelCard3, self.angelCard4, self.angelCard5
    ],
    "arson": [
        self.arsonCard1, self.arsonCard2, self.arsonCard3, self.arsonCard4, self.arsonCard5
    ],
    "bottomlayer": [
        self.bottomlayerCard1, self.bottomlayerCard2, self.bottomlayerCard3, self.bottomlayerCard4, self.bottomlayerCard5
    ],
    "mine": [
        self.mineCard1, self.mineCard2, self.mineCard3, self.mineCard4, self.mineCard5
    ],
    "seeingeye": [
        self.seeingeyeCard1, self.seeingeyeCard2, self.seeingeyeCard3, self.seeingeyeCard4, self.seeingeyeCard5
    ],
    "copycat": [
        self.copycatCard1, self.copycatCard2, self.copycatCard3, self.copycatCard4, self.copycatCard5
    ]
}

    def process(self):
        self.cpuDecision.text = f"CPU played {self.whatdidcpudo}"
        self.CPUlistLen = len(self.CPUlist)
        # again, i know this is very unoptimized and laggy, but best i could do with my knowledge
        # the lag is because all of the code i have inside of process but its necessary to constantly update
        shuffle_cards = [self.shuffleCard1, self.shuffleCard2, self.shuffleCard3, self.shuffleCard4, self.shuffleCard5]
        angel_cards = [self.angelCard1, self.angelCard2, self.angelCard3, self.angelCard4, self.angelCard5]
        arson_cards = [self.arsonCard1, self.arsonCard2, self.arsonCard3, self.arsonCard4, self.arsonCard5]
        bottomlayer_cards = [self.bottomlayerCard1, self.bottomlayerCard2, self.bottomlayerCard3, self.bottomlayerCard4, self.bottomlayerCard5]
        mine_cards = [self.mineCard1, self.mineCard2, self.mineCard3, self.mineCard4, self.mineCard5]
        seeingeye_cards = [self.seeingeyeCard1, self.seeingeyeCard2, self.seeingeyeCard3, self.seeingeyeCard4, self.seeingeyeCard5]
        copycat_cards = [self.copycatCard1, self.copycatCard2, self.copycatCard3, self.copycatCard4, self.copycatCard5]

        all_cards = [card for cards in self.card_data.values() for card in cards]

        for card in all_cards:
            card.x, card.y = -1000, -1000

        for index, card_name in enumerate(self.PlayerList):
            if card_name not in self.card_data:
                continue 

            cards = self.card_data[card_name]
            for card in cards:
                if card.x < 0:  
                    card.x = 150 + index * 62
                    card.y = 340
                    break  


                # this was by far the hardest thing ive had to code, it took me quite a while to figure out positioning with this as you can only have one sprite on the screen per time so i couldnt use the same sprite aka 2 cards per sprite

        if self.Turn:

            
            if self.deckBtn.clicked:
                self.cards -= 1
                self.cardsinDeck.text = f"Cards In Deck: {self.cards}"
                self.PlayerList.append(self.deckList[0])
                self.deckList.pop(0)
                if "hitman" in self.PlayerList:
                    
                    if "angel" in self.PlayerList:
                        self.PlayerList.remove("angel")
                        self.PlayerList.remove("hitman")
                        print("removed angel for hitman")
                        self.Turn = False
                    else:
                        print("you lost")
                        instructions = Instructions()
                        self.stop()
                        instructions.start()
                else:
                    
                    self.Turn = False
            for card in shuffle_cards:
                if card.clicked:
                    random.shuffle(self.deckList)
                    if "shuffle" in self.PlayerList:
                        self.PlayerList.remove("shuffle") 
                    self.Turn = False
                    break
            for card in arson_cards:
                if card.clicked:
                    self.randomchoice = random.choice(self.CPUlist)
                    self.CPUlist.remove(self.randomchoice)
                    if "arson" in self.PlayerList:
                        self.PlayerList.remove("arson")  
                    self.Turn = False
                    break
            for card in bottomlayer_cards:
                if card.clicked:
                    self.PlayerList.append(self.deckList[-1])
                    self.deckList.pop(-1)
                    if "bottomlayer" in self.PlayerList:
                        self.PlayerList.remove("bottomlayer")
                    self.Turn = False
                    break
            for card in mine_cards:
                if card.clicked:
                    self.randomchoice = random.choice(self.CPUlist)
                    self.PlayerList.append(self.randomchoice)
                    self.CPUlist.remove(self.randomchoice)
                    if "mine" in self.PlayerList:
                        self.PlayerList.remove("mine")
                    self.Turn = False
                    break
            for card in seeingeye_cards:
                if card.clicked:
                    first, second, third = self.deckList[0], self.deckList[1], self.deckList[2]
                    print(f"first card",{first}, " second card", {second}, " third card", {third})
                    if "seeingeye" in self.PlayerList:
                        self.PlayerList.remove("seeingeye")
                    self.Turn = False
                    break
            for card in copycat_cards:
                if card.clicked:
                    self.PlayerList.append(self.CPUlist[-1])
                    if "copycat" in self.PlayerList:
                        self.PlayerList.remove("copycat")
                    self.Turn = False
                    break
        elif not self.Turn:
                self.cardsinDeck.text = f"Cards In Deck: {self.cards}"
                self.cpuChoice = random.randint(1,2)
                self.realThinking = random.randint(2,4)
                time.sleep(self.realThinking)
                if len(self.CPUlist) == 1:
                    for item in self.CPUlist:
                        if item == "angel":
                            self.cards -= 1
                            self.CPUlist.append(self.deckList[0])
                            self.deckList.pop(0)
                            self.cardsinDeck.text = f"Cards In Deck: {self.cards}"
                elif self.cpuChoice == 1:
                    self.CPUlist.append(self.deckList[0])
                    self.deckList.pop(0)
                    self.cpuText.text = f"Cards: {self.CPUlistLen}"
                    self.cards -= 1
                    self.cardsinDeck.text = f"Cards In Deck: {self.cards}"
                    self.whatdidcpudo = "draw"
                    for card in self.CPUlist:
                        if "hitman" == card:
                            if "angel" == card:
                                self.CPUlist.remove("angel")
                            else:
                                print("you won")
                                self.stop()
                                instructions = Instructions()
                                instructions.start()
                                
                    
                    self.Turn = True
                    
                elif self.cpuChoice == 2:
                    self.playedCard = random.choice(self.CPUlist) 
                    if self.playedCard == "arson":
                        self.chosen = random.choice(self.PlayerList)
                        self.PlayerList.remove(self.chosen)
                        self.whatdidcpudo = "arson"
                    elif self.playedCard == "bottomlayer":
                        self.CPUlist.append(self.deckList[-1])
                        self.deckList.pop(-1)
                        self.whatdidcpudo = "bottomlayer"
                    elif self.playedCard == "mine":
                        self.ChosenCard = random.choice(self.PlayerList)
                        self.CPUlist.append(self.ChosenCard)
                        self.PlayerList.remove(self.ChosenCard)
                        self.whatdidcpudo = "mine"
                    elif self.playedCard == "shuffle":
                        random.shuffle(self.deckList)
                        self.whatdidcpudo = "shuffle"
                    elif self.playedCard == "copycat":
                        self.CPUlist.append(self.PlayerList[-1])
                        self.whatdidcpudo = "copycat"
                    self.cpuText.text = f"Cards: {self.CPUlistLen}"
                    self.Turn = True
        if self.cards <= 10: # this is a check to make sure there wont be more angels than hitmans so the game can end with a loser
            for item in self.deckList:
                if item == "angel":
                    self.deckList.remove(item)
                    self.choice = random.choice(self.finalList)
                    self.deckList.append(self.choice)
      
            
                    

            

def main(): 
    keepGoing = True
    while keepGoing:
        instructions = Instructions()
        instructions.start()
        if instructions.response == "Settings":
            settings = Settings()
            settings.start()
        else:
            keepGoing = False
    
if __name__ == "__main__":
    main()
