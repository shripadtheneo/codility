import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by shri on 2017/01/21.
 * Assume the input is an array of numbers 0 thru to 9. Here, an "Increasing Value Part Array" means
 * a part of an array in which successive numbers are increasing.
 * For example, "12", "49" and "678" are all "Increasing Value Part Arrays" but "53" and "22" are not.
 * Given Above, implement a program to return the longest "Increasing Value Part Array" for any array
 * input. e.g. "134297381"
 */

public class Inc_Val_Part_Arr {

    private static int[] incValPartArr(int[] sequence, int length){
        int[] longest = {0, 0};
        int[] curr = {0, 0};
        int first = 0;
        int last;
        for (int i=1; i<length; i++) {
            last = i;
            if (sequence[i] > sequence[i - 1]) {
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

    public static void main(String[] args) {
        System.out.println("Please input the array: ");
        Scanner scan = new Scanner(System.in);
        String str = scan.next();
        int length = str.length();
        char[] charstr = str.toCharArray();
        int[] sequence = new int[length];
        for (int i=0; i<length; i++) {
            sequence[i] = Character.getNumericValue(charstr[i]);
        }
        System.out.println("Longest increasing value part is: "
                + Arrays.toString(incValPartArr(sequence, length)) + "\n");
    }
}
