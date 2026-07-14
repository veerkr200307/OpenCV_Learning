import cv2 as cv
import numpy as np

BrushCOL = (0, 255, 0)
BrushSiz = 5
drawing = False

blank = np.zeros((700,700,3), dtype="uint8")

def mouse(event, x, y, f, p):
    global drawing
    global BrushCOL
    global BrushSiz

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True

    if event == cv.EVENT_MOUSEMOVE and drawing:
        # BrushSiz is now the radius
        cv.circle(blank, (x, y), BrushSiz, BrushCOL, -1)

    if event == cv.EVENT_LBUTTONUP:
        drawing = False


cv.namedWindow("canvas")
cv.setMouseCallback("canvas", mouse)

while True:

    cv.imshow("canvas", blank)

    key = cv.waitKey(1) & 0xFF

    if key == ord('x'):
        break

    elif key== ord('e') :
        BrushCOL=(0,0,0)

    elif key == ord('b'):
        BrushCOL = (255, 0, 0)

    elif key == ord('g'):
        BrushCOL = (0, 255, 0)

    elif key == ord('r'):
        BrushCOL = (0, 0, 255)

    elif key == ord('+'):
        BrushSiz += 2

    elif key == ord('-'):
        if BrushSiz > 1:
            BrushSiz -= 2

    elif key == ord('c'):
        blank[:] = 0          # Clears canvas efficiently

    elif key == ord('s'):
        cv.imwrite("PaintApp\ScreenShots\drawing.png", blank)
        print("Drawing Saved!")

cv.destroyAllWindows()