public class Solution {
    public String interpret(String command) {
        // Initialize a StringBuilder to build the result
        StringBuilder result = new StringBuilder();
        
        // Iterate over each character in the command string
        for (int i = 0; i < command.length(); i++) {
            // Check for 'G'
            if (command.charAt(i) == 'G') {
                result.append('G');
            }
            // Check for '(' - indicates the start of a possible "al" or an empty string
            else if (command.charAt(i) == '(') {
                // Check the next character
                if (command.charAt(i + 1) == ')') {
                    result.append('o'); // Empty parentheses corresponds to 'o'
                    i++; // Move past ')'
                } else { 
                    // Otherwise, it must be "al"
                    result.append("al");
                    i += 3; // Move past "al)"
                }
            }
        }
        // Convert StringBuilder to string and return final result
        return result.toString();
    }
}