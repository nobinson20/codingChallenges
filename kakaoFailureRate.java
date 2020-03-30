import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class kakaoFailureRate {
    public static void main(String[] args) {
        int N = 4;
        int[] stages = {4,4,4,4,4};
        int[] result = solution(N, stages);

        System.out.println(Arrays.toString(result));
    }

    public static int[] solution(int N, int[] stages) {
        int playersN = stages.length;
        ArrayList<Double> resultList = new ArrayList<Double>();

        // count occurences of same stage number in stages,
        // '1'의 개수 => Arraylist<Double>의 0번째에 배치
        // (occurence 세기 쉬울려고 arraylist 사용)
        // [1,3,2,1,0]
        ArrayList<Integer> stagesList = new ArrayList<>();
        for (int e : stages) {
            stagesList.add(e);
        }

        for (int i = 1; i < N + 1; i++) {
            double occurences = Collections.frequency(stagesList, i); //auto-casting
            resultList.add(occurences);
        }


        // stages랑 사이즈 같은 배열 하나 더 만들어서 (굳이 ㄴㄴ)
        // each element = playersN - arraylist[i-1]
        // [8,7,4,2,1]
        // 분자/분모 해서 arraylist에 차례로 집어넣기

        //int stuckN;

        for (int i = 0; i < resultList.size(); i++) {
            int stuckN = resultList.get(i).intValue();
            resultList.set(i, resultList.get(i) / playersN);
            playersN -= stuckN;
        }


        // 가장 큰 숫자의 인덱스를 찾아 + 1 한 다음 배열에 집어넣기
        int[] result = new int[resultList.size()];
        for (int i = 0; i < result.length; i++) {
            int pos = resultList.indexOf(Collections.max(resultList));
            resultList.set(pos, -1.0);
            result[i] = pos + 1;
        }
        return result;
    }
}


// succint 하게 쓰긴 했지만 arraylist, collections API를 너무 많이 이용했다는 단점이 있다.
