import java.util.List;
import java.util.ArrayList;
import java.lang.Math;
import java.util.Arrays;

/*
 * Solution for problem 707. Problem does not specify if listeners and towers are ordered or not.
 * Solution can be optimised if so.
 * 
 * If tower or listener is outside the range (0, 1000), the value returned will be -1. Alternatively, this could be modified
 * to simply ignore any towers or listeners outside of the range.
 */

public class problem_707{
    public static void main(String[] args){
        int[] listenersBasic = {1, 5, 11, 20};
        int[] towersBasic = {4, 8, 15};

        int[] listenersMaxRangeExceeded = {1, 5, 11, 20, 1001};
        int[] listenersMinRangeExceeded = {-1, 1, 5, 11, 20};

        int[] towersMaxRangeExceeded = {4, 8, 15, 1001};
        int[] towersMinRangeExceeded = {-1, 4, 8, 15};

        int[] listenersMinAndMaxRange = {0, 1, 5, 11, 20, 1000};
        int[] towersMinAndMaxRange = {0, 4, 8, 15, 1000};


        tester(listenersBasic, towersBasic, 5);
        tester(listenersMaxRangeExceeded, towersBasic, -1);
        tester(listenersMinRangeExceeded, towersBasic, -1);
        tester(listenersBasic, towersMaxRangeExceeded, -1);
        tester(listenersBasic, towersMinRangeExceeded, -1);
        tester(listenersMinAndMaxRange, towersBasic, 985);
        tester(listenersBasic, towersMinAndMaxRange, 5);
    }

    public static void tester(int[] listeners, int[] towers, int expected){
        System.out.printf("Listeners = %s, towers = %s. Min range required = %d. Should be %d.%n", Arrays.toString(listeners), Arrays.toString(towers), getMinRange(listeners, towers), expected);

    }

    public static int getMinRange(int[] listeners, int[] towers){
        final int MIN_POS = 0;
        final int MAX_POS = 1000;

        List<Integer> rangesFromClosestTower = new ArrayList<>();

        for(int listener : listeners){
            if(listener < MIN_POS || listener > MAX_POS){
                return -1;
            }
            int minRange = Integer.MAX_VALUE;

            for(int tower: towers){
                if(tower < MIN_POS || tower > MAX_POS){
                    return -1;
                }
                int potentialRange = Math.abs(listener - tower);

                // I.e. if there is a closer tower...
                if(potentialRange < minRange){
                    minRange = potentialRange;
                }
            }

            rangesFromClosestTower.add(minRange);
        }

        int maxRange = Integer.MIN_VALUE;

        for(int range : rangesFromClosestTower){
            if(range > maxRange){
                maxRange = range;
            }
        }

        return maxRange;
    }
}