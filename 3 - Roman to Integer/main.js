function roman(s) {
    const symbols = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000,
    }
    let total = 0
    for(let i = 0; i< s.length; i++) {
        const currentNumber = symbols[s[i]]
        const nextNumber = symbols[s[i + 1]]

        if(nextNumber > currentNumber) {
            total -= currentNumber
        } else {
            total += currentNumber
        }
    }

    return total
}

console.log(roman("IV"));