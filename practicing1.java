import java.util.Scanner;

public class practicing1 { // Scanner Class importieren

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in); // Scanner Objekt erstellen
        
        System.out.println("Was ist deine Lieblingszahl? "); // Welcher Input angezeigt wird
        int lieblingszahl =  scanner.nextInt(); // User Input lesen & in welchem Daten Typ es gelesen wird.
        scanner.nextLine();
        System.out.println("Was ist dein Lieblingsessen? ");
        String lieblingsessen = scanner.nextLine();

        System.out.println("Deine Lieblingszahl ist: " + lieblingszahl); // Output des User Input anzeigen lassen.
        System.out.println("Dein Lieblingsessen ist: "+ lieblingsessen);

    }
    
}
