package day1;

import utilities.InputLoader;

public class Puzzle extends day0.Puzzle{
    int[] inputData;

    public Puzzle() {
        this.inputData = InputLoader.intArray(1, false);
    }

    public long part1(){
        int inc = 0;
        for(int i=1; i < this.inputData.length; i++){
            if(inputData[i] > inputData[i-1]) inc++;
        }

        return inc;
    }

    public long part2(){
        int inc = 0;
        for(int i=3; i < this.inputData.length; i++){
            if(this.inputData[i] > this.inputData[i-3]) inc++;
        }

       return inc;
    }



}
