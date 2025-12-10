/**
 * Task 5: Java Car Class - Final Version with Javadoc
 */
public class CarFinal {
    String brand;   // Car manufacturer
    String model;   // Car model name
    int year;       // Manufacturing year

    /**
     * Constructor to initialize Car attributes
     */
    public CarFinal(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }

    /**
     * Display car details in required format
     */
    public void displayDetails() {
        System.out.println("Car Details:");
        System.out.println("Brand: " + brand);
        System.out.println("Model: " + model);
        System.out.println("Year: " + year);
    }

    public static void main(String[] args) {
        CarFinal car = new CarFinal("Toyota", "Corolla", 2020);
        car.displayDetails();
    }
}
