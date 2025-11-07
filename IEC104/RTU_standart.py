import c104

# server and station preparation
server = c104.Server(ip="0.0.0.0", port=2404)

# add local station and points
station = server.add_station(common_address=47)
measurement_point = station.add_point(io_address=11, type=c104.Type.M_ME_NC_1, report_ms=1000)
command_point = station.add_point(io_address=12, type=c104.Type.C_RC_TA_1)

server.start()
