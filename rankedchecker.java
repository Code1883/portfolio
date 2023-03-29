import java.util.Scanner;

public class rankedchecker {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        
        System.out.println("How much RR do you have?");
        int rank = scanner.nextInt();
        

        if (rank > 650) {
            System.out.println("You are radiant.");
        } else if (rank <= 550 && rank >= 200) {
            System.out.println("You are Immortal 3.");
        }
        else {
            System.out.println("You are below Immortal 3.");
        }
    }
    
}
