
![main](https://github.com/Team-hwaE/Capston_hwa_E/assets/87376242/a83f0679-d86a-4aeb-be03-911cb583fe07)

# skinTree : 협업필터링과 머신러닝을 활용한 성분 맞춤형 화장품 추천 서비스

> **이화여자대학교 컴퓨터공학전공 캡스톤디자인프로젝트 : 2023-9 ~ 2024-5**
<br>
스킨트리는 기존에 잘 맞았던 화장품을 입력하면 자동으로 성분리스트를 생성하고, 당신의 성분프렌즈를 찾아 화장품을 추천해주는 서비스입니다.
<br>

## 🔧 팀원 소개

|      정다희       |          안민영         |       임수화         |                                                                                                               
| :------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | 
|   <img width="160px" src="https://github.com/Team-hwaE/Capston_hwa_E/assets/87376242/fc8c4c59-d033-4c38-ad18-7e2d6daeb9e9" />    |                      <img width="160px" src="https://user-images.githubusercontent.com/50205887/207570536-f5a82e48-99a1-4399-91d3-75fc5f8f3349.png" />    |                   <img width="160px" src="https://github.com/Team-hwaE/Capston_hwa_E/assets/87376242/89aa9120-c3fe-490c-a1e1-4df72578488e"	/>   |
|   [@da2mon](https://github.com/da2mon)   |    [@minzer01](https://github.com/minzer01)  | [@aihamster](https://github.com/aihamster)  |
| 이화여자대학교 컴퓨터공학과 4학년 | 이화여자대학교 컴퓨터공학과 4학년 | 이화여자대학교 컴퓨터공학과 4학년 |



## 배포 주소

> **개발 버전** : [http://voluntain.cs.skku.edu/](http://voluntain.cs.skku.edu/) <br>


## 프로젝트 소개

#### 스킨트리는 두 가지 화장품 추천 기능을 제공합니다.
1. 성분프렌즈 (유사 사용자 기반) 추천
2. 에디터 (제품 성분 기반) 추천


## 시작 가이드
### Requirements
For building and running the application you need:

- [Node.js 14.19.3](https://nodejs.org/ca/blog/release/v14.19.3/)
- [Npm 9.2.0](https://www.npmjs.com/package/npm/v/9.2.0)
- [Strapi 3.6.6](https://www.npmjs.com/package/strapi/v/3.6.6)

### Installation
``` bash
$ git clone https://github.com/Voluntain-SKKU/Voluntain-2nd.git
$ cd Voluntain-2nd
```
#### Backend
```
$ cd strapi-backend
$ nvm use v.14.19.3
$ npm install
$ npm run develop
```

#### Frontend
```
$ cd voluntain-app
$ nvm use v.14.19.3
$ npm install 
$ npm run dev
```

---

## Stacks 🐈

### Environment
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)             

### Config
![npm](https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white)        

### Development
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=Javascript&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Strapi](https://img.shields.io/badge/Strapi-2F2E8B?style=for-the-badge&logo=Strapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=Next.js&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=Bootstrap&logoColor=white)
![Material UI](https://img.shields.io/badge/Material%20UI-007FFF?style=for-the-badge&logo=MUI&logoColor=white)

### Communication
![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white)
![GoogleMeet](https://img.shields.io/badge/GoogleMeet-00897B?style=for-the-badge&logo=Google%20Meet&logoColor=white)




## 화면 구성 📺
| 메인 페이지  |  화장품 입력페이지   |
| :-------------------------------------------: | :------------: |
|  <img width="329" src="https://github.com/Team-hwaE/Capston_hwa_E/assets/87376242/232152aa-44cd-4db2-a545-694d39501ab0"/> |  <img width="329" src="https://github.com/Team-hwaE/Capston_hwa_E/assets/87376242/ee75c05b-c120-469e-8aa9-1eb821e85ac5"/>|  
| 화장품 입력 팝업   |  카테고리 선택   |  
| <img width="329" src="https://github.com/Team-hwaE/Capston_hwa_E/assets/87376242/a7edb5cc-8dbc-4196-ac88-55fdc86a3cd3"/>   |  <img width="329" src="https://github.com/Team-hwaE/Capston_hwa_E/assets/87376242/8a01ccf4-9103-47b8-a358-1740c9aa6b09"/>     |
| 성분프렌즈 추천 결과   |  성분프렌즈 조회   |  
| <img width="329" src="https://github.com/Team-hwaE/Capston_hwa_E/assets/87376242/07442acb-79fb-4363-b166-9812fa73f355"/>   |  <img width="329" src="https://github.com/Team-hwaE/Capston_hwa_E/assets/87376242/aa15b29d-2faf-49b8-942c-f7f49bf235ad"/>     |
| 성분프렌즈 화장품 조회   |  에디터 추천 화면  |  
| <img width="329" src="https://github.com/Team-hwaE/Capston_hwa_E/assets/87376242/d5bd971a-7688-49e4-928a-43062056f461"/>   |  <img width="329" src="https://github.com/Team-hwaE/Capston_hwa_E/assets/87376242/0d9671da-223a-48b8-97ca-bf5220631031"/>     |
| 재추천화면   |  
| <img width="329" src="https://github.com/Team-hwaE/Capston_hwa_E/assets/87376242/e08369ca-24a7-42ca-8603-f5c2c73e130c"/>      |


---
## 주요 기능 📦

### ⭐️ 성분프렌즈 (유사 사용자 기반) 추천
- 메모리 기반 협업필터링 방식
- 성분 프렌즈가 매칭되면 해당 프렌즈의 화장품을 추천
  
### ⭐️ 에디터 (제품 성분 기반) 추천
- K평균 클러스터링 모델 활용
- 성분 벡터화 후 2차원 축소한 피처공간
- 유저 성분리스트와의 최소 유클리드 거리에 위치하는 성분 유사 제품 추천

---
## 아키텍쳐

### 디렉토리 구조
```bash
├── README.md : 리드미 파일
│
├── static/ : 백엔드
│   ├── font/ : 폰트
│   │   └── 롯데마트드림폰트.ttf 
│   │ 
│   ├── image/ : 이미지 저장 폴더
│   │   ├── bichon03.png : 성분프렌즈 프로필 이미지
│   │   ├── frenh03.png : 성분프렌즈 프로필 이미지
│   │   ├── welsh02.png : 성분프렌즈 프로필 이미지
│   └──── server.js : 서버 설정 정보 파일
│
├── templates/ : 프론트엔드 화면
│   ├── home.html : 메인 화면
│   ├── index.html : 하단바
│   ├── Insert_product.html : 화장품 입력화면
│   ├── Recommend.html : 성분프렌즈 추천화면
│   ├── Recommend2.html : 에디터 추천화면
│   ├── Restart.html : 재시작 요청 화면
│   ├── Select_category.html : 카테고리 선택화면
│   ├── Select_friend.html : 성분프렌즈 조회화면
│   └── View_friend.html : 성분프렌즈 화장품 조회화면
│   │
├── application.py : flask 어플리케이션 구현
├── database.py : mysql 연결정보, 조회 기능
├── clustering.ipnyb : 에디터 추천 기능 - 화장품 성분 기준 군집화 모델 생성 및 인덱스 추출 코드
│
├── product.csv : 화장품 이름/성분/카테고리 데이터
├── kms_model.pkl : 화장품 성분 군집 모델
├── new_X_data_fin.csv : 화장품 성분 벡터 데이터
└── mysql_table.zip : mysql table import 파일


```



