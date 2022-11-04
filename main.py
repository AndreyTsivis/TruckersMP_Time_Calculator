from datetime import datetime

game_time_in = input("Input game time in \"hh:mm\" format: ")
game_time_split = game_time_in.split(":") 

game_time_secs = (int(game_time_split[0])*60 + int(game_time_split[1]))*60

real_time_secs = game_time_secs / 10
real_time_hours = real_time_secs // 60**2
real_time_mins = round(real_time_secs / 60**2 - real_time_hours, 3) * 60

now = datetime.strptime(f"{round(real_time_hours)}:{round(real_time_mins)}", '%H:%M')
print(f"\nReal time: {now.strftime('%H:%M')}")