#include <iostream>
#include <vector>


std::vector<int> merge(std::vector<int> a, std::vector<int> b){
    int m {(int) a.size() - 1};
    int n {(int) b.size() - 1};
    std::vector<int> c {};

    // match inputs' lengths

    // check which vector has the largest value at the end
    // extend the other by this value
    /*
    a {1,3,8}
    b {2,4,5,6,17}
    m = 2, n = 4 
    a[m] = 8, b[n] = 17, 17 > 8 then:
    a[3] = 17
    
    */
    if(a[m] <= b[n]){
        a.push_back(b[n]);
    }
    else{
        b.push_back(a[m]);
    }

    int i {};
    int j {};
    int k {};
    int size {n+m+2};

    while(k < size){
        if(a[i] < b[j]){
            c.push_back(a[i++]);
        }
        else{
            c.push_back(b[j++]);
        }
        k++;
    }
    return c;
}

void print(std::vector<int> v){
    for(auto x:v){
        std::cout << x << " ";
    }
    std::cout << std::endl;
}
int main(){
    std::vector<int> a {1, 15, 16};
    std::vector<int> b {2, 4, 6, 8};

    std::vector<int> c = merge(a, b);
    print(c);


    std::vector<int> v1 {1,2,3};
    std::vector<int> v2 {4,5,6};

    print(merge(v1,v2));

    return 0;
}