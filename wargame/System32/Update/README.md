# [System32] Update - Writeup

이 문제도 워밍업 문제처럼 html 소스코드를 보면 flag가 나와있다.

```
-- 생략 --
          <a id="ref" data-translate="_win10workingonupdates">Working on updates </a> &nbsp;<a id="timer">0%</a> <span data-translate="_win10percent">complete.</span><br
          /><span data-translate="_win10donotturnoff">Don't forget system32.kr We will update homepage.</span>
        </div>
        <div id="bottom" data-translate="_win10willrestart">Contact : pental@system32.kr / Thanks and Sorry!</div>
        <!-- Flag{We_will_update_sorry!} -->
      </div>
    </div>
  </div>
-- 생략 --
```

___

## Answer

flag: `We_will_update_sorry!`