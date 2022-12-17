/* Given two variables a & b, exchange their values without 
using a temporary variable.
source:: How to solve it by computer - p 47 prob 2.1.4*/

#include <iostream>

void swap(int &a, int &b){
    a = a - b;
    b = b + a;
    a = b - a;
    std::cout << "a is: " << a << " b is: " << b << std::endl;
    
    return;
}

int main(){

    int a {13};
    int b{5};

    swap(a,b);


    return 0; 
}