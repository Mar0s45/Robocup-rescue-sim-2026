from controller import Robot, Motor, GPS, InertialUnit, Lidar, Camera

robot = Robot()
timestep = int(robot.getBasicTimeStep())

wheel1 = robot.getDevice("wheel1 motor")
wheel2 = robot.getDevice("wheel2 motor")
wheel1.setPosition(float('inf'))
wheel2.setPosition(float('inf'))
wheel1.setVelocity(0)
wheel2.setVelocity(0)
#inertial measurment unit
imu = robot.getDevice("inertial_unit")
imu.enable(timestep)

gps = robot.getDevice("gps")
gps.enable(timestep)
#light detection and ranging, gives list of 360 distances around robot
lidar = robot.getDevice("lidar")
lidar.enable(timestep)
lidar.enablePointCloud()

camera = robot.getDevice("camera1")
camera.enable(timestep)




while robot.step(timestep) != -1:
    #vals = values
    imu_vals = imu.getRollPitchYaw()
    gps_vals = gps.getValues()
    lidar_vals = lidar.getRangeImage()
    cam_image = camera.getImage()
    print(imu_vals)
    print(gps_vals)
    