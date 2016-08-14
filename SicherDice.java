import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.concurrent.ThreadLocalRandom;


public class SicherDice {
    private static ArrayList<Integer> normalDie = new ArrayList<Integer>(Arrays.asList(1,2,3,4,5,6));
    private static ArrayList<Integer> normalOutcomes = createOutcome(normalDie, normalDie);
    private static int[] expectedOutcomeHistogram = createHistogram(normalOutcomes);

    public static void main(String[] args){
        for (int i = 0; i < 1000000; i++){
            ArrayList<Integer> die1 = createRandomDie(1, 8); // new ArrayList<Integer>(Arrays.asList(1,2,2,3,3,4));
            ArrayList<Integer> die2 = createRandomDie(1, 8); // new ArrayList<Integer>(Arrays.asList(1,3,4,5,6,8));
            if (IsOutcomeEquivalentToNormalDice(createOutcome(die1, die2))){
                // will print normal and sicher configurations
                System.out.println(die1 + " " + die2);
            }
        }
    }

    private static boolean IsOutcomeEquivalentToNormalDice(ArrayList<Integer> outcome) {
        int[] outcomeHistToTest = createHistogram(outcome);
        if (outcomeHistToTest.length != expectedOutcomeHistogram.length) return false;

        for (int i = 0; i <outcomeHistToTest.length; i++){
            if (outcomeHistToTest[i] != expectedOutcomeHistogram[i]) return false;
        }
        return true;
    }

    private static ArrayList<Integer> createOutcome (ArrayList<Integer> die1, ArrayList<Integer> die2) {
        ArrayList<Integer> outcomes = new ArrayList<Integer>();
        for (int faceValue1 : die1) {
            for (int faceValue2 : die2) {
                outcomes.add(faceValue1 + faceValue2);
            }
        }
        return outcomes;
    }

    private static int[] createHistogram(ArrayList<Integer> outcomes){
        int[] hist = new int[Collections.max(outcomes)+1];
        for (int value : outcomes){
            hist[value] += 1;
        }
        return hist;
    }

    private static ArrayList<Integer> createRandomDie(int min, int max){
        ArrayList<Integer> die = new ArrayList<Integer>();
        for (int i = 0; i < 6; i++){
            die.add(randInt(min, max));
        }
        return die;
    }

    private static int randInt(int min, int max) {
        return ThreadLocalRandom.current().nextInt(min, max + 1);
    }

}
