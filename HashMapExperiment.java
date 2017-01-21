
import java.util.concurrent.ConcurrentHashMap;

public class HashMapExperiment {
    public static void main(String[] args) {
        ConcurrentHashMap<Integer, Integer> sqMap = new ConcurrentHashMap<>();
        for (int i = 0; i <10; i++){
            sqMap.put(i, i*i);
        }
        System.out.println(sqMap.toString());

        // recursive test
        String test = "12345";
        System.out.println(reverse(test));
        System.out.println(reverse2(test));
    }
    // recursive
    private static String reverse (String str){
        if (str.length() <= 1){
            return str;
        }
        return str.charAt(str.length()-1) + reverse(str.substring(0, str.length() - 1));
    }
    // recursive
    private static String reverse2 (String str){
        if (str.length() <= 1){
            return str;
        }
        return reverse2(str.substring(1)) + str.charAt(0);
    }

}
