function slow_exp(base, exp){
    console.assert(exp > 0, "Exponent must be > 0");
    if (exp == 0){
        return 1;
    } else if (exp == 1) {
        return base;
    }
    return base * slow_exp(base, exp - 1);
}

function fast_exp(base, exp){
    console.assert(exp > 0, "Exponent must be > 0");
    if (exp == 0){
        return 1;
    } else if (exp == 1) {
        return base;
    } else if (exp == 2){
        return base * base;
    } else if (exp % 2 == 0){
        return fast_exp(fast_exp(base, exp/2), 2);
    } else {
        return base * fast_exp(base, exp-1);
    }
}

function time_it(funcToTime, ...names){
    console.time(funcToTime.name);
    console.log(funcToTime(...names));
    console.timeEnd(funcToTime.name);
}


time_it(slow_exp, 2, 1000);
time_it(fast_exp, 2, 1000);
