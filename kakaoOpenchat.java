import java.util.*;

public class Main {

    public static void main(String[] args) {
        String[] record =
                {"Enter uid1234 Muzi",
                        "Enter uid4567 Prodo",
                        "Leave uid1234",
                        "Enter uid1234 Prodo",
                        "Change uid4567 Ryan"
                };
/////////////////////////// String[] record => List<Element> 테스트
//        List<Element> elements = new ArrayList<>();
//
//        for (int i = 0; i < record.length; i++) {
//            String[] eArr = record[i].split(" ");
//            elements.add(new Element());
//            for (int j = 0; j < 3; j++) {
//                switch (j) {
//                    case 0:
//                        elements.get(i).action = eArr[j];
//                        break;
//                    case 1:
//                        elements.get(i).uid = eArr[j];
//                        break;
//                    case 2:
//                        if (eArr.length == 2){
////                            System.out.println("eArr.length == 2 detected: " + Arrays.toString(eArr));
////                            System.out.println("i is " + i);
//                            for (int k = i - 1 ; k >= 0; k--){
////                                System.out.println("For loop 진입");
////                                System.out.println(elements.get(i).uid + "&&" + elements.get(k).uid);
//                                if(elements.get(i).uid.equals(elements.get(k).uid)) {
//                                    //System.out.println(elements.get(i).uid + "&&" + elements.get(k).uid);
//                                    elements.get(i).nickname = elements.get(k).nickname;
//                                    break;
//                                }
//                            }
//                        } else{
//                            elements.get(i).nickname = eArr[j];
//                        }
//
//                        break;
//                }
//            }
//        }
//
//        for (Element e : elements) {
//            System.out.println("Element: ");
//            System.out.println("action is " + e.action +
//                    "\n uid is " + e.uid +
//                    "\n nickname is " + e.nickname);
//        }


/////////////////////////////

        System.out.println(Arrays.toString(solution(record)));

    }
    // solution 1: map을 포함해서 자바 내용을 전반적으로 다 까먹은 바람에 주먹구구식으로 만든 코드.
    //    public static String[] solution(String[] record) {
//
//
//        List<Element> elements = new ArrayList<>();
//
//        for (int i = 0; i < record.length; i++) {
//            String[] eArr = record[i].split(" ");
//            elements.add(new Element());
//            for (int j = 0; j < 3; j++) {
//                switch (j) {
//                    case 0:
//                        elements.get(i).action = eArr[j];
//                        break;
//                    case 1:
//                        elements.get(i).uid = eArr[j];
//                        break;
//                    case 2:
//                        if (eArr.length == 2) {
////                            System.out.println("eArr.length == 2 detected: " + Arrays.toString(eArr));
////                            System.out.println("i is " + i);
//                            for (int k = i - 1; k >= 0; k--) {
////                                System.out.println("For loop 진입");
////                                System.out.println(elements.get(i).uid + "&&" + elements.get(k).uid);
//                                if (elements.get(i).uid.equals(elements.get(k).uid)) {
//                                    //System.out.println(elements.get(i).uid + "&&" + elements.get(k).uid);
//                                    elements.get(i).nickname = elements.get(k).nickname;
//                                    break;
//                                }
//                            }
//                        } else {
//                            elements.get(i).nickname = eArr[j];
//                        }
//
//                        break;
//                }
//            }
//        }
//
//
//
//        List<Element> elementsResult = new ArrayList<>();
//
//        for (int i = 0; i < elements.size(); i++) {
//            switch (elements.get(i).action) {
//                case "Enter":
//                    // elementsResult에 element 추가
//                    Element element = new Element( elements.get(i).action, elements.get(i).uid, elements.get(i).nickname );
//                    elementsResult.add(element);
//                    // elementsResult에 같은 uid를 가진 객체가 있으면 nickname 수정
//
//                    // 아래는 실수. for-each는 해당 자료구조의 내용을 변경할 수 없다.
////                    for (Element e : elementsResult) {
////                        if (e.uid == elements.get(i).uid)
////                            e.nickname = elements.get(i).nickname;
////                    }
//
//                    for (int j = 0; j < elementsResult.size(); j++) {
//                        if (elementsResult.get(j).uid.equals(elements.get(i).uid))
//                            elementsResult.get(j).nickname = elements.get(i).nickname;
//                    }
//
//                    break;
//                case "Leave":
//                    // elementsResult에 element 추가
//                    // elementsResult에 같은 uid를 가진 객체를 찾아서 nickname을 가져와서 추가
//                    Element element2 = new Element( elements.get(i).action, elements.get(i).uid, elements.get(i).nickname );
//
//                    // for each 실수 내용
////                    for (Element e : elementsResult) {
////                        if (e.uid == elements.get(i).uid) {
////                            element.nickname = e.nickname;
////                            break;
////                        }
////                    }
//
//                    // 위에서 복사할때 이미 처리한 내용!!!!!!!
//                    // find the first element that has same uid in elementsResult
////                    for (int j = 0; j < elementsResult.size(); j++) {
////                        if (elementsResult.get(j).uid.equals(elements.get(i).uid)) {
////                            element2.nickname = elements.get(i).nickname;
////                            break;
////                        }
////                    }
//
//
//                    elementsResult.add(element2);
//                    break;
//                case "Change":
//                    // elementsResult 중에 uid가 같은 것을 찾아서
//                    // nickname 을 모두 수정한다.
//
//
//                    for (int j = 0; j < elementsResult.size(); j++) {
//                        if (elementsResult.get(j).uid.equals(elements.get(i).uid))
//                            elementsResult.get(j).nickname = elements.get(i).nickname;
//                    }
//
//                    break;
//
//            }
//        } // end of for loop
//
//        String[] result = new String[elementsResult.size()];
//        for (int i = 0; i < result.length; i++) {
//            if (elementsResult.get(i).action.equals("Enter")) {
//                String s = elementsResult.get(i).nickname + "님이 들어왔습니다.";
//                result[i] = s;
//            } else if (elementsResult.get(i).action.equals("Leave")) {
//                String s = elementsResult.get(i).nickname + "님이 나갔습니다.";
//                result[i] = s;
//            }
//        }
//        // object를 copy해올때는 새로운 객체를 만든 다음에 initialize해줘야한다. 아니면 그 reference의 값을 그대로 가져와서
//        // 향후에 원래 value들에 영향을 준다.
////        for (Element e : elements) {
////            System.out.println("Element: ");
////            System.out.println("action is " + e.action +
////                    "\n uid is " + e.uid +
////                    "\n nickname is " + e.nickname);
////        }
////
////        for (Element e : elementsResult) {
////            System.out.println("Element Result: ");
////            System.out.println("action is " + e.action +
////                    "\n uid is " + e.uid +
////                    "\n nickname is " + e.nickname);
////        }
//
//
////        System.out.println(elements.toString());
////        System.out.println(elementsResult.toString());
//
//        return result;
//    }


