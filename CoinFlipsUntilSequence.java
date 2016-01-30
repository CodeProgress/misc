import java.util.ArrayList;
import java.util.Random;

public class CoinFlipsUntilSequence {
    private Random rand = new Random();
    private int numTrials;
    private int desiredSequenceLength;
    private ArrayList<Double> outcomes = new ArrayList<>();

    public CoinFlipsUntilSequence(int numTrials, int desiredSequenceLength){
        this.desiredSequenceLength = desiredSequenceLength;
        this.numTrials = numTrials;
    }

    public static void main(String[] args) {
        CoinFlipsUntilSequence cf = new CoinFlipsUntilSequence(10000, 10);
        cf.runSimulation();
        cf.printStatistics();
    }

    public double numTrialsUntilSuccessiveHeads(int desiredSequenceLength){
        double count = 0.;
        int numSuccessiveHeads = 0;

        while (numSuccessiveHeads < desiredSequenceLength) {
            count += 1;
            if (isHeads()) {
                numSuccessiveHeads++;
            } else {
                numSuccessiveHeads = 0;
            }
        }
        return count;
    }

    public boolean isHeads() {
        return rand.nextBoolean();
    }

    public void runSimulation(){
        outcomes.clear();
        for (int i = 0; i < numTrials; i++) {
            outcomes.add(numTrialsUntilSuccessiveHeads(desiredSequenceLength));
        }
    }

    public void printStatistics(){
        System.out.println(outcomes.stream().mapToDouble(a -> a).summaryStatistics());
    }
}
