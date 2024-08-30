# Flask-MongoDB 채팅 애플리케이션 (Chat Application)

이 프로젝트는 Flask와 MongoDB를 사용하여 구축된 채팅 애플리케이션으로, Docker를 통해 컨테이너화되어 있습니다.

## 프로젝트 구조 (Project Structure)

```
.
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── socket_events.py
│   └── templates/
├── .env
├── .gitignore
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## 필수 조건 (Prerequisites)

- Docker
- Docker Compose

## 설정 방법 (Setup)

1. 저장소를 클론합니다:
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. 루트 디렉토리에 `.env` 파일을 생성하고 환경 변수를 추가합니다:
   ```
   SECRET_KEY=your_secret_key
   MONGO_URI=mongodb://mongo:27017/chatapp
   ```
   
   **중요**: `.env` 파일은 민감한 정보를 포함하고 있으므로 절대로 버전 관리 시스템에 커밋하지 마세요!

3. Docker 컨테이너를 빌드하고 실행합니다:
   ```
   docker-compose up --build
   ```
   
   **참고**: 첫 실행 시 시간이 좀 걸릴 수 있습니다. 모든 의존성을 다운로드하고 이미지를 빌드하기 때문입니다.

## 사용 방법 (Usage)

- Flask 애플리케이션은 `http://localhost:5000`에서 접근 가능합니다.
- MongoDB Express (데이터베이스 관리 인터페이스)는 `http://localhost:5001`에서 접근 가능합니다.
  - 사용자 이름: root
  - 비밀번호: 1234

**주의**: 이 접속 정보는 개발 환경용입니다. 실제 운영 환경에서는 반드시 보안을 강화해야 합니다!

## 개발 (Development)

- 애플리케이션 코드는 볼륨으로 마운트되어 있어, `app` 디렉토리의 변경 사항이 실시간으로 반영됩니다.
- Flask 개발 서버는 코드 변경 시 자동으로 재시작됩니다.

**팁**: 코드를 수정한 후 변경 사항이 바로 적용되지 않는다면, 브라우저 캐시를 지우고 새로고침해보세요.

## 서비스 (Services)

- `web`: Flask 애플리케이션
- `mongo`: MongoDB 데이터베이스
- `mongo-express`: 웹 기반 MongoDB 관리 인터페이스

## 주의사항 (Notes)

- 이 설정은 개발용으로 구성되어 있습니다. 실제 운영 환경에서는 추가적인 보안 조치가 필요합니다.
- `.env` 파일을 버전 관리 시스템에 커밋하지 않도록 주의하세요.

## 문제 해결 (Troubleshooting)

- 컨테이너가 제대로 시작되지 않는 경우, `docker-compose logs` 명령어를 사용하여 로그를 확인해보세요.
- MongoDB 연결 문제가 발생하면 `MONGO_URI` 환경 변수가 올바르게 설정되어 있는지 확인하세요.