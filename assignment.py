#Import WebexTeamAPI
from webexteamssdk import WebexTeamsAPI;

#Webex token
teams_token = input ("Enter Your access token : ")
api = WebexTeamsAPI(access_token= teams_token)

#To testConnection
def testConnection(): 
    print ("Connecting....")
    webex = api.people.me()

    if webex : 
        print("Successful")

#To display the user details
def information(): 
    webex = api.people.me()
    print(f"Display Name : {webex.displayName}")
    print(f"Nickname : {webex.nickName}")
    print(f"Emails : {', '.join(webex.emails)}")

#to displayRoom
def displayRoom():
    print("\nList of Rooms:")
    rooms = api.rooms.list(max=5)  # list 5 rooms
    room_count = 0

    for room in rooms:
        print(f"Room ID : {room.id}")
        print(f"Room Title : {room.title}")
        print(f"Data Created  : {room.created}")
        print(f"Last Activity : {room.lastActivity}\n")

        room_count += 1
        if room_count >= 5 :
            break

#to createRoom
def createRoom():
    titleRoom = input("Enter the title of the new room: ")
    dataRoom = {"title": titleRoom}
    try:
        new_room = api.rooms.create(titleRoom)
        print(f"Room '{new_room.title}' (Room ID: {new_room.id}) has been created successfully.")
    except api:
        print(f"Failed to create the room.")

#Import the ApiError class
from webexteamssdk import ApiError

#to sendMessage
def sendMessage():
  
  #To list room
  print("\nList of Rooms:")

  roomList = list(api.rooms.list(max=5))

  for i, room in enumerate(roomList):
    print(f"{i+1}. {room.title}")

  while True:
    try:
      room_choice = int(input("\nEnter the number of the room to send the message to: "))
      if room_choice > 0 and room_choice <= len(roomList):
        break
      else:
        print("Invalid room number, please try again")
    except ValueError:
      print("Please enter a valid number")

  selected_room = roomList[room_choice-1]

  while True:
    message = input("Enter your message: ")
    if message:
      break
    else:
      print("Message cannot be empty, please try again")

  try:
    api.messages.create(roomId=selected_room.id, text=message)
  except ApiError as e:
    print("Error sending message:", e)

  print(f"\nMessage sent to room '{selected_room.title}'")
    
#list option
while True:
   print("\nOptions to select: ")
   print("0: Test Connection")
   print("1: Display Information")
   print("2: Display Rooms")
   print("3: Create Room")
   print("4: Send Message")
   print("5: Exit")

   option = input("\nSelect your option: ")

   if option == "0": #option for test connection
        testConnection() 
   elif option =="1": #option for display info
        information() 
   elif option =="2": #option for display 5 rooms
        displayRoom()
   elif option =="3": #option for create room
        createRoom()
   elif option =="4":#option for send message
        sendMessage()
   elif option == "5":#option for back to main menu
        print("Exit")
        break
   else:
        print("Invalid option")