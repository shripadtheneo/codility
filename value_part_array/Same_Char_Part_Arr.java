import java.util.Arrays;


/**
 * Created by shri on 2017/01/22.
 * Assume the input is an array of alphabets, both capital and small, A thru to Z and a thru to z.
 * Here, a "Same Character Part Array" means a part of an array in which successive characters are
 * same(case sensitive).
 * For example, "aa", "AA", "bb" and "BB" are all "Same Character Part Arrays" but "aA" "ab" and
 * "Ab" are not.
 * Given Above, implement a program to return the longest "Same Character Part Array" for any array
 * input. e.g. "AaBBBcC"
 */

public class Same_Char_Part_Arr {

    private static char[] same_char_part_arr(char[] sequence, int length){
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
        char[] sequence = {'A', 'a', 'B', 'B', 'B', 'c', 'C'};
        int length = sequence.length;
        System.out.println("Longest same value part is: "
                + Arrays.toString(same_char_part_arr(sequence, length)) + "\n");
    }
}
