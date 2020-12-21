import java.util.Scanner;

public class Baekjoon2871 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        StringBuffer str = new StringBuffer(scanner.next());
        scanner.close();

        String sk = "";
        String hw = "";
        while (str.length() > 0) {
            sk += str.charAt(str.length() - 1);
            str.deleteCharAt(str.length() - 1);
            int min_idx = str.length() - 1;
            char min_ch = 'z' + 1;
            for (int i = str.length() - 1; i >= 0; i--) {
                if (str.charAt(i) < min_ch) {
                    min_ch = str.charAt(i);
                    min_idx = i;
                }
            }
            hw += min_ch;
            str.deleteCharAt(min_idx);
        }
        
        if (hw.compareTo(sk) < 0){
            System.out.println("DA");
        }
        else {
            System.out.println("NE");
        }
        System.out.println(hw);
    }

}