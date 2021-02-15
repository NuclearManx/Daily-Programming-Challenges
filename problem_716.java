import java.util.*;

public class problem_716 {
    public static void main(String[] args) {
        // This is a nice converter: https://onlineutf8tools.com/convert-utf8-to-decimal
        int[] example = {226, 130, 172};
        tester(example, true);

        int[] exampleOne = {0, 0, 1, 0};
        tester(exampleOne, false);

        int[] exampleTwo = {97}; // 'a'
        tester(exampleTwo, true);
    }

    // The question weirdly asks for input bytes to be decimal array, but then gives examples in binary form.
    public static void tester(int[] bytes, boolean expected) {
        String byteString = "";
        for (int utfByte: bytes) {
            byteString += intToByte(utfByte);
            byteString += " ";
        }
        System.out.printf("UFT-8 %si.e. %s is valid: %s. Should be: %s.\n", byteString, Arrays.toString(bytes), validUFT8(bytes), expected);
    }

    public static String intToByte(int toByte) {
        if (toByte < 0 || toByte > 256) {
            throw new ArithmeticException("A byte must be between decimal 0 and 256!");
        }

        String byteVersion = "";

        for (int i = 128; i > 0; i = i / 2) {
            if ((toByte - i) > -1) {
                byteVersion += "1";
                toByte -= i;
            }
            else {
                byteVersion += "0";
            }
        }

        return byteVersion;
    }

    public static boolean validUFT8(int[] byteInts) {
        if (byteInts.length > 4) {
            throw new ArithmeticException("The maximum number of bytes for UTF-8 encoding is four!");
        }
        
        List<String> bytes = new ArrayList<String>();        
        for (int byteInt : byteInts) {
            bytes.add(intToByte(byteInt));
        }

        int numOfBytes = bytes.size();

        if (numOfBytes == 1) {
            return bytes.get(0).substring(0, 1).equals("0");
        }

        else {
            String expectedStart = "";
            for (int i = 0; i < numOfBytes; i++) {
                expectedStart += "1";
            }
            expectedStart += "0";


            if (!bytes.get(0).substring(0, numOfBytes + 1).equals(expectedStart)) {
                return false;
            }

            for (int i = 1; i < numOfBytes; i++) {
                if (!bytes.get(i).substring(0, 2).equals("10")) {
                    return false;
                }
            }
        }
        return true;
    }
}
