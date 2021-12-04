package utilities;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Scanner;

public class InputLoader {
    private static Scanner sc;
    private static File file;

    public static int[] intArray(int dayNo, boolean getSample){
        String folder = getSample ? "sample" : "input";
        try {
            List<String> lines = Files.readAllLines(Path.of("../Data/"+ folder +"/day" + dayNo +".txt"));
            return lines.stream().mapToInt(Integer::parseInt).toArray();
        }
        catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
        return null;
    }

    public static List<String> list(int dayNo, boolean getSample) {
        String folder = getSample ? "sample" : "input";
        try {
            List<String> lines = Files.readAllLines(Path.of("../Data/"+ folder +"/day" + dayNo +".txt"));
            return lines;
        }
        catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
        return null;
    }

    public static String string(int dayNo, boolean getSample) {
        String folder = getSample ? "sample" : "input";
        try {
            String content = Files.readString(Path.of("../Data/"+ folder +"/day" + dayNo +".txt"));
            return content;
        }
        catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
        return null;
    }


}
