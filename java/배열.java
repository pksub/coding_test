package java;

public class 배열 {
    public int[] solution(String[] cpr) {
        int[] answer = {0, 0, 0, 0, 0};
        String[] basic_order = {"check", "call", "pressure", "respiration", "repeat"};

        for(int i=0; i< answer.length; i++){
                for(int j=0; j<basic_order.length; j++){
                    if(cpr[i].equals(basic_order[j])){
                        answer[i] = ++j;
                        break;
                    }
                }
            }
            return answer;
        }
}

/* 입력 / 출력
 * ["call", "respiration", "repeat", "check", "pressure"]	[2, 4, 5, 1, 3]
 * ["respiration", "repeat", "check", "pressure", "call"]	[4, 5, 1, 3, 2]
 */