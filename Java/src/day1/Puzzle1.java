package day1;

import utilities.InputLoader;

public class Puzzle1 {
    public Puzzle1() {
        int[] inputData = InputLoader.asList(1).stream().mapToInt(Integer::parseInt).toArray();

        int inc = 0;
        for(int i=1; i < inputData.length; i++){
            if(inputData[i] > inputData[i-1]) inc++;
        }

        System.out.println(inc);
    }
}
