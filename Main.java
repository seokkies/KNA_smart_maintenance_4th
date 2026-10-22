class A {
    int x = 10;

    A() {
        show();
        x += 5;
    }

    void show() {
        System.out.print("A" + x + " ");
    }
}

class B extends A {
    int y = 7;

    B() {
        y += x;
        show();
    }

    void show() {
        System.out.print("B" + x + "," + y + " ");
    }
}

public class Main {
    public static void main(String[] args) {
        A obj = new B();
        obj.show();
        System.out.print(obj.x);
    }
}