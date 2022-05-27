import time

print("Time: ", time.time()) # Time:  1651681071.4428504
print("\nTime: ", time.localtime(time.time())) #Time:  time.struct_time(tm_year=2022, tm_mon=5, tm_mday=4, tm_hour=18, tm_min=18, tm_sec=23, tm_wday=2, tm_yday=124, tm_isdst=1)
print("\nAño: ", time.localtime(time.time()).tm_year) # Año:  2022
print("\nMes: ", time.localtime(time.time()).tm_mon) # Mes:  5
print("\nDía: ", time.localtime(time.time()).tm_mday) # Día:  4
print("\nMinutos: ", time.localtime(time.time()).tm_min) # Minutos:  20
print("\nSegundos: ", time.localtime(time.time()).tm_sec) # Segundos:  35
print("\nTime: ", time.asctime(time.localtime(time.time()))) # Time:  Wed May  4 18:22:04 2022