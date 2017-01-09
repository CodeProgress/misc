import java.io.*;
import java.util.*;

public class LeftRotatedArray {

    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        
        int arrayLength = scan.nextInt();
        int numRotations = scan.nextInt();
       
        int[] arr = new int[arrayLength];
        
        int indexAfterRotation = arrayLength - numRotations % arrayLength;
        while (scan.hasNext()){ 
            arr[indexAfterRotation] = scan.nextInt();
            indexAfterRotation++;
            indexAfterRotation %= arrayLength;
        }
        
        Arrays.stream(arr).forEach(x -> System.out.print(x + " "));
    }
}