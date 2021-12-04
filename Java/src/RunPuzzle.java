import day0.Puzzle;

public class RunPuzzle {
    public static void main(String[] args) {

        Puzzle puzzle = new day2.Puzzle();

        long startTime = System.nanoTime();
        System.out.println("Puzzle 1 ----------------");
        long answer = puzzle.part1();
        System.out.println("Answer: " + answer);
        long stopTime = System.nanoTime();
        System.out.println("Completed in " + (stopTime-startTime)/1000000 + " ms.\n");

        startTime = System.nanoTime();
        System.out.println("Puzzle 2 ----------------");
        answer = puzzle.part2();
        System.out.println("Answer: " + answer);
        stopTime = System.nanoTime();
        System.out.println("Completed in " + (stopTime-startTime)/1000000 + " ms.");
    }

}
