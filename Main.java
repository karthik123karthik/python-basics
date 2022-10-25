

class Main{
    public static class Car{
    static int y = 5;
     int x = 10;
    }
    public static void main(String[]args){
        Car car1 = new Car();
        Car car2 = new Car();
        System.out.println(car1.x);
        System.out.println(car1.y);
        System.out.println(car2.x);
        System.out.println(car2.y);
        car1.y = 10;
        car1.x = 5;
        System.out.println(car1.x);
        System.out.println(car1.y);
        System.out.println(car2.x);
        System.out.println(car2.y);

    }
}
