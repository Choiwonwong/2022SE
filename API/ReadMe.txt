MrDae API를 실행하기 위해선 다음을 준수해야한다.

0. MrDae.zip 파일 압축 해제
1. 파이썬 3.9.12 버전 설치 - ???
2. 가상환경 임의로 생성 - sudo apt-get install python3-venv / cd ~ / python3 -m venv SE
3. 가상환경 활성화 후 requirement.txt에 존재하는 패키지 설치 - source SE/bin/activate / requirement.txt로 작업폴더 이동 후 / pip3 install -r requirement.txt
4. 장고 마이그레이션 생성 및 마이그레이션 수행. - cd MrDaeApi / python manage.py makemigrations / python manage.py migrate
5. sqlite 데이터베이스에 최초 쿼리 입력(fixed table) - python query.py
6. 장고 백엔드 서버 실행(8000포트) - python manage.py runserver 0.0.0.0:8000

실제 통신을 하는 API 서버 URL은 http://0.0.0.0:8000 이다

가장 상위의 URL 분기는 
    :8000/MrDae - MrDae 서비스 기능
    :8000/auth/registration - 회원가입
    :8000/auth/login - 로그인