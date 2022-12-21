/* insertion sort mimics the way card player sort their cards
 you keep a sorted part of ur cards and you examine the remaining 
 cards one by one and insert each into its proper place in the sorted part*/

 #include <iostream>
 #include <vector>

void isort(std::vector<int> &v){
    // first: find the minimum value and put in idx 0
    int min {v[0]};
    int idx {};
    
    for(int i {}; i < v.size(); i++){
        if(v[i] < min){
            min = v[i];
            idx = i;
        }
    }

    // swap 0 and min
    int tmp {v[0]};
    v[0] = min;
    v[idx] = tmp;

    // now first 2 positions are considered ordered, start from third
    // and check each idx to see where it will be inserted
    if(v.size() > 2){
        for(int j {2}; j < v.size(); j++){
            int k {j};
            while(v[k] < v[k-1] && k > 0){
                int tmp {v[k]};
                v[k] = v[k-1];
                v[k-1] = tmp;
                k--;
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
    std::vector<int> v1 {5, 13, 9, 8, 2};
    isort(v1);
    print(v1);
    return 0;
 }