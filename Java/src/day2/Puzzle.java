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
        int[] position = new int[2];

        for (String command: input){
            String[] values = command.split(" ");
            switch (values[0]) {
                case "forward":
                    position[0] += Integer.parseInt(values[1]);
                    break;
                case "down":
                    position[1] += Integer.parseInt(values[1]);
                    break;
                case "up":
                    position[1] -= Integer.parseInt(values[1]);
                    break;
            }
        }
        return position[0] * position[1];
    }

    public long part2() {
        int[] position = new int[3];

        for (String command: input){
            String[] values = command.split(" ");
            switch (values[0]) {
                case "forward":
                    position[0] += Integer.parseInt(values[1]);
                    position[1] += position[2] * Integer.parseInt(values[1]);
                    break;
                case "down":
                    position[2] += Integer.parseInt(values[1]);
                    break;
                case "up":
                    position[2] -= Integer.parseInt(values[1]);
                    break;
            }
        }
        return position[0] * position[1];
    }
}
