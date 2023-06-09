import cv2


# 웹캠 연결
cap = cv2.VideoCapture(1)


# 웹캠에서 fps 값 획득
fps = cap.get(cv2.CAP_PROP_FPS)
print('fps', fps)


width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width, height)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
writer = cv2.VideoWriter('./output.mp4', fourcc, fps, (width, height))

while True:

    # 웹캠에서 이미지 읽어옴
    ret,img_color = cap.read()

    if ret == False:
        print('웹캠에서 영상을 읽을 수 없습니다.')
        break

    writer.write(img_color)

    # cv2.imshow("Color", img_color)


    # # ESC키 누르면 중지
    # if cv2.waitKey(1)&0xFF == 27:
    #     break

cap.release()
writer.release()
cv2.destroyAllWindows()