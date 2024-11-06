import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {

    public List<String> alertNames(String[] keyName, String[] keyTime) {
        Map<String, List<Integer>> timeMap = new HashMap<>();
        
        // Convert keyTime to a map with the associated keyName
        for (int i = 0; i < keyName.length; i++) {
            String name = keyName[i];
            String[] splitTime = keyTime[i].split(":");
            int minutes = Integer.parseInt(splitTime[0]) * 60 + Integer.parseInt(splitTime[1]);
            timeMap.computeIfAbsent(name, k -> new ArrayList<>()).add(minutes);
        }

        List<String> alertNames = new ArrayList<>();
        
        // Check each user's times
        for (Map.Entry<String, List<Integer>> entry : timeMap.entrySet()) {
            String name = entry.getKey();
            List<Integer> times = entry.getValue();
            // Sort the list of times to facilitate the checking
            times.sort(Integer::compareTo);
            
            // Check for alerts within one hour
            for (int i = 0; i < times.size() - 2; i++) {
                if (times.get(i + 2) - times.get(i) <= 60) {
                    alertNames.add(name);
                    break; // No need to check further for this name
                }
            }
        }
        
        // Sort the names before returning
        alertNames.sort(String::compareTo);
        return alertNames;
    }
}