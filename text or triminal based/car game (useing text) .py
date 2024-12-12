cmd_line = ">"
limit = 9
null = 0
started = False

print(f"{cmd_line} if you have any problmem just type help.")

while null < limit:
     cmd = input(f"{cmd_line}").upper()
     if cmd == "HELP":
          print(f"{cmd_line}start - to start the car\nstop - stop the car\nquit - to quit the game")
     elif cmd == "START":
          if started:
               print("Car already started.")
          else:
               started = True
               print("The car has started.")
     elif cmd == "STOP":
          if not started:
               print("Car has already stopped.")
          else:
               started = False
               print("The car has stopped.")
     elif cmd == "QUIT":
          break
     else:
          print("ERROR, there is no command like that.")
else:
     quit()
