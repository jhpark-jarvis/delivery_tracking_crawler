# delivery_tracking_crawler

배송 추적 상태를 확인하고 주문 상태를 갱신하는 프로젝트입니다.
해당 레포지토리는 2023년 작성된 코드입니다.
2026년 7월 시점에서 정상 동작하지 않을 수 있습니다.
동작이 가능하다면 가급적 데몬으로 띄워 사용하시길 권장합니다.

## 구성

- `delivery_bot_craw_util.py`
  - 배송 추적 실행 진입점입니다.
- `app.py`
  - 배송 추적 스케줄 실행 진입점입니다.
- `config.py`
  - DB 접속 정보를 관리합니다.
- `repositories/`
  - MySQL 접근 계층입니다.
  - `delivery_repository.py`가 포함됩니다.
- `services/`
  - 배송 상태 판별 로직을 담고 있습니다.
  - `tracking_service.py`가 포함됩니다.
- `init_db.py`
  - MySQL 스키마 생성 스크립트입니다.
- `schema.sql`
  - 주문/주문상세 테이블 생성 SQL입니다.
- `requirements.txt`
  - 이 프로젝트의 설치 의존성 목록입니다.
- `run.bat`
  - DB 초기화 후 배송 추적을 실행하는 Windows용 런처입니다.

## 실행 전제

- Python 3.x
- `selenium`
- `schedule`
- `pymysql`
- 브라우저 드라이버가 동작 가능한 환경
- 내부 MySQL 서버 접근 가능해야 함

## 실행 방법

프로젝트 폴더로 이동한 뒤 실행합니다.

```bash
cd .\delivery_tracking_crawler
python init_db.py
python delivery_bot_craw_util.py
```

Windows에서는 `run.bat`로 한 번에 실행할 수 있습니다.

## 주의사항

- DB 접속 정보가 코드에 하드코딩되어 있습니다.
- 추적 대상 주문은 `T_order`, `T_orderList` 테이블을 사용합니다.
- 배송 추적 결과에 따라 `T_orderList.orderState`가 변경됩니다.
- 현재는 10초 간격으로 반복 실행하도록 되어 있습니다.

## 독립성 기준

이 폴더는 배송 추적 기능만 포함합니다.
다른 프로젝트와 섞이지 않도록 `repositories/`와 `services/`를 분리한 구조로 구성했습니다.

## 흐름

`config.py` -> `services/` -> `repositories/` -> DB 업데이트
