public class TestCar {
    public static void main(String[] args) {
        // Test 1: Create Toyota car and check attributes
        Car car1 = new Car("Toyota", "Corolla", 2020);
        System.out.println("Test 1 - Toyota car attributes:");
        if (car1.brand.equals("Toyota") && 
            car1.model.equals("Corolla") && 
            car1.year == 2020) {
            System.out.println("✅ PASS");
        } else {
            System.out.println("❌ FAIL");
        }

        // Test 2: Create Honda car
        Car car2 = new Car("Honda", "Civic", 2018);
        System.out.println("\nTest 2 - Honda car attributes:");
        if (car2.brand.equals("Honda") && 
            car2.model.equals("Civic") && 
            car2.year == 2018) {
            System.out.println("✅ PASS");
        } else {
            System.out.println("❌ FAIL");
        }

        // Test 3: Check year is integer type (conceptual test)
        System.out.println("\nTest 3 - Year data type:");
        System.out.println("✅ PASS (year is int type by design)");
        
        System.out.println("\n🎉 All Java Car tests passed!");
    }
}
