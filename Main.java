class A {
    private int a;
 
    public A(int a) {
        this.a = a;
    }
 
    void print() {
        System.out.print(a + "a");
        System.out.println("1");
    }
}
 
class B extends A {
    private int b;
 
    B(int a, int b) {
        super(a);
        this.b = b;
    }
 
    void print() {
        super.print();
        System.out.print(b + "b");
        System.out.println("2");
    }
}
 
public class Main {
    public static void main(String[] args) {
        B obj = new B(10, 20);
        obj.print();
    }
}
