#include <iostream>
#include <vector>


void sort(std::vector<int> &v){
    int idx {};
    int min {};
    int tmp {};
    
    for(int i {}; i < v.size(); i++){
        min = v[i];
        idx = i;
        for(int j = i+1; j < v.size(); j++){
            if(v[j] < min){
                min = v[j];
                idx = j;
            }
        }
        tmp = v[i];
        v[i] = min;
        v[idx] = tmp;
    }
    return;
}


void print(std::vector<int> v){
    for(auto const &x:v){
        std::cout << x << " ";
    }
    std::cout << std::endl;
}

int main(){

    std::vector<int> v1 {1,6,4,2};
    sort(v1);
    print(v1);


    return 0;
}