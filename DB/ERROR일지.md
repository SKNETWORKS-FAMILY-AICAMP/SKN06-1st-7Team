# 🚨 ERROR 일지 🚨

### 📌 실수하기 좋은 아해들(MySQL과 Python)

<br/>

**배경**
> DB를 맡게 되면서 python 코드를 통해 MySQL에 접근하여 DB를 구축하였다. 그 과정에서 발생한 몇 가지 실수하기 좋은 에러이다.
> 
> 모쪼록 도움이 되길 바란다.😉

<br/>

**DB 권한 주기**
> **OperationalError: (1045, "Access denied for user 'skn06-1st-7team'@'localhost' (using password: YES)")**
> 
> 문제 : host에 DB 권한을 주지 않아서 생기는 문제이다. 프로젝트를 하게 되면 필히 DB를 만들게 되는데 그 때 꼭 host에게 권한을 주자.
> 
> 해결 : (MySQL) GRANT ALL PRIVILEGES ON (DB 이름).* TO 'host 이름'@'localhost';

<br/>

**예약어 피하기**
> **ProgrammingError: (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'usage' at line 1")**
> 
> 문제 : 'usage'가 MySQL에 예약어인지 모르고 테이블이름으로 지정해서 발생한 에러이다. 
> 
> 해결 : 예약어를 피해서 테이블 또는 데이터베이스 명을 지정해주어야 한다.
>
> 다음은 MySQL의 예약어를 모아둔 블로그이다. 한 번 방문해서 살피길 바란다. 
>
> https://solbel.tistory.com/1728 

<br/>

**제약 조건은 한 번만 정의하기**
> **ProgrammingError: (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'month int\n)' at line 4")**
> 
> 문제 : 이는 컬럼에서도 제약 조건을 선언하고, 아래에서 constraint 값으로도 같은 제약조건을 선언해서 발생한 에러이다. 
> 
> 해결 : 특별히 테이블을 정의할 때, 각 컬럼별로 제약조건이 한 번만 들어가있는지 확인해보아야 한다.
>
> 이는 자식테이블을 선언할 때도 마찬가지이다. 자식테이블에서 부모테이블과 join하려고 만든 컬럼에는 따로 제약조건을 주어서는 안 된다. 
>
> 초보의 실수이지만, 중요한 것 중에 하나인 것 같다. 

<br/>

**sql문 입력**
>**OperationalError: (1054, "Unknown column 'MY_id' in 'field list'")**
>
> 문제 : sql문을 잘못 입력해서 발생한 에러였다. 
> 
> 해결 : 본인이 작성한 코드를 다시 한 번 유심히 살핀다. 
>
> 테이블의 형식을 변환할 때가 발생할 수 있는데 그럴 때 놓치기 쉬운 실수 포인트이다.
>
> 테이블의 형식을 바꿀 때는 조금 더 주의깊게 살피자. 

<br/>

### 📌 번외

<br/>

**MySQL에서 테이블 행 만들기 수 제한 푸는 법**
> 에러는 나지 않아서 번외로 빼두었다.
>
> 분명히 에러는 나지 않았는데, 코드가 잘못된 줄 알고 한참을 살폈다.
>
> 코드는 에러가 없었다.
>
> MySQL이 잘못이렸다.
>
> ![image](https://github.com/user-attachments/assets/2ded1b45-3ac2-4b1a-811f-fedd270ec14c)
>
> 이미지 상단에 Don't limit 이라고 체크된 문구가 보이는가?
>
> 이 창을 통해 table에서 생성되는 행의 갯수를 제한할 수 있다. 10개부터 50000개까지 있다.
>
> 내가 의도한 행의 갯수는 30000개였는데, table에는 1000개 밖에 입력이 안 되어 애를 먹었다.
>
> 이 글을 보는 당신은 애를 덜 먹길 바란다. 

<br/>
