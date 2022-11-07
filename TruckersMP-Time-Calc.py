class TimeCalc:
    def gametime_to_real(self, hours, mins) -> str:
        from datetime import datetime

        game_time_secs = (int(hours)*60 + int(mins))*60

        real_time_secs = game_time_secs / 10
        real_time_hours = real_time_secs // 60**2
        real_time_mins = round(real_time_secs / 60**2 - real_time_hours, 3) * 60

        now = datetime.strptime(f"{round(real_time_hours)}:{round(real_time_mins)}", '%H:%M')
        return now.strftime('%H:%M')

    def dist_speed_to_realtime(self, dist:int, speed:int) -> str:
        from datetime import datetime

        game_time_secs = ((round((dist / speed)))*60 + (round(((dist / speed) - round((dist / speed),0)) * 60)))*60

        real_time_secs = game_time_secs / 10
        real_time_hours = real_time_secs // 60**2
        real_time_mins = round(real_time_secs / 60**2 - real_time_hours, 3) * 60

        now = datetime.strptime(f"{round(real_time_hours)}:{round(real_time_mins)}", '%H:%M')
        return now.strftime('%H:%M')

if __name__ == "__main__":
    while True:
        dist = int(input("Введите дистацию: "))
        speed = int(input("Введите скорость: "))
        print(f"Реальное время: {TimeCalc().dist_speed_to_realtime(dist, speed)}")
        print()