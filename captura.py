from pymavlink import mavutil
import csv

with open('dataAtaque.csv', 'w', newline='') as csvfile:
    campos_head =['tempo','latitude','longitude','altitude']
    writer = csv.DictWriter(csvfile, fieldnames=campos_head)

the_connection = mavutil.mavlink_connection('udpin:localhost:14551')

the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" %
      (the_connection.target_system, the_connection.target_component))

writer.writerheader()

while 1:
    try: 
        altitude = the_connection.messages['GLOBAL_POSITION_INT'].alt
        latitude = the_connection.messages['GLOBAL_POSITION_INT'].lat
        longitude = the_connection.messages['GLOBAL_POSITION_INT'].lon
        timestamp = the_connection.messages['GLOBAL_POSITION_INT'].time_boot_ms
        print('altitude: ',altitude)
        print('latitude: ',latitude)
        print('longitude: ',longitude)
        print('tempo ',timestamp)
        writer.writerow({'tempo': timestamp,'latitude': latitude, 'longitude':longitude, 'altitude':altitude} )

    except:
        print('no GLOBAL_POSITION_INT message received')
