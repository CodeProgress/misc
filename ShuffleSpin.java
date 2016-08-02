import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

public class ShuffleSpin {
    private ArrayList<Integer> deck = new ArrayList<Integer>();

    private ArrayList<Integer> getDeck() {
        return deck;
    }
    private ShuffleSpin(Player player1, Player player2){
        deck = createDeck();
        Collections.shuffle(deck);
        player1.start();
        player2.start();
    }

    public static void main(String[] args) {
        Player player1 = new Player("Player 1");
        Player player2 = new Player("Player 2");
        ShuffleSpin game = new ShuffleSpin(player1, player2);
        System.out.println(game.getDeck().toString());
    }

    private static ArrayList<Integer> createDeck() {
        // Suits do not matter
        ArrayList<Integer> cardDeck = new ArrayList<Integer>();
        for (int i = 1; i <= 13; i++) {
            cardDeck.add(i);  // Hearts
            cardDeck.add(i);  // Spades
            cardDeck.add(i);  // Diamonds
            cardDeck.add(i);  // Clubs
        }
        return cardDeck;
    }
}


class Player extends Thread {

    private String playerName;

    Player(String name){
        playerName = name;
    }

    @Override
    public void run() {
        int numTurns = 4;  // to be unbounded and controlled by a while a loop until game is over
        int totalTimeSlept = 0;
        for(int i=0; i<numTurns; i++) {
            Random rand = new Random();
            int sleepMilliSeconds = rand.nextInt(100)+1;
            try {
                Thread.sleep(rand.nextInt(sleepMilliSeconds));
                // execute move
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(sleepMilliSeconds + " " + this.playerName);
            totalTimeSlept += sleepMilliSeconds;
        }
        System.out.println(this.playerName + " Total time: " + totalTimeSlept);
    }
}
