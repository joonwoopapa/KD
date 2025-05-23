# Kawasaki Disease Risk Prediction Application

이 애플리케이션은 가와사키병 환자의 IVIG 저항성과 관상동맥류 발생 위험을 예측하는 도구입니다.

## 주요 기능

- **IVIG 저항성 예측**: 혈액검사, 심초음파, 임상증상 데이터를 기반으로 IVIG 치료에 대한 저항성 위험을 예측
- **관상동맥류 발생 예측**: 동일한 데이터를 사용하여 관상동맥류 발생 위험을 예측
- **SHAP 기반 설명**: 각 예측에 대한 특성별 영향도를 시각화하여 제공
- **직관적인 UI**: 사용하기 쉬운 인터페이스와 명확한 결과 표시

## 시작하기

### 필수 요구사항

- Docker Desktop
  - Windows: [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
  - Mac: [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/)
  - Linux: [Docker Engine](https://docs.docker.com/engine/install/) + [Docker Compose](https://docs.docker.com/compose/install/)

### 설치 및 실행 방법

#### Windows 사용자
1. Git 설치
   - [Git for Windows](https://git-scm.com/download/win)를 다운로드하여 설치
   - 설치 과정에서 기본 옵션 선택

2. Docker Desktop 설치
   - [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/) 설치
   - 설치 완료 후 시스템 재시작

3. 저장소 클론 및 실행:
   - PowerShell이나 Command Prompt를 관리자 권한으로 실행
   - 원하는 디렉토리로 이동 후 다음 명령어 실행:
```powershell
git clone https://github.com/joonwoopapa/KD.git
cd KD
docker compose up
```

#### Linux/Mac 사용자
1. 저장소 클론:
```bash
git clone https://github.com/joonwoopapa/KD.git
cd KD
```

2. Docker Compose로 실행:
```bash
docker compose up
```

### 접속 방법

애플리케이션이 실행되면 웹 브라우저에서 다음 주소로 접속:
```
http://localhost:8501
```

## 입력 데이터

### 혈액검사
- Lymphocyte (%)
- Platelet count (10^3/ml)
- Cholesterol (mg/dL)
- CRP (mg/dL)
- Neutrophil (%)
- Total bilirubin (mg/dL)
- Phosphorus (mg/dL)
- Absolute Neutrophil count (10^9/L)

### 심초음파
- RCA z score
- LMCA z score
- LAD z score

### 임상증상
- 발열 기간 (일)

## 프로젝트 구조

```
KD/
├── src/               # 소스 코드
│   ├── config.py      # 설정 및 상수
│   ├── models.py      # 예측 모델 관리
│   └── visualization.py # 시각화 컴포넌트
├── models/            # 학습된 모델 파일
├── styles/            # CSS 스타일
└── app.py            # 메인 애플리케이션
```

## 모델 정보

- 다중 작업 학습(Multi-task Learning) 모델 사용
- SHAP (SHapley Additive exPlanations) 기반 설명 가능한 AI
- 자세한 정보는 [models/README.md](models/README.md) 참조

## 개발 정보

### 기술 스택
- Streamlit: 웹 인터페이스
- scikit-learn: 머신러닝 모델
- SHAP: 모델 설명
- Matplotlib: 데이터 시각화

### 코드 스타일
- Python 코드는 PEP 8 준수
- 모듈화된 구조로 유지보수성 향상
- 타입 힌팅 사용으로 코드 품질 향상

## 라이선스

이 프로젝트는 [라이선스 정보 추가] 하에 배포됩니다.

## 연락처

[연락처 정보 추가] 