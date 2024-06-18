
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

> 웹 페이지 주소 : [http://ec2-3-80-183-199.compute-1.amazonaws.com:3000](http://ec2-3-80-183-199.compute-1.amazonaws.com:3000) <br>
* 테스트 계정 : demo@gmail.com 
> **로컬 주소** : [http://127.0.0.1:3000/]

## 프로젝트 소개

#### 스킨트리는 두 가지 화장품 추천 기능을 제공합니다.
1. 성분프렌즈 (유사 사용자 기반) 추천
2. 에디터 (제품 성분 기반) 추천


## How to build
#### AWS Server Requirements

- EC2 : Ubuntu server 22.04 LTS

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
```
1. mysql workbench에서 connection을 셋업한다 (Address 127.0.0.1/3000)
2. mysql_table.zip의 table 파일을 import해서 로컬에 데이터베이스를 세팅한다.
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
* Data Tables : <br>
  * user - userID, email, productID, fitness <br>
  * userIngredients - userID, ingredientsList <br>
  * product - ProductID, productName, productIngredients, categoryID, productCategory, translated_productName


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

### 1.	AWS EC2 생성

aws를 검색해서 홈페이지에 들어갑니다. 홈페이지에 들어가서 우측 상단에 있는 콘솔에 로그인을 눌러 로그인을 합니다. 로그인 후 콘솔 홈에서 EC2에 들어갑니다. EC2 페이지에서 인스턴스 시작 버튼을 누릅니다. <br>
#### (1)	인스턴스 이름 설정, AMI 선택<br>
이름을 설정해주고, AMI는 Ubuntu를 선택합니다. Ubuntu 중에도 많은 종류가 있지만, 무료로 이용할 것이라면 프리 티어 사용 가능을 선택해야 합니다. 프리 티어로 사용 가능한 Ubuntu Server 24.04 LTS를 선택합니다. 인스턴스 유형도 프리 티어 사용 가능한 t2.micro를 선택합니다. <br>
#### (2)	키 페어 등록<br>
키 페어가 없다면 생성해서 키 페어를 등록합니다. 생성한 키 페어는 인스턴스에 접속할 때마다 사용해야 하기에 위치와 비밀번호를 기억해 두어야 합니다.
인스턴스 이름 설정, AMI 선택 그리고 키페어 등록을 완료한 뒤 인스턴스 시작 버튼을 누르면 AWS EC2를 생성하게 됩니다. <br>

### 2. 인스턴스 연결<br><br>

#### (1)	접속할 주소 확인<br>

인스턴스 연결 페이지에 들어가서 하단에 있는 ‘예’ 링크를 복사하면 키페어 부분만 따옴표 처리로 되어있는데, 그 부분에 방금 전 생성한 키 페어 주소를 복사해서 링크를 수정해 넣으면 됩니다. 
<br>
#### (2)	터미널에서 접속<br>

터미널에서 ssh 명령문을 통해 AWS ubuntu server에 접속합니다. <br>

### 3. Ubuntu에 mySQL 설치+workbench와 연결<br><br>

 먼저 Ubuntu에 mySQL을 설치합니다. <br>

#### (1)	시스템 패키지 목록 업데이트<br>

인스턴스에 접속한 상태로 시스템 패키지 목록을 업데이트합니다. 
sudo apt update
(다음 명령문을 통해 시스템 패키지 목록을 업데이트할 수 있습니다. )
<br><br>
#### (2)	MySQL 서버 설치, 설정<br>

MySQL 서버 패키지를 설치합니다. 
sudo apt install mysql-server -y
(다음 명령문을 통해 MySQL 서버 패키지를 설치할 수 있습니다.)
설치를 완료한 후에는 외부에서 mySQL에 접근 가능하도록 설정해야 합니다.
터미널에서 MySQL 설정 파일을 엽니다. 이때 SSH로 연결된 상태에서 진행해야 합니다. <br><br>

~$ cd /etc/mysql/mysql.conf.d
$ sudo vi mysqld.cnf
터미널에서 해당 명령어를 입력하고 기존 bind-address가 127.0.0.1로 되어 있는 부분을 0.0.0.0으로 바꿔줍니다. 

‘i’를 눌러 입력 모드로 진입하고, [mysqld] 섹션 아래에 bind-address = 0.0.0.0으로 수정해둡니다.
입력이 끝난 뒤에는 ‘ESC’를 눌러 명령 모드로 돌아간 뒤 ‘:wq’를 입력하고 엔터 키를 눌러 파일을 저장하고 종료합니다. 

#### (3)	MySQL에서 사용할 계정 생성<br>

mysql -u root -p
을 통해 mySQL에 접속해 사용할 계정을 생성해 보겠습니다. 

create user ‘계정이름’@’localhost’ identified by ‘비밀번호’;
grant all privileges on *.* to '계정이름'@'localhost' with grant option;
flush privileges;

계정을 생성하고 권한을 부여합니다. 

#### (4)	인스턴스 보안 설정<br>

다시 aws에 돌아가서 인스턴스 보안 페이지로 갑니다. 인바운드 규칙 편집 버튼을 눌러 3306 포트로 접근이 가능하도록 합니다. 

규칙 추가 버튼을 누르고, MySQL/Aurora 3306 0.0.0.0/0를 선택하고, 규칙 저장 버튼을 누릅니다. 

#### (5)	Workbench 설정<br>

workbench를 열고 연결할 connection에서 Edit connection을 선택해주면 Manage Server Connections 창이 뜹니다. 

•	Connection Name: 원하는 이름으로 정해줍니다.<br>
•	Connection Method: Standard TCP/IP over SSH로 설정해줍니다.<br>
•	SSH Hostname: 인스턴스의 퍼블릭 IPv4 DNS를 입력해주면 됩니다.     <br>                                                                                      ( AWS에서 EC2>인스턴스>인스턴스 ID 누르면 인스턴스 요약 나오는데 거기에 퍼블릭 IPv4 DNS 있습니다.)<br>
•	SSH Username: ubuntu를 입력해줍니다.<br>
•	SSH Key File: 인스턴스 생성할 때 만들었던 키 체인 파일 넣어주면 됩니다.<br>
•	MySQL Hostname: 0.0.0.0 입력해줍니다.<br>
•	MySQL Server Port: 3306 입력해줍니다.<br>
•	Username: 아까 mySQL에서 생성한 계정의 '계정이름'을 넣어줍니다.<br>
•	password: Store in Keychain을 누르고 설정한 '비밀번호'를 입력합니다.<br>
입력하고 ok 버튼을 누른 뒤에 Test Connection 버튼을 누릅니다. 연결에 성공하면 창에 Successfully made the MySQL connection이 뜹니다. <br>



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
1. 웹 서버 접속 : http://127.0.0.1:3000 or http://ec2-3-80-183-199.compute-1.amazonaws.com:3000 주소 입력
2. 데모 계정 접속 : 'demo@gmail.com' 입력
3. 사용자의 화장품 입력/삭제 : ex) 겔랑 슈퍼 아쿠아 세럼 라이트
4. 카테고리 선택 : 스킨케어/선케어/클렌징/마스크팩
5. 추천 결과 조회

