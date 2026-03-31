class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder newStrs = new StringBuilder(); 
        System.out.println(s.toCharArray());
        for ( char c : s.toCharArray()) { 
            if ( Character.isLetterOrDigit(c)) { 
                newStrs.append(Character.toLowerCase(c));
            }

        }
        return newStrs.toString().equals(newStrs.reverse().toString());
    }
}
