import os
#change directory-> chdir 모르면 구글검색하면서 해보기
#리눅스에서 .은 현재폴더를 뜻함
os.chdir(r'C:\Users\student\change\SSAFY지원자')

for filename in os.listdir("."):
    after_name = filename.replace("SAMSUNG","SSAFY")
    os.rename(filename, after_name)
   
   
    #os.rename(filename ,"SSAMSUNG_"+filename)
    