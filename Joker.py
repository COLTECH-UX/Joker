import random


def reminder():
    return "You can enter a Small Letter if you want to"


def notify():
    return "Now you have start the joke by entering HA/ha"


def people():
    return """
Actors(A)
FamilY(F)
Others(O)
"""


Actors = ["""
    Why is Kevin Hart such a good actor today ?
It is Because of he has a good HEART to ACT!!!
Think Again.
""", """
    Which Actor that study Geography ?
D ROCK!!!
"""]

FamilY = ["""
    What do you call the disease of parents ?
You call it Parenthesis
"""]

Others = ["""
    What kind of rice do a herbalist eat ?
Concussion Rice
Think Again!!!
"""]


def animals():
    return """
Land Animals(LA)
Fish(F)
Insects(I)    
"""


Land_Animals = ["""
    What is the richest Bird in the world ?
A GOLDEN Eagle
""", """
    Why is Elle so fat ?
Because she's an ELEPHANT!!!
Think again. 
""", """
    What do you call a bear without teeth ?
A Gummy Bear
Think again!!!
""", """
    What do you call a group of funny cows ?
You call it a Laughing Stock.
""", """
    What do you call an American Bee ?
You call it a USB.
Think Again!!!
"""]

Fish = ["""
    What is the richest fish in the world ?
A GOLD Fish
""", """
    What kind of music do a fish listen to ?
Something CATCHY!!!
Think again.
""", """
    Why's a fish so easy to weigh ?
Because it comes with it's own SCALES!!! 
""", """
    Why does a fish hate BasketBall
Because it comes with its own NET!!!
Think again.
""", """
    What's the cutest fish in the world ?
A CATFISH!!!
Think again.
""", """
    What is the funniest fish in the world ?
A CLOWNFISH.
"""]

Insects = ["""
    What is the most religious insect in the world ?
A Praying Mantis
""", """
    What makes Master Roshi so corky sometimes ?
A Cockroach
"""]


def animes():
    return """
Dragon Balls(DB)
Naruto(N)   
"""


Dragon_Balls = ["""
    What do the dragon tell Goku to do ?
Stop touching my BALLS!!!
Think again.
""", """
    Why does Goku doesn't wear a underpants ?
Because he got Dragon "BALLS". 
""", """
    What did Goku tell the doctor to do about the COVID-19 patients ?
He told him to fight their "IMPERFECT CELL".
Think again. 
""", """
    What did Cooler tell Frieza to do when he was angry ?
He told him to "GO-KU" himself down.
Think again.
"""]

Naurto = ["""
    What do you call someone sucks at baking cake ?
SASUKE!!!
Think again.
""", """
    What you call someone haves the balls to fight Naruto ?
BORUTO!!!
Think again."""]


def technology():
    return """
Laptops(L)
Phones(PH)
Desktops(DT)
Cars(CR)  
"""


Laptops = ["""
    Which Laptop is known for its good health bar ?
HP!!!
Think again!!!
"""]

Desktops = ["""
    Which Desktop is edible for work ?
APPLE!!!
"""]

Cars = ["""
    What do you call a car where a black and white man enter ?
A RACE Car!!!
""", """
    What do you call a car that stalks on its owner ?
A STOCK Car!!!
"""]

Phones = ["""
    What do you call a phone that is a year plus ?
You call it ONE+plus!!!
Think Again.
""", """
    Which phone that has the sweetest voice for singing ?
SAMSUNG!!!
Think again.  
""", """
    What do you call a phone that only has one eye ?
You call an i-phone. 
"""]

Movies = ["""
    What do you call a God that is Zealous in everything he does ?
You call him GodZilla 
""", """
    What do you say when you see 2 dead people playing pool ?
Deadpool 2 
""", """
    What do you call a thief that robs in a hood ?
Robin Hood
""", """
    What do you call a girl that is daddy's pet ?
You call her Daddys little girl
""", """
    What do you call a man that do his things mistakenly ?
You call him Accident Man
""", """
    What do you say when you see two spies going undercover in a mission ?
Spies in Disguise
""", """
    What do you call a fight that is being filmed ?
You call it an Acts of Violence
"""]

