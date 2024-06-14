
![main](https://github.com/Team-hwaE/Capston_hwa_E/assets/87376242/a83f0679-d86a-4aeb-be03-911cb583fe07)

# skinTree : 협업필터링과 머신러닝을 활용한 성분 맞춤형 화장품 추천 서비스

> **이화여자대학교 컴퓨터공학전공 캡스톤디자인프로젝트 : 2023-9 ~ 2024-5**
<br>
스킨트리는 기존에 잘 맞았던 화장품을 입력하면 자동으로 개인 성분리스트를 생성하고, 당신의 성분프렌즈를 찾아 화장품을 추천해주는 서비스입니다.
<br>

## 🔧 팀원 소개

|      정다희       |          안민영         |       임수화         |                                                                                                               
| :------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | 
|   <img width="160px" src="https://github.com/Team-hwaE/Capston_hwa_E/assets/87376242/fc8c4c59-d033-4c38-ad18-7e2d6daeb9e9" />    |                      <img width="160px" src="https://github.com/Team-hwaE/Capston_hwa_E/assets/87376242/0d7710c7-abfd-4fba-b383-8a2579a777a0" />    |                   <img width="160px" src="https://github.com/Team-hwaE/Capston_hwa_E/assets/87376242/89aa9120-c3fe-490c-a1e1-4df72578488e"	/>   |
|   [@da2mon](https://github.com/da2mon)   |    [@minzer01](https://github.com/minzer01)  | [@aihamster](https://github.com/aihamster)  |
| 프론트엔드 | 백엔드 | 머신러닝 |



## 배포 주소

> **웹 페이지 주소 ** : [http:~~~](http://~~/) <br>
* 테스트 계정 : demo@gmail.com 
> **로컬 주소** : [http://127.0.0.1:3000/]

## 프로젝트 소개

#### 스킨트리는 두 가지 화장품 추천 기능을 제공합니다.
1. 성분프렌즈 (유사 사용자 기반) 추천
2. 에디터 (제품 성분 기반) 추천


## How to build
#### AWS Server Requirements

- EC2 : Ubuntu 버전명

#### Installation
``` bash
$ git clone https://github.com/Team-hwaE/Capston_hwa_E.git
$ cd Capston_hwa_E
```
#### Backend
```
$ pip3 install flask 
$ pip3 install pymysql
$ pip3 install numpy pandas matplotlib scikit-learn
```

#### Frontend
```
$ python3 application.py
```

---

## Stacks 🐈

### Environment
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)   

### Development
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=Javascript&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

### Database
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)

### Machine Learning
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

### Communication
![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white)

### Collect data
[Incidecoder](https://incidecoder.com/) <br>
[대한화장품협회 성분사전](https://kcia.or.kr/cid/main/)

* Schema: The schema includes tables for users, Projects, userIngredients and product. <br>
* Data Tables - <br>
  user: userID, email, productID, fitness <br>
  userIngredients: fields like userID, ingredientsList <br>
  product : fields like ProductID, productName, productIngredients, categoryID, productCategory, traslated_productName


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
### 기능 흐름도
<img width="825" alt="image" src="https://github.com/Team-hwaE/Capston_hwa_E/assets/87376242/80f57382-6b2e-4ed5-b702-80fcc222bcd3">

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
## 서브 기능 📦

### ⭐️ 기존 화장품 입력
- 사용자가 입력한 화장품을 user table 에서 조회
- 입력 팝업창에서 화장품 이름을 검색하면 적합/부적합 여부를 선택하여 등록함
- 추가/삭제 기능
- 추가/삭제가 일어나면 성분리스트가 업데이트됨
```
@application.route("/insert_product", methods=["POST"])
@application.route("/delete_product/<int:product_id>")
def update_user_ingredient():
```
  
### ⭐️ 성분 프렌즈 화장품 조회
- 성분프렌즈 추천 결과 화면이 출력된 경우, 3명의 성분 프렌즈가 검색됨을 의미
- 해당 프렌즈들이 입력한 화장품 목록을 조회하는 기능
```
@application.route('/Select_friend')
@application.route('/View_friend/<int:userID>')
```
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
│   └────── welsh02.png : 성분프렌즈 프로필 이미지
│   
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
│   
├── application.py : flask 어플리케이션 구현
├── database.py : mysql 연결정보, 조회 기능
├── clustering.ipnyb : 에디터 추천 기능 - 화장품 성분 기준 군집화 모델 생성 및 인덱스 추출 코드
│
├── product.csv : 화장품 이름/성분/카테고리 데이터
├── kms_model.pkl : 화장품 성분 군집 모델
├── new_X_data_fin.csv : 화장품 성분 벡터 데이터
└── mysql_table.zip : mysql table import 파일


```
<img width="872" alt="스크린샷 2024-06-14 오후 7 46 34" src="https://github.com/Team-hwaE/Capston_hwa_E/assets/87376242/dcf46ab2-1e97-48c6-adf2-13619567762b">

---
## How to Install (AWS 설정 과정 설명)
아래는 예시임
Provision AWS Resources:

Create an EC2 instance for the application server.
Set up an RDS instance for the database.
Configure S3 buckets for file storage if needed.
Use AWS Elastic Beanstalk or ECS for containerized deployments.
Deploy Application:

SSH into your EC2 instance.
Clone the repository and install dependencies.
Build the application for production.
Set up environment variables (e.g., database connection strings, AWS keys).
Run the application on the EC2 instance.
Set Up Networking:

Configure security groups to allow traffic on necessary ports.
Set up a load balancer if needed.
Point your domain to the EC2 instance using Route 53.
Automate with CI/CD:

---
## Description of Sample Data
1. demo 사용자
   선택 제품 : loccitane-immortelle-precious-cream, summecosmetics-s-cell-c-antiage-double-action-cream
2. 유사 사용자 1
   선택 제품 : loccitane-immortelle-precious-cream, summecosmetics-s-cell-c-antiage-double-action-cream, ponds-nourishing-moisturizing-cream
3. 유사 사용자 2
   선택 제품 : loccitane-immortelle-precious-cream, summecosmetics-s-cell-c-antiage-double-action-cream, senka-aqua-bright-glow-gel-cream
4. 유사 사용자 3
   선택 제품 : loccitane-immortelle-precious-cream, summecosmetics-s-cell-c-antiage-double-action-cream, natura-bisse-inhibit-tensolift-neck-cream
---
## How to Test
1. 웹 서버 접속 : 주소 입력
2. 데모 계정 접속 : 'demo@gmail.com' 입력
3. 사용자의 화장품 입력/삭제 : ex) 겔랑 슈퍼 아쿠아 세럼 라이트
4. 카테고리 선택 : 스킨케어/선케어/클렌징/마스크팩
5. 추천 결과 조회

