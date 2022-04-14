# OcrTest
텍스트 음성인식
pytesseract 사용

#pytesseract

pytesseract의 image_to_string 사용

parameter = (사용 이미지, 언어, oem, psm 값 지정)

# oem = OCR Engine modes
0 - Legacy engine only. xx 한글 안됨

1 - Neural nets LSTM engine only. 한글인식

2 - Legacy + LSTM engines.  xxxx안됨

3 - Default, based on what is available. ** 한글인식


# psm = Page segmentation modes
0 - Orientation and script detection (OSD) only.  -- 방향및 스크립트 감지(OSD) 만 해당

1 - Automatic page segmentation with OSD. ODB로 자동 페이지 분할

2 - Automatic page segmentation, but no OSD, or OCR. 자동페이지 분할,osd나 ocR은 없음

3 - Fully automatic page segmentation, but no OSD. (Default) 완전히 자동으로 페이지 분할, OSD없음

4 - Assume a single column of text of variable sizes.한글인식됨....가변적인 크기의 1라인 텍스트

5 - Assume a single uniform block of vertically aligned text. 수직텍스트 ...일본어같은경우

6 - Assume a single uniform block of text. 한글인식.....텍스트의 균일한 단일 블록을 가정함

7 - Treat the image as a single text line. 1라인 텍스트로 처리

8 - Treat the image as a single word. 1단어로 처리

9 - Treat the image as a single word in a circle. 원 안의 1단어로 처리

10 - Treat the image as a single character.   1문자로 처리

11 - Sparse text. Find as much text as possible in no particular order. 한글인식...특정 순서없이 가능한 한 많은 텍스트 찾기 ***

12 - Sparse text with OSD. 한글인식 ODB가 포함된 Sparse

13 - Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.  원시라인, 이미지를 단일 텍스트로 처리




# [출처]
Tesseract OCR oem psm|작성자 바다사랑

# test1 에 대한 insight
![Test1](https://user-images.githubusercontent.com/87853267/163346471-eca1da25-868a-44b3-b59d-590bf2b4011f.jpg)
![test1텍스트변환](https://user-images.githubusercontent.com/87853267/163346484-2fe8d249-893d-42fa-b335-ab7872619eb2.png)
