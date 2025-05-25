from urdfpy import URDF


if __name__ == "__main__":
    robot = URDF.load('/home/aesrtech/docs/Стажировка/Модели роботов/robot1.urdf')
    robot.animate()
