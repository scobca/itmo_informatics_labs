import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int counter = 0;
        int[] indexes = new int[7];

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the received message: ");
        String number = scanner.nextLine();

        if (number.length() != 7) {
            System.out.println("Error: incorrect message length");
            System.exit(0);
        }

        for (int i = 0; i < number.length(); i++) {
            int index = Integer.parseInt(String.valueOf(number.charAt(i)));

            counter += index;
            indexes[i] = index;
        }

        if (counter > 7) {
            System.out.println("Error: Invalid format of the received message");
        } else {
            output(getSyndromes(indexes));
        }
    }

    public static int[] getSyndromes(int[] indexes) {
        int s1 = (indexes[0] + indexes[2] + indexes[4] + indexes[6]) % 2;
        int s2 = (indexes[1] + indexes[2] + indexes[5] + indexes[6]) % 2;
        int s3 = (indexes[3] + indexes[4] + indexes[5] + indexes[6]) % 2;

        String errorCode = "" + s1 + s2 + s3;

        System.out.println("Start processing...");

        if (!errorCode.equals("000")) {
            switch (errorCode) {
                case "100" -> {
                    indexes[0] = changeNum(indexes[0]);
                    System.out.println("Error: bit r1");
                    return indexes;
                }
                case "010" -> {
                    indexes[1] = changeNum(indexes[1]);
                    System.out.println("Error: bit r2");
                    return indexes;
                }
                case "110" -> {
                    indexes[2] = changeNum(indexes[2]);
                    System.out.println("Error: bit i1");
                    return indexes;
                }
                case "001" -> {
                    indexes[3] = changeNum(indexes[3]);
                    System.out.println("Error: bit r3");
                    return indexes;
                }
                case "101" -> {
                    indexes[4] = changeNum(indexes[4]);
                    System.out.println("Error: bit i2");
                    return indexes;
                }
                case "011" -> {
                    indexes[5] = changeNum(indexes[5]);
                    System.out.println("Error: bit i3");
                    return indexes;
                }
                case "111" -> {
                    indexes[6] = changeNum(indexes[6]);
                    System.out.println("Error: bit i4");
                    return indexes;
                }
            }
        }

        System.out.println("No errors!");
        return indexes;
    }

    public static int changeNum(int index) {
        if (index == 0) {
            return 1;
        } else {
            return 0;
        }
    }

    public static void output(int[] indexes) {
        String message = "";
        String incomingMessage = "" + indexes[2] + indexes[4] + indexes[5] + indexes[6];

        for (int index : indexes) {
            message = message.concat(String.valueOf(index));
        }

        System.out.println("Corrected message:" + " " + message);
        System.out.println("Incoming message:" + " " + incomingMessage);
    }
}
