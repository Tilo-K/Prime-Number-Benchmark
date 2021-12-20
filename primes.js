function isPrime(n){
    for(var i = 2; i < n-1; i++){
        if(n % i == 0){
            return false;
        }
    }

    return true;
}

for(var i = 0; i < 100000; i++){
    if(isPrime(i)){
        process.stdout.write(i + "\r"); 
    }
}
console.log();
