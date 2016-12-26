
//Implement the class Box  
//l,b,h are integers representing the dimensions of the box
class Box{
    private:
    int l;
    int b;
    int h;

// The class should have the following functions : 

// Constructors: 
    public:
 Box(){
     BoxesCreated++;
     l = 0;
     b = 0;
     h = 0;
 }
Box(int a,int x,int c){
    BoxesCreated++;
    l = a;
    b = x;
    h = c;
}
Box(Box& box){
    BoxesCreated++;
    l = box.getLength();
    b = box.getBreadth();
    h = box.getHeight();
}

// Destructor
 ~Box(){
     /*delete l;
     delete b;
     delete h;
     */
     BoxesDestroyed++;
     
 }
// {

// }

 int getLength(){
     return l;
 } // Return box's length
 int getBreadth (){
     return b;
 } // Return box's breadth
 int getHeight (){
     return h;
 }  //Return box's height
 long long CalculateVolume(){
     return (long)b * (long)h * (long)l;
 } // Return the volume of the box

//Overload operator < as specified
bool operator < (Box& c){
    return (l < c.getLength() ||(b < c.getLength() && l == c.getLength())|| (h < c.getHeight() &&b==c.getLength()&&l==c.getLength()));
}
};
//Overload operator << as specified
ostream& operator<<(ostream& out, Box B){
    out << B.getLength() << " "<< B.getBreadth() << " "<< B.getHeight();
    return out;
}
