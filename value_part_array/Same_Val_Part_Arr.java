import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by shri on 2017/01/22.
 * Assume the input is an array of numbers 0 and 1. Here, a "Same Value Part Array" means a part of
 * an array in which successive numbers are the same.
 * For example, "11", "00" and "111" are all "Same Value Part Arrays" but "01" and "10" are not.
 * Given Above, implement a program to return the longest "Same Value Part Array" for any array
 * input. e.g. "011011100"
 */

public class Same_Val_Part_Arr {

    private static int[] same_val_part_arr(int[] sequence, int length){
        int[] longest = {0, 0};
        int[] curr = {0, 0};
        int first = 0;
        int last;
        for (int i=1; i<length; i++) {
            last = i;
            if (sequence[i] == sequence[i - 1]) {
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
        Scanner scan = new Scanner(System.in);
        String str = scan.next();
        int length = str.length();
        char[] charstr = str.toCharArray();
        int[] sequence = new int[length];
        for (int i=0; i<length; i++) {
            sequence[i] = Character.getNumericValue(charstr[i]);
        }
        System.out.println("Longest same value part is: "
                + Arrays.toString(same_val_part_arr(sequence, length)) + "\n");
    }
}
