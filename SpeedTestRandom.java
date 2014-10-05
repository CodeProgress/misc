import java.util.Random;

public class SpeedTestRandom {

	public static void main(String[] args){
		int    randNum  = 0;
		int    numRands = 100000000;
		long   time     = System.nanoTime();
		long   duration;
		double seconds;
		
		Random rand = new Random();
		for (int i = 0; i < numRands; i++){
			randNum = rand.nextInt(numRands);
		}
		
		System.out.printf("Last random number generated: %d \n", randNum);
		duration = System.nanoTime() - time;
		seconds = duration/Math.pow(10, 9);
		System.out.printf("%f \t Total time in Seconds \n", seconds);
		System.out.printf("%,3d \t Random numbers generated per second \n", Math.round(numRands/seconds));
	}
	
}
