public class Solution {
    public bool CanConstruct(string ransomNote, string magazine) {
        //DICTIONARY METHOD
        Dictionary<char, int> d = new Dictionary<char, int>();

        foreach(char c in magazine){
            if(d.ContainsKey(c)){
                d[c]++;
            }
            else{
                d[c] = 1;
            }
        }

        foreach(var c in ransomNote){
            if(!d.ContainsKey(c) || d[c] == 0){
                return false;
            }
            else{
                d[c]--;
            }
        }

        return true;

        //LIST REMOVE Method
        // List<char> l = new List<char>(ransomNote);
        // int count = 0;

        // foreach(char c in magazine){
        //     if(l.Remove(c)){
        //         count++;
        //     }
        // }

        // return ransomNote.Length == count;
    }
}