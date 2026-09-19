import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int check = 1;
    Scanner scan = new Scanner(System.in);
    while(check == 1) {
      int jscore = 0, sscore = 0, dscore = 0;
      String ext = "";
      String grade= "";

      System.out.println("Input:\nJava Score:");
      jscore = scan.nextInt();
      System.out.println("C Score:");
      sscore = scan.nextInt();
      System.out.println("Database Handling Score:");
      dscore = scan.nextInt();

      double score = (jscore + sscore + dscore) / 3.0;
      int choiceScore = ((jscore + sscore + dscore) / 3)/10;

      switch (choiceScore) {
        case 10, 9:
          grade = "A";
          break;
        case 8:
          grade = "B";
          break;
        case 7:
          grade = "C";
          break;
        default:
          grade = "F";
      }

      if(score >= 0 && score <= 100) {
        System.out.println("Grade: " + grade);
        System.out.println("Explanation: The average of the student is " + String.format("%.3f", score) + " so the student's grade is " + grade);
      }

      System.out.println("Do you want to continue: (YES / NO)");
			ext = scan.next();
			if(ext.equalsIgnoreCase("NO")) {
        System.out.println("Program terminated.\nThank you!");
				check--;
			}
      System.out.println("\n");
    }
  }
}
