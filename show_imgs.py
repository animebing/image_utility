import sys, os
import cv2
import glob

def show_imgs(img_dir):

    img_path_glob = glob.glob(os.path.join(img_dir, '*.jpg'))
    img_path_list = sorted(img_path_glob)
    files_num = len(img_path_list)

    terminate, is_paused = False, False

    idx = 0
    while not terminate:

        if not is_paused:
            img = cv2.imread(img_path_list[idx])
            #img = cv2.resize(img, (0, 0), fx=2.0, fy=2.0)
            idx += 1

        cv2.imshow('image', img)
        key = cv2.waitKey(20)

        if key & 255 == 27:  # ESC
            print("terminating")
            terminate = True
        elif key & 255 == 32:  # ' '
            print("toggeling pause: " + str(not is_paused))
            is_paused = not is_paused
        elif key & 255 == 115:  # 's'
            img = cv2.imread(img_path_list[idx])
            #img = cv2.resize(img, (0, 0), fx=2.0, fy=2.0)
            idx += 1
            is_paused = True

        if idx == files_num:
            terminate = True

    cv2.destroyAllWindows()

def my_plot(img, boxes):

    color = (0, 0, 255)
    for i in range(len(boxes)):
        box = boxes[i]

        cls_name = box[0]
        if cls_name != "person":
            continue

        x, y, w, h = box[2]
        pt1 = int(x - w / 2), int(y - h / 2)
        pt2 = int(x + w / 2), int(y + h / 2)
        if pt1[0] <= 520 and pt1[1] <= 70:
            continue
        if h / w >= 6.0:
            continue

        cv2.rectangle(img, pt1, pt2, color, 2)

    return img

if __name__ == "__main__":

    if len(sys.argv) == 2:
        img_dir = sys.argv[1]
        show_imgs(img_dir)
    else:
        print('Usage: ')
        print('  python show_imgs.py img_dir')
