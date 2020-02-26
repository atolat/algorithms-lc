# HashMap<Character, Integer> map = new HashMap<Character,Integer>();
# for(char c: s.toCharArray()){
#     if(map.containsKey(c)){
#         map.put(c,map.get(c)+1);
#     }else{
#         map.put(c,1);
#     }
# }    
# int res = 0;
# HashSet<Integer> set = new HashSet<>();
# for(int count : map.values()){
    
#     if(!set.contains(count)){
#         set.add(count);
#     }else{
#         int n = count;
#        while(set.contains(n) && n>0){
#            n=n-1;
#            res=res+1;
#        } 
#        if(n>0){
#            set.add(n);
#        }
#     }
# }

# return res;