# 가상환경 생성 -> VSCode에서 사용하는
# 파이썬 인터프리터를 가상환경에 있는 인터프리터로 설정
# > select ~ -> 현 폴더 내 가상환경의 인터프리터 설정

# 내장 모듈 -> sys, os, pathlib
# import sys
# sys -> 현재 실행중인 인터프리터의 정보를 담고 있다.
# print(__file__)
# __로 시작하는 변수를 매직 변수
# 매직변수 시스템(인터프리터)이 변수의 값을 설정

# for path in sys.path:
#     print(path)

# __name__: 매직 변수 -> 현재 파일의 실행 이름
# 1) main script 실행: __main__
# 2) import ~~ 모듈로 실행: 파일이름(모듈 이름)
# print(__name__)

# python test.py -> test.py를 main script로 실행
# python -m teset -> test 모듈을 main script로 실행

# python -m test
# -> 실행 -> test 모듈을 메인 스크립트로 실행 
#            모듈을 검색
#            1) 내 폴더 -> c:\temp\happyday
#            2) PYTHONPATH -> 등록된 디렉토리
#            3) Built-Module 디렉토리
#            4) Site-package 디렉토리

# import sys

# sys.path.insert(0, "c:\\")
# for v in sys.path:
#     print(v)

# import sys
# import network
# print("이제 시작할까요?")
# print(network.recv())
# print(sys.modules['network'].recv())

import gsc_1

print(gsc_1.g_1.name)
print(gsc_1.g_2.name)
print(gsc_1.g_3.name)

# import gsc_1
# gsc_1 -> 디렉토리 또는 .py
# 디렉토리이면 -> 패키지 방식으로 처리
# 현재 디렉토리에 __init__.py 있나?
# 1) 있다면 -> 일반 패키지로 처리
# 2) 없다면 -> namespace 패키지로 처리
# 일반 패키지이면 -> __init__.py 를 실행
