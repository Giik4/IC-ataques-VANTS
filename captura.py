from pymavlink import mavutil

the_connection = mavutil.mavlink_connection('udpin:localhost:14551')

the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" %
      (the_connection.target_system, the_connection.target_component))


while 1: 
    msg = the_connection.recv_match(
        type='GLOBAL_POSITION_INT', blocking=True)
    print(msg) 
