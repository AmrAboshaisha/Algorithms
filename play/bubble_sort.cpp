#include <iostream>
#include <vector>


void bsort(std::vector<int> &v){
    int i {};
    int n = (int) v.size();
    bool sorted {false};
    // while vector is not sorted
    while(!sorted){
        // set sorted = true
        sorted = true;
        // go through elements i -> n-2
        for(int j = i; j < n -1; j++){
            // for each element, check all adjacent pairs if sorted
            if(v[j] > v[j+1]){
                // if not sorted:
                //swap
                int tmp = v[j];
                v[j] = v[j+1];
                v[j+1] = tmp;
                // set sorted to false
                sorted = false;
            }
            
        }
        
    }
   
}



void print(std::vector<int> v){
    for(auto const &x:v){
        std::cout << x << " ";
    }
    std::cout << std::endl;
}



int main(){
    std::vector<int> v1 {5, 13, 8, 9, 2};
    bsort(v1);
    print(v1);
    return 0;
}