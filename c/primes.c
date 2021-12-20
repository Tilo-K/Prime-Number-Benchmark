#include <stdio.h>

int isPrime(int n){
    for(int i = 2; i < n-1; i++){
        if(n % i == 0){
            return 0;
        }
    }

    return 1;
}

int main(){
    for(int i = 0; i < 100000; i++){
        if(isPrime(i)){
            printf("%d\r", i);
        }
    }

    puts("\n");
}