Programming = ["""
    Why a program so easy to interact with this days ?
Because it comes with an interFACE
""", """
    Which Programming Language that owns the best coffee shop ?
Java 
""", """
    Which Programming Language that belongs to the entertainment industry ?
JavaSCRIPT.
Think again!!! 
""", """
    Which Programming Language that has the poorest eyesight ?
C++.
Think again!!!  
""", """
    Why does C++ have poor eyesight ?
Because it doesn't C#.
Think again!!!
"""]

Places = ["""
    Which place does a host tells on his vistors ?
A HOTEL.
Think again!!! 
""", """
    Which place does a lobster bunk in ?
A Lobby
""", """
    Where does Jasmin usually visit Abu the monkey ?
ABUJA(Which is the capital of Nigeria)
Think again
"""]

Social_Media_Platforms = ["""
    Which Social Media Platform that have best voice for singing ?
Twitter
""", """
    Which Social Media Platform that keeps your face in a book ?
FaceBook
""", """
    Which Social Media Platform that measures your stuffs instantly in Grams ?
INSTAGRAM
"""]

# User Input

Name = input("Enter Your Name Here: ")
print("Hi there " + Name + ". Welcome to the Joker Program where we bring Jokes for you to smile ^_^")
print(" So " + Name + """ I would like you to choose from the options below, where you want a joke to come from
  People(P)
  Animals(A)   
  Animes(AM)
  Technologies(T)
  Movies(M)
  Programming(PG)
  Places(PL)
  Social Media Platforms(SMP)
  Quit(Q)
""")

while True:
    print(reminder())
    Choice = input("Enter Your Choice Here: ").lower()
    if Choice == "p":
        print(people())
        Option = input("Enter Your Option Here: ").lower()
        if Option == "a":
            Value_People = random.choice(Actors)
            print(Value_People)
        if Option == "f":
            Value_People = random.choice(FamilY)
            print(Value_People)
        elif Option == "o":
            Value_People = random.choice(Others)
            print(Value_People)

    if Choice == "a":
        print(animals())
        Decision = input("Enter Your Option Here: ").lower()
        if Decision == "la":
            Value_Animals = random.choice(Land_Animals)
            print(Value_Animals)
        if Decision == "f":
            Value_Animals = random.choice(Fish)
            print(Value_Animals)
        elif Decision == "i":
            Value_Animals = random.choice(Insects)
            print(Value_Animals)

    elif Choice == "am":
        print(animes())
        Condition = input("Enter Your Option Here: ").lower()
        if Condition == "db":
            Value_Animes = random.choice(Dragon_Balls)
            print(Value_Animes)
        if Condition == "n":
            Value_Animes = random.choice(Naurto)
            print(Value_Animes)


    elif Choice == "t":
        print(technology())
        Option_2 = input("Enter Your Option Here: ").lower()
        if Option_2 == "l":
            Value_Technology = random.choice(Laptops)
            print(Value_Technology)
        if Option_2 == "ph":
            Value_Technology = random.choice(Phones)
            print(Value_Technology)
        elif Option_2 == "dt":
            Value_Technology = random.choice(Desktops)
            print(Value_Technology)
        elif Option_2 == "cr":
            Value_Technology = random.choice(Cars)
            print(Value_Technology)

    elif Choice == "m":
        Value_Movies = random.choice(Movies)
        print(Value_Movies)

    elif Choice == "pg":
        Value_Programming = random.choice(Programming)
        print(Value_Programming)

    elif Choice == "pl":
        Value_Places = random.choice(Places)
        print(Value_Places)

    elif Choice == "smp":
        Value_SocialMediaPlatforms = random.choice(Social_Media_Platforms)
        print(Value_SocialMediaPlatforms)

    elif Choice == "q":
        break








