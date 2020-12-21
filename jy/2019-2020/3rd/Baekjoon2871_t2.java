import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon2871_t2 {
    static int n = 0;
    static StringBuilder str = null;
    static StringBuilder sk = new StringBuilder();
    static StringBuilder hw = new StringBuilder();
    static String alpha = "abcdefghijklmnopqrstuvwxyz";

    public static void main(String[] args) {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        try {
            n = Integer.parseInt(bf.readLine());
            str = new StringBuilder(bf.readLine());
            bf.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        int cnt_idx = 0;
        int[] cnt = new int[26];

        StringBuilder sorted_str = str.reverse();
        for (int i = 0; i < str.length(); i++) {
            cnt[(sorted_str.charAt(i) - 'a')] += 1;
        }

        while (str.length() > 0) {
            char sk_char = sorted_str.charAt(0);
            sorted_str.deleteCharAt(0);
            sk.append(sk_char);
            cnt[sk_char - 'a'] -= 1;

            while (cnt[cnt_idx] == 0) {
                cnt_idx += 1;
            }
            char hw_char = alpha.charAt(cnt_idx);
            hw.append(hw_char);
            cnt[hw_char - 'a'] -= 1;
            for (int i = 0; i < sorted_str.length(); i++) {
                if (sorted_str.charAt(i) == hw_char) {
                    sorted_str.deleteCharAt(i);
                    break;
                }
            }
        }

        if (hw.compareTo(sk) < 0) {
            System.out.println("DA");
        } else {
            System.out.println("NE");
        }
        System.out.println(hw);
    }

}