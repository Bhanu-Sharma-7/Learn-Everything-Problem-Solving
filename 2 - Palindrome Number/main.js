function Palindromex(x) {
    if(x < 0 || (x % 10 === 0 && x !== 0)) return false;

    var rev = 0
    while(x > rev) {
        let lastDigit = x % 10
        rev = rev * 10 + lastDigit
        x = Math.floor(x / 10)
    }
    return (x === rev || x === Math.floor(rev / 10))
}

console.log(Palindromex(11))