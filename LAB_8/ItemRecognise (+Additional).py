import cv2
import numpy as np

def track_marker(video_source, ref_image_path, fly_image_path, output_file):
    cap = cv2.VideoCapture(video_source)
    ref_image = cv2.imread(ref_image_path, 0)
    fly_image = cv2.imread(fly_image_path, -1)
    fly_h, fly_w, _ = fly_image.shape
    
    with open(output_file, 'w') as f:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(gray_frame, ref_image, cv2.TM_CCOEFF_NORMED)
            _, _, min_loc, max_loc = cv2.minMaxLoc(res)
            
            x, y = max_loc
            f.write(f"{x}, {y}\n")
            
            x_center, y_center = x + ref_image.shape[1] // 2, y + ref_image.shape[0] // 2
            fly_x1, fly_y1 = x_center - fly_w // 2, y_center - fly_h // 2
            fly_x2, fly_y2 = fly_x1 + fly_w, fly_y1 + fly_h
            
            if 0 <= fly_x1 < frame.shape[1] and 0 <= fly_y1 < frame.shape[0] and fly_x2 < frame.shape[1] and fly_y2 < frame.shape[0]:
                fly_alpha = fly_image[:, :, 3] / 255.0
                for c in range(3):
                    frame[fly_y1:fly_y2, fly_x1:fly_x2, c] = (fly_alpha * fly_image[:, :, c] + (1 - fly_alpha) * frame[fly_y1:fly_y2, fly_x1:fly_x2, c])
            
            cv2.rectangle(frame, max_loc, (x + ref_image.shape[1], y + ref_image.shape[0]), (0, 255, 0), 2)
            cv2.imshow('Tracking', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    track_marker(0, 'ref-point.jpg', 'fly64.png', 'marker_coords.txt')