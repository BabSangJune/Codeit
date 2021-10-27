// 여기에 코드를 입력해 주세요.
function teraToGiga(num) {
  console.log(num + "TB는")
  console.log(num * 1024 + "GB 입니다.")
}

function teraToMega(num) {
  console.log(num + "TB는")
  console.log(num * 1024 * 1024 + "MB 입니다.")
}

// TB -> GB 테스트
teraToGiga(2);
// TB -> MB 테스트
teraToMega(2);