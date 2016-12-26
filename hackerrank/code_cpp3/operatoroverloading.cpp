std::ostream& operator << (std::ostream& outs, const Complex& x){
    outs << x.a << "+i" << x.b << endl;
    return outs;
}
Complex operator + (const Complex& a, const Complex& b){
    Complex ret =  Complex();
    ret.a = a.a + b.a;
    ret.b = a.b + b.b;
    return ret;
}