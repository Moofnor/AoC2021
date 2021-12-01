package day1;

import utilities.InputLoader;

public class Puzzle2 {
    public Puzzle2() {
        int[] inputData = InputLoader.asList(1).stream().mapToInt(Integer::parseInt).toArray();

        int inc = 0;
        for(int i=3; i < inputData.length; i++){
            if(inputData[i] > inputData[i-3]) inc++;
        }

        System.out.println(inc);
    }
}
