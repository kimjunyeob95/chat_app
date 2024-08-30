FROM python:3.9-slim-bullseye

WORKDIR /app

# Python 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 애플리케이션 실행
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]