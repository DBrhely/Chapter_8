class Televison(object):
    def channel(self, channel):
        channel = 0
        number = int(input("What channel would you like to go to?"))
        channel = number
        if channel < 0:
            print("Invalid channel number")
        return channel
    def volume(self, volume):
        question = input("Would you like to change the volume up or down?")
        if question == "up":
            Up = int(input("What would you like to raise it too?"))
            volume += Up
        if question == "down":
            Down = int(input("What would you like to lower to too?"))
            volume -= Down
        return volume   
def main():
    volume = 0
    channel = 0
    print("-----------------")
    print("Television turning on..")
    print("Tv Channel:", channel)
    print("Tv Volume:", volume)
    print("""
    1 - Change Channel
    2 - Change Volume
    3- Turn off TV
    """)
    choice = input("What would you like to do?")
    while choice != "3":
        if choice == "1":
            Televison.channel(channel)
            print("Tv Channel:", channel)
            print("Tv Volume:", volume)
        if choice == "2":
            Televison.volume(volume)
            print("Tv Channel:", channel)
            print("Tv Volume:", volume)
        if choice == "3":
            print("TV turning off..")
            print("Tv Channel:", channel)
            print("Tv Volume:", volume)
            
        choice = input("What would you like to do?")


main()
