
import java.util.*;
import java.util.concurrent.atomic.AtomicIntegerArray;

public class ShuffleSpin {
    final int NUM_CARDS_IN_PILE = 4;
    final int NUM_PLAYER_PILES = 6;
    private ArrayList<Integer> deck = new ArrayList<Integer>();
    private AtomicIntegerArray communityPile = new AtomicIntegerArray(4);
    private Player player1;
    private Player player2;
    private Random rand = new Random();

    private ShuffleSpin(){
        deck = createDeck();
        Collections.shuffle(deck);
        for (int i = 0; i < NUM_CARDS_IN_PILE; i++){
            communityPile.set(i, deck.get(i));
        }
    }

    public static void main(String[] args) {
        ShuffleSpin game = new ShuffleSpin();
        Player player1 = new Player(game, "Player 1");
        Player player2 = new Player(game, "Player 2");
        game.addPlayers(player1, player2);
        game.startGame();
    }

    private void addPlayers(Player player1, Player player2){
        this.player1 = player1;
        this.player2 = player2;
        for (int i = 0; i < NUM_PLAYER_PILES; i++){
            this.player1.addPileToUncompletedPiles(getPileOfFourFromDeck());
            this.player2.addPileToUncompletedPiles(getPileOfFourFromDeck());
        }
    }

    private void startGame(){
        this.player1.start();
        this.player2.start();
    }

    private static ArrayList<Integer> createDeck() {
        // Suits do not matter, just use the value
        ArrayList<Integer> cardDeck = new ArrayList<Integer>();
        for (int i = 1; i <= 13; i++) {
            cardDeck.add(i);  // Hearts
            cardDeck.add(i);  // Spades
            cardDeck.add(i);  // Diamonds
            cardDeck.add(i);  // Clubs
        }
        return cardDeck;
    }

    private ArrayList<Integer> getPileOfFourFromDeck(){
        ArrayList<Integer> pile = new ArrayList<Integer>();
        for (int i = 0; i < NUM_CARDS_IN_PILE; i++){
            pile.add(deck.remove(deck.size()-1));
        }
        return pile;
    }

    boolean isCompletedPile(ArrayList<Integer> pile){
        Integer firstVal = pile.get(0);
        for (int i = 1; i < pile.size(); i++){
            if (!firstVal.equals(pile.get(i))){
                return false;
            }
        }
        return true;
    }

    Integer getAndSetRandomValueOfCommunityPile(int newValue){
        return this.communityPile.getAndSet(rand.nextInt(NUM_CARDS_IN_PILE), newValue);
    }

    boolean compareAndUpdateCommunityPile(int index, int expected, int update){
        return this.communityPile.compareAndSet(index, expected, update);
    }
}

class Player extends Thread {

    private String playerName;
    private ArrayList<ArrayList<Integer>> uncompletedPiles = new ArrayList<ArrayList<Integer>>();
    private ArrayList<ArrayList<Integer>> completedPiles = new ArrayList<ArrayList<Integer>>();
    private ShuffleSpin game;
    private Random rand = new Random();

    void addPileToUncompletedPiles(ArrayList<Integer> pile) {
        this.uncompletedPiles.add(pile);
    }

    Player(ShuffleSpin game, String name){
        playerName = name;
        this.game = game;
    }

    private boolean isGameOver(){
        return completedPiles.size() == this.game.NUM_PLAYER_PILES;
    }

    @Override
    public void run() {
        int numTurns = 0;
        long startTime = System.nanoTime();
        System.out.println(playerName + " Starting! Nanosecond timestamp: " + startTime);
        while (!isGameOver()) {
            makeMove();
            numTurns++;
        }

        System.out.println(this.playerName
                + " Done! Num turns: "
                + numTurns + " in "
                + (System.nanoTime()-startTime)/1e9
                + " seconds."
        );
    }

    private void orderPileByCardFrequency(ArrayList<Integer> pile){
        // sorts pile from least frequent to most frequent to enable more efficient pop from ArrayList
        final HashMap<Integer, Integer> hist = new HashMap<Integer, Integer>();
        for (int card : pile){
            Integer previous = hist.get(card);
            hist.put(card, previous == null ? 1 : previous + 1);
        }
        Collections.sort(pile, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return hist.get(o2) - hist.get(o1);
            }
        });
    }

    private void cleanUpCompletedPile(int indexOfPile, ArrayList<Integer> pile){
        completedPiles.add(pile);
        uncompletedPiles.remove(indexOfPile);
    }

    private void randomlySwapACardIfPileNotComplete(int indexOfPile, ArrayList<Integer> pile){
        if (!this.game.isCompletedPile(pile)) {
            orderPileByCardFrequency(pile);
            int randSwapPile = rand.nextInt(this.game.NUM_CARDS_IN_PILE);
            Integer newValue = this.game.getAndSetRandomValueOfCommunityPile(pile.get(randSwapPile));
            pile.set(randSwapPile, newValue);
            if (this.game.isCompletedPile(pile)) {
                cleanUpCompletedPile(indexOfPile, pile);
            }
        }
    }

    private int getValueToSwapIndex(int pileIndex){
        int indexOfCardAtEndOfPile = this.game.NUM_CARDS_IN_PILE - 1;
        if (pileIndex < indexOfCardAtEndOfPile) {
            return indexOfCardAtEndOfPile;
        }
        return indexOfCardAtEndOfPile - 1;  // the second to last card
    }

    private void makeMove(){
        // Simulates a basic strategy.  Not pretty, just to get a baseline.
        if (!uncompletedPiles.isEmpty()){
            int indexOfPile = rand.nextInt(uncompletedPiles.size());
            ArrayList<Integer> pile = uncompletedPiles.get(indexOfPile);
            int communityIndex = 0;
            int pileIndex = 0;
            int valueToSwapIndex;
            while (pileIndex < this.game.NUM_CARDS_IN_PILE) {
                if (this.game.isCompletedPile(pile)) {
                    cleanUpCompletedPile(indexOfPile, pile);
                    break;
                }
                orderPileByCardFrequency(pile);
                valueToSwapIndex = getValueToSwapIndex(pileIndex);
                if (this.game.compareAndUpdateCommunityPile(communityIndex, pile.get(pileIndex), pile.get(valueToSwapIndex))) {
                    pile.set(valueToSwapIndex, pile.get(pileIndex));
                    pileIndex += 2;
                    communityIndex = 0;
                } else {
                    communityIndex++;
                    if (communityIndex > 3) {
                        communityIndex = 0;
                        pileIndex++;
                    }
                }
            }
            randomlySwapACardIfPileNotComplete(indexOfPile, pile);
        }
    }
}
