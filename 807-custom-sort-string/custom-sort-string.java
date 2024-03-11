class Solution {
    public String customSortString(String order, String s) {
        char[] ord = order.toCharArray();
        char[] st = s.toCharArray();
        ArrayList<Character> al = new ArrayList<Character>();
        ArrayList<Character> ans = new ArrayList<Character>();
        for (char c:st){
            al.add(c);
        }
        // System.out.println(al);
        for (int i=0;i<ord.length;i++){
            while (al.contains(ord[i])){
                ans.add(ord[i]);
                al.remove(Character.valueOf(ord[i]));
            }
        }
        // System.out.println(ans);
        // System.out.println(al);
        ans.addAll(al);
        // System.out.println(ans);
        StringBuilder sb = new StringBuilder();
        for (int q=0;q<ans.size();q++){
            sb.append(ans.get(q));
        }
        // System.out.println(sb);
        return sb.toString();
    }
}