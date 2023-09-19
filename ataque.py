from pymavlink import mavutil


the_connection = mavutil.mavlink_connection('udpin:localhost:14550')

the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" %
      (the_connection.target_system, the_connection.target_component))




the_connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_global_int_message(10, the_connection.target_system,
                        the_connection.target_component, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, int(0b110111111000), int(-35.36384566 * 10 ** 7), int(149.16480758 * 10 ** 7), 10, 0, 0, 0, 0, 0, 0, 0, 0))

msg = the_connection.recv_match(type= 'COMMAND_ACK', blocking=True)
print(msg)