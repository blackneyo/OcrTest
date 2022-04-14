'''
2022.04.13 이동한
샘플 OCR 스크립트
샘플 이미지 읽기
'''
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread("Test1.jpg")  # cv2.imread() 매서드 사용해 이미지를 읽고 변수 img에 저장
img = cv2.resize(img, (900, 1000))
cv2.imshow("image", img) # 창을 무한히 표시 (커널 충돌 방지)

img_gray=cv2.imread("Test1.jpg", cv2.IMREAD_GRAYSCALE) # Gray scale로 변환
text = pytesseract.image_to_string(img, lang="kor", config='--oem 1 --psm 4') #이미지 문자열로 변환
print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Text to Audio
gTTS = 구글 번역의 택스트 음성 변환 API
'''

# from gtts import gTTS
# import os
#
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' ## 테서렉트 경로 설정
# aud = cv2.imread("Test2.jpg")
#
# txt = pytesseract.image_to_string(aud, lang="kor", ) #언어 설정 후 텍스트, 언어를 우회하는 gTTS를 사용하여 텍스트를 오디오로 변환
#
# print(txt)
# language = 'ko'
# outObj = gTTS(text=txt, lang=language, slow=False)
# outObj.save("aud.mp3") # 오디오 파일을 aud.mp3 로 저장
# print("오디오 파일 재생중")
# os.system('aud.mp3')


# -oem 1 -psm 4, 6