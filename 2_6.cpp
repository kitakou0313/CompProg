#include <iostream>
#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
#define MAXSIZE 10000000;

const int MAX = 510000;
const int MOD = 1000000007;
const long long INF = 1LL << 60;

ll dp[10001][1001] ={ 0 };

int main()
{
    int N;
    string S;

    cin >>N>>S;

    int ans = 0;

    for (int i = 0; i <=999; i++) {
        string code = to_string(i);
        if (i <= 9) {
            code = "0" + code;
            code = "0" + code;
        }
        else if (10 <= i && i <= 99) {
            code = "0" + code;
        }

        int codeInd = 0;
        for (int j = 0; j < N; j++) {
            if (code[codeInd] == S[j])codeInd++;
        }

        if (codeInd == 3) {
            ans++;
        }
    }

    cout <<ans<<endl;
}

/*Syakutori
while(cin >>b && b)){
      ll t = 1;
      long long int ansS = 1,ansT=0;
      long long int sum = 0;

      for(ll s = 1;s < 50000000;s++){

        while(t <  50000000 && sum+Rsum[t] < b){
          sum += Rsum[t];
          t++;
        }
        if(b == sum+Rsum[t]){
          if(ansT - ansS < t-s){
            ansS = s;
            ansT = t;
          }
          cout <<ansS<<" "<<ansT-ansS + 1<<endl;
          break;
        }
        if(t == s)++t;
        else sum -= Rsum[s];
        }
    }

//priority_queue<long long int,vector<long long int>, greater<long long int>> PQ;
//priority_queue<long long int> PQ1;

bool comp(const pair<int,int> a, const pair<int,int> b) {
    return a.second < b.second;
}

ll gcd(ll a,ll b){
  if(a%b == 0){
    return b;
  }else{
    return gcd(b,a%b);
  }
}


*/
