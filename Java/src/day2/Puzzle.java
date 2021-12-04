package day2;

import utilities.InputLoader;

import java.util.List;

public class Puzzle extends day0.Puzzle {
    List<String> sample;
    List<String> input;

    public Puzzle(){
        input = InputLoader.list(2, false);
        sample = InputLoader.list(2, true);
    }

    public long part1() {

        for (String in : input){
            System.out.println(in);
        }
        return 0;
    }
}
