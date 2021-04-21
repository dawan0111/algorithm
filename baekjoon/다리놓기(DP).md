# 다리놓기
`DP`

다리놓는 문제 

```cpp
#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int c, n, m;
    cin >> c;
    
    long dp[31][31];
    
    for (int i = 1; i <= 30; i++) {
        for (int j = i; j <= 30; j++) {
            if (i == 1) {
                dp[i][j] = j;
            } else {
                dp[i][j] = 0;
                for (int k = i; k <= j; k++) {
                    dp[i][j] += dp[i - 1][k - 1];
                }
            }
        }
    }
    
    for (int i = 0; i < c; i++) {
        cin >> n >> m;
        cout << dp[n][m] << endl;
    }
    
    return 0;
}

```
