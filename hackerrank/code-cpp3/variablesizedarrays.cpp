    long N;
    long Q;
    cin >> N;
    cin >> Q;
    long k;
long n;
    int** ns = new int*[N];
    for(long i = 0; i < N; i++){
        cin >> k;
        ns[i] = new int[k];
        for(long x= 0; x < k; x++){
            cin >> n;
            ns[i][x] = n;
        }
    }
int a;
int e;
    for(long j = 0; j < Q; j++){
        cin >> a;
        cin >> e;
        cout << ns[a][e] << endl;
    }
	return 0;
}
