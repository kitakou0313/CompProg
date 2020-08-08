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

    int l[30][2] ={ 0 };

    cin >>N;
    for (int i = 0; i < N; i++) {
        cin >>l[i][0]>>l[i][1];
    }

    ll ans = INF;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int s = l[i][0];
            int o = l[j][1];

            ll tmpSum = 0;
            for (int k = 0; k < N; k++) {
                tmpSum += abs(l[k][0] - s) + abs(l[k][0] - l[k][1]) + abs(l[k][1] - o);
            }

            ans = min(ans, tmpSum);
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
