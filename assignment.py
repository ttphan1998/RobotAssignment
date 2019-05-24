import ai2thor.controller
import cv2
import keyboard
import yolo


def export_frame():
    event = controller.step(dict(action='Initialize', continuous=True))
    cv2.imwrite('img/image.jpg', event.cv2img)
    yolo.detect()


if __name__ == "__main__":
    controller = ai2thor.controller.Controller()
    controller.start(player_screen_height=480, player_screen_width=480)
    controller.reset('FloorPlan28')
    while True:
        try:
            if keyboard.is_pressed('a'):
                event = controller.step(dict(action='MoveLeft'))
            elif keyboard.is_pressed('d'):
                event = controller.step(dict(action='MoveRight'))
                export_frame()
            elif keyboard.is_pressed('w'):
                event = controller.step(dict(action='MoveAhead'))
            elif keyboard.is_pressed('s'):
                event = controller.step(dict(action='MoveBack'))
            elif keyboard.is_pressed('right arrow'):
                event = controller.step(dict(action='RotateRight'))
            elif keyboard.is_pressed('left arrow'):
                event = controller.step(dict(action='RotateLeft'))
            elif keyboard.is_pressed('up arrow'):
                event = controller.step(dict(action='LookUp'))
            elif keyboard.is_pressed('down arrow'):
                event = controller.step(dict(action='LookDown'))
	    elif keyboard.is_pressed('f'):
		export_frame()
            elif keyboard.is_pressed('esc'):
                exit()
        except Exception as error:
            raise error
