import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by shri on 1/25/17.
 */
public class LongestArray {

    //For finding the longest array
    private static char[] longestArray(char[] sequence, int length, String check){
        int[] longest = {0, 0};
        int[] curr = {0, 0};
        int first = 0;
        int last;
        for (int i=1; i<length; i++) {
            last = i;
            if (comparison(sequence[i], sequence[i-1], check)) {
                curr[0] = first;
                curr[1] = last;
            }
            else {
                first = i;
            }

            if ((curr[1] - curr[0]) > (longest[1] - longest[0])) {
                longest[0] = curr[0];
                longest[1] = curr[1];
            }
        }

        return Arrays.copyOfRange(sequence, longest[0], longest[1] + 1);
    }

    //For doing the comparison
    private static boolean comparison(char char1, char char2, String check) {
        if (check.equals("Similar char")) {
            return char1 == char2;
        }
        else if (check.equals("Increasing int")) {
            return Character.getNumericValue(char1) > Character.getNumericValue(char2);
        }
        else if (check.equals("Similar bool")) {
            return char1 == char2;
        }

        return false;
    }

    public static void main(String args[]) {

        Scanner scan = new Scanner(System.in);
        System.out.println("Please select the type of array manipulation you want to perform: ");
        System.out.println("1. Increasing Value Part Array");
        System.out.println("2. Same Value Part Array");
        System.out.println("3. Same Character Part Array");
        String check = "";
        int selection = scan.nextInt();


        System.out.println("Please input the array: ");
        String str = "";

        if (selection == 1) {
            check = "Increasing int";
            str = scan.next();
            if (!str.chars().allMatch(Character::isDigit)) {
                System.out.println("Please enter the correct array");
                System.exit(1);
            }
        }
        else if (selection == 2) {
            check = "Similar bool";
            str = scan.next();
            if (!str.matches("[01]+")) {
                System.out.println("Please enter the correct array");
                System.exit(1);
            }
        }
        else if (selection == 3) {
            check = "Similar char";
            str = scan.next();
            if (!str.chars().allMatch(Character::isLetter)) {
                System.out.println("Please enter the correct array");
                System.exit(1);
            }
        }

        int length = str.length();
        char[] sequence = str.toCharArray();

        System.out.println("Longest same value part is: "
                + Arrays.toString(longestArray(sequence, length, check)) + "\n");
    }

}
