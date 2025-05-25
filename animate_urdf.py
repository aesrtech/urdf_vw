from urdfpy import URDF


if __name__ == "__main__":
    robot = URDF.load('/home/user/robot.urdf')
    robot.animate()
