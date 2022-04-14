from pdf2image import convert_from_path

f = "C:\\Users\\4lab\\PycharmProjects\\pdfToimg\\Test.pdf"

s = "C:\\Users\\4lab\\PycharmProjects\\pdfToimg\\"

pages = convert_from_path(f)

for i, page in enumerate(pages):
    page.save(s + "Test" + str(i+1) + ".jpg", "JPEG")

print('conversion complete')