    // solution 2
    // 아래 코드를 쓴 사람은 해쉬맵과 배열 2개를 이용했다.
    // 출처: https://sundries-in-myidea.tistory.com/46


//    public static String[] solution(String[] record) {
//        HashMap<String, String> user = new HashMap<String, String>();
//        String[] logState = new String[100000];
//        String[] logId = new String[100000];
//        int j = 0;
//        for (int i = 0; i < record.length; i++) {
//            String check = record[i];
//            StringTokenizer st = new StringTokenizer(check, " ");
//            String command = st.nextToken();
//            if (command.equals("Enter")) {
//                String id = st.nextToken();
//                String nick = st.nextToken();
//                user.put(id, nick);
//                logId[j] = id;
//                logState[j] = "님이 들어왔습니다.";
//                j++;
//            }
//            if (command.equals("Leave")) {
//                String id = st.nextToken();
//                logId[j] = id;
//                logState[j] = "님이 나갔습니다.";
//                j++;
//            }
//            if (command.equals("Change")) {
//                String id = st.nextToken();
//                String nick = st.nextToken();
//                user.put(id, nick);
//            }
//        } //이중 포문 안됨.
//        String answer[] = new String[j];
//        for (int i = 0; i < j; i++) {
//            answer[i] = user.get(logId[i]) + logState[i];
//        }
//        return answer;
//    }

    /// solution 3
    // 아래 사람 코드가 젤 나은 것 같은데, 해쉬맵과 링크드리스트를 이용했다.
    /*
        참고로,
        Map<String, String> idMap = new HashMap<>();
        HashMap<String, String> idMap = new HashMap<>();
        은 동일한 코드이지만, 윗줄의 코드는 Map이라는 인터페이스를 이용해서 코드의 재사용성을 늘렸기 때문에
        아주 약간 더 좋은 코드라고 할 수 있다.
     */
    public static String[] solution(String[] record) {
        Map<String, String> idMap = new HashMap<>();
        List<String[]> tmp = new LinkedList<>();

        for (String records : record)
        {
            String[] keyWord = records.split(" ");
            if (keyWord[0].equals("Enter"))
            {
                idMap.put(keyWord[1], keyWord[2]);
                tmp.add(keyWord);
            } else if (keyWord[0].equals("Change"))
            {
                idMap.put(keyWord[1], keyWord[2]);
            } else
            {
                tmp.add(keyWord);
            }
        }

        String[] answer = new String[tmp.size()];
        int idx = 0;
        for (String[] keyWords : tmp)
        {
            String nickName = idMap.get(keyWords[1]);
            if (keyWords[0].equals("Enter"))
                answer[idx++] = nickName + "님이 들어왔습니다.";
            else
                answer[idx++] = nickName + "님이 나갔습니다.";
        }
        return answer;
    }

}


// 결론적으로 Map을 이용할 줄 아는 것이 관건인 문제였다. Map을 이용하면 K, V 페어를 이용해서
// K값이 같은 객체를 손쉽게 찾아서 V값을 수정할 수 있기 때문이다.


