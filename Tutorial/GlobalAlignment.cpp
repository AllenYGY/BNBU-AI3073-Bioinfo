#include<vector>
#include<string>
#include<iostream>
#define int long long
#define endl '\n'
using namespace std;
 
int read(){
    int x = 0, f = 1;
    char ch = getchar();
    while (ch < '0' || ch > '9'){
        if (ch == '-')
            f = -1;
        ch = getchar();
    }
    while (ch >= '0' && ch <= '9')
        x = x * 10 + ch - '0', ch = getchar();
    return x * f;
}
 
void write(int x){
    if (x < 0)
        putchar('-'), x = -x;
    if (x > 9)
        write(x / 10);
    putchar(x % 10 + '0');
}
 
void solve(){
    string B="GGATGCA",A="GTCATCA";
    vector<vector<int>> dp(A.size()+1,vector<int>(B.size()+1,0));
    int match=5,mismatch=-2,penality=-6;
    for(int j=0;j<=B.size();j++){
        dp[0][j]=j*penality;
    }
    for(int i=0;i<=A.size();i++){
        dp[i][0]=i*penality;
    }
    for(int i=1;i<=A.size();i++){
        for(int j=1;j<=B.size();j++){
            if(A[i-1]==B[j-1]){
                dp[i][j]=dp[i-1][j-1]+match;
            }
            else{
                dp[i][j]=max(dp[i-1][j-1]+mismatch,max(dp[i-1][j]+penality,dp[i][j-1]+penality));
            }
        }
    }
    for(int i=0;i<=A.size();i++){
        for(int j=0;j<=B.size();j++){
            cout<<dp[i][j]<<" ";
        }
        cout<<endl;
    }
    return ;
}
 
signed main() {

    solve();
    return 0;
}