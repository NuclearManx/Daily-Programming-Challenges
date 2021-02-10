import java.util.Stack;

public class problem_712{
    
    public static void main(String[] args){
        String testOne = "([])[]({})";
        String testTwo = "([)]";
        String testThree = "((()";
        String testFour = "((((({{{{{[[[[[((((()))))]]]]]}}}}})))))()()(){{[[]]}}";
        String testFive = "";
        String testSix = "((((({{{{[[[[[((((()))))]]]]]}}}}})))))()()(){{[[]]}}";

        checkStringTester(testOne, true);
        checkStringTester(testTwo, false);
        checkStringTester(testThree, false);
        checkStringTester(testFour, true);
        checkStringTester(testFive, true);
        checkStringTester(testSix, false);
    }

    public static void checkStringTester(String str, boolean expected){
        System.out.println("String: '" + str + "' is well-formed: " + checkString(str) + ". Should be: " + expected);
    }

    private static char oppositeChar(char symbol){
        if (symbol == '}'){
            return '{';
        }
        if (symbol == ')'){
            return '(';
        }
        if (symbol == ']'){
            return '[';
        }
        return '_';
    }

    public static boolean checkString(String str){
        String opens = "{[(";
        Stack<Character> toBeClosed = new Stack<Character>();

        for (char chr : str.toCharArray()){
            
            if (opens.contains(String.valueOf(chr))){
                toBeClosed.push(chr);
            }
            else if (toBeClosed.pop() != oppositeChar(chr)) {
                return false;
            }
        }
        if (toBeClosed.empty()){
            return true;
        }

        return false;
    }
}
