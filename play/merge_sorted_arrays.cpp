#include <iostream>

void merge(int A[4], int B[4]){
    int i {};
    int j {};
    int k {};
    int C [8] {};

    while(k < 8){
        if(A[i] <= B[j]){
            C[k] = A[i];
            i++;
            std::cout << "i is: " << i << std::endl;
        }
        else{
            C[k] = B[j];
            j++;
            std::cout << "j is: " << j << std::endl;
        }

        if(k == 7){
            if(A[i] >= B[j]){
                C[k] = A[i];
            }
            else{
                C[k] = B[j];
            }
        }
        k++;


    }

    for(int i {}; i < 8; i++){
        std::cout << C[i] << " ";
    }
    std::cout << std::endl;

}





int main(){
    int A[] {1,4,5,8};
    int B[] {2,4,5,7};
    merge(A,B);
    return 0;
}