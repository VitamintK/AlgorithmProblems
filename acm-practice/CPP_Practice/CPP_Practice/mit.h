char chars[];
int a;
int b;
int c;
int d;
int e;
int f;
int g;
int h;
int i;
int j;

int lhs[20000][6];
int rhs[20000][6];
int evn[20000][6];
int lc = 0;
int rc = 0;
int ec = 0;
int storage[12];
#include<iostream>
void mit(){
	//for (int l = 65; l < 123; l++){
		//for (int k = 65; k < 123; k++){
			//for (int j = 65; j < 123; j++){
				//for (int i = 65; i < 123; i++){
					//for (int h = 65; h < 123; h++){
						//for (int g = 65; g < 123; g++){
							for (int f = 65; f < 123; f++){
								std::cout << "f" << f << std::endl;
								for (int e = 65; e < 123; e++){
									//std::cout << "e " << e << std::endl;
									for (int d = 65; d < 123; d++){
										for (int c = 65; c < 123; c++){
											for (int b = 65; b < 123; b++){
												for (int a = 65; a < 123; a++){

													if ((6 * a + 5 * b + 4 * c + 3 * d + 2 * e + 1 * f) % 255 == 208 && (a + b + c + d + e + f) % 255 == 110){
														//std::cout << a << b << c << d << e << std::endl;
														lhs[lc][0] = a;
														lhs[lc][1] = b;
														lhs[lc][2] = c;
														lhs[lc][3] = d;
														lhs[lc][4] = e;
														lhs[lc++][5] = f;
														
													}
													/*if ((6 * a + 5 * b + 4 * c + 3 * d + 2 * e + 1 * f) % 255 == 0 && (a + b + c + d + e + f) % 255 == 0){
														//std::cout << a << b << c << d << e << std::endl;
														evn[ec][0] = a;
														evn[ec][1] = b;
														evn[ec][2] = c;
														evn[ec][3] = d;
														evn[ec][4] = e;
														evn[ec++][5] = f;

													}*/
													if ((6 * a + 5 * b + 4 * c + 3 * d + 2 * e + 1 * f) % 255 == 240 && (a + b + c + d + e + f) % 255 == 13){
														//std::cout << a << b << c << d << e << std::endl;
														//rhs[rc][0] = a;
														//rhs[rc][1] = b;
														//rhs[rc][2] = c;
														//rhs[rc][3] = d;
														//rhs[rc][4] = e;
														//rhs[rc++][5] = f;
														for (int i=0; i < lc; i++){
															int h0 = lhs[i][0];
															int h1 = lhs[i][2];
															int h2 = lhs[i][4];
															if ((6 * h0 + 5 * h1 + 4 * h2 + 3 * a + 2 * c + 1 * e) % 255 == 0 && (h0 + h1 + h2 + a + c + e) % 255 == 0){
																std::cout << lhs[i][0] << ' ' << lhs[i][1] << ' ' << lhs[i][2] << ' ' << lhs[i][3] << ' ' << lhs[i][4] << ' ' << lhs[i][5] << ' ' << a << ' ' << b << ' ' << c << ' ' << d << ' ' << e << ' ' << f << std::endl;
																int win;
																std::cin >> win;
															}
														}
													}

												}
											}
										}
									}
								}
							//}
						//}
					//}
				//}
			//}
		//}
	}
							//for (int i = 0; i < lc;i++){
						//		for (int j )
	//}
}
