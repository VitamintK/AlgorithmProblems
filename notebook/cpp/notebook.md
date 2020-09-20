## Numbers:

``` c++
vector<pair<ll, int>> prime_factorize(ll n) {
    vector<pair<ll, int>> factorization;
    ll x = n;
    for(ll i =2; i*i <= n; i++){
        if (x%i == 0){
            int cnt = 0;
            while(x%i == 0){
                cnt++;
                x/=i;
            }
            factorization.push_back(make_pair(i, cnt));
        }
    }
    if (x > 1) {
        factorization.push_back(make_pair(x, 1));
    }
    return factorization;
}
```

``` c++
set<ll> get_divisors(ll n) {
    set<ll> divisors;
    for(ll i =2; i*i <= n; i++){
        if(n%i == 0){
            divisors.insert(i);
            divisors.insert(n/i);
        }
    }
    divisors.insert(n);
    return divisors;
}
```

