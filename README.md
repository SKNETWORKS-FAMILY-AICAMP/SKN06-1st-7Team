## :ear: 팀 소개 :eyes:

### 📌 팀 명
SKN03-1st-3Team : 셋이서도 잘해요

<br/>

### 📌 팀 멤버
| 강채연 | 김동명 | 조하늘 |
|:----------:|:----------:|:----------:|
| <img width="120px" src="https://github.com/user-attachments/assets/0006ea2c-b76e-4756-a563-c563130d14c2" /> | <img width="120px" src="https://github.com/user-attachments/assets/43cfe23e-0562-4fac-929c-de5b07579dbd" /> | <img width="120px" src="https://github.com/user-attachments/assets/f3679466-0f72-4b21-8cc1-2c1b3d0394f0" /> |
| I'm lit | 동방의 crawler | DBDB딥 |

<br/><br/><br/>
## 🚗 서울시 자동차 등록 댓수와 사고율 🚗
### 📌 개발 기간
2024.10.11 ~ 2024.10.15 (총 5일)

<br/>

### 📌 프로젝트 개요
 서울시 내에 자치구별 자동차 등록 댓수와 자치구별 자동차 사고를 살펴보며 차가 많을수록 사고도 많은지 살펴보고자 한다. 
 
<br/>

### 📌 프로젝트 내용
**① 자치구별 자동차 증감율**

>  특정기간(2021.12. ~ 2023.12., 25개월) 동안에 자치구별 자동차 등록 증감을 한 눈에 보기 쉽게 나타낸다.
>  

**② 기간에 따른 자치구별 자동차 등록수**
> 기간을 설정할 수 있는 슬라이드바를 제공하여, 설정된 기간동안 선택한 자치구의 자동차 등록수를 그래프로 나타낸다. 
> 
> 이를 통해 자치구별 자동차 등록수도 비교할 수 있다. 또한 특정 기간동안의 증감율도 가시적으로 관찰할 수 있다. 

**③ 기간에 따른 자치구별 자동차 사고수**

> 자동차 등록수를 나타내는 그래프 상에 같은 자치구에서 일어난 자동차 사고수를 그래프로 나타낸다. 
> 
> 이를 통해 사용자는 자동차 등록수에 따라 발생하는 사고수를 직관적으로 파악할 수 있다. 

<br/>

### 📌 데이터베이스 (ERD)
| 자동차 등록 현황 DB | 자동차 사고수 DB |
|:----------:|:----------:|
| ![image](https://github.com/user-attachments/assets/6de6e280-b4cf-476e-9329-39b15d6e01e8) | ![image](https://github.com/user-attachments/assets/75a5d9e6-b7c7-4c18-afde-b32f636916d9) |

<br/>

### 📌 프로젝트 결과 (최종 streamlit UI)
| 기간 선택 슬라이드바 | 설명 | 
|:--:|--|
|![image](https://github.com/user-attachments/assets/d8227248-bd74-4396-a828-fba95411ca15) | 2022.12월부터 2023.12월까지 선택할 수 있는 슬라이드 바를 제공합니다. 기간에 따라 자동차 등록 횟수와 사고 횟수가 조정되어 나타납니다. |

<br/>

| 기간별 자동차 등록수와 증감 top5 | 설명 |
|:--:|--|
| ![image](https://github.com/user-attachments/assets/f6ec8cb0-6d44-4ca5-853e-1f88678ca647) | 자치구별 선택된 기간동안 차량 등록수가 증가한 상위 5개 구와 차량 등록수가 하락한 하위 5개 구의 자동차 등록수와 증감수를 표시합니다.  |

<br/>

| 자치구 선택 위젯 | 설명 |
|:--:|--|
|![image](https://github.com/user-attachments/assets/ffaef9c8-9312-4ada-9d9f-12c98aa24888) | 가시적인 그래프로 나타내기 위하여 특정 구를 선택하는 위젯을 제공합니다.  |

<br/>

| 자동차 등록수 및 사고 횟수 가시화 그래프 | 설명 |
|:--:|--|
|![image](https://github.com/user-attachments/assets/9bf5b0ed-c952-44cd-a06a-a97e0f892a2e) | 선택된 기간, 자치구의 자동차 등록수 추이와 사고 횟수를 나타내는 그래프를 제공합니다. |

- 끝 
