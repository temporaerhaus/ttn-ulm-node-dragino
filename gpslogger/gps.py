from time import sleep
from gps3 import gps3
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)        
        if data_stream.TPV['lat'] and data_stream.TPV['lon'] and data_stream.TPV['lat'] != 'n/a' and data_stream.TPV['lon'] != 'n/a':
            f = open('/home/pi/geo/geo.dat', 'w')
            fa = open('/home/pi/geo/geo_all.dat', 'a')
            f.write(str(data_stream.TPV['lat']) + '\n' + str(data_stream.TPV['lon']))
            fa.write('['+str(data_stream.TPV['lat']) + ',' + str(data_stream.TPV['lon'])+'],')
            f.close()
            fa.close()
        sleep(2)
        #print('Alt/Lat/Lon', data_stream.TPV['alt'], data_stream.TPV['lat'], data_stream.TPV['lon'])
