package 인터페이스예제;

import java.util.Scanner;

public class Main {

	// ui & play
	// 게임횟수체크 - 5문제
	// 정답기회 횟수체크 - 한 문제당 기회는 3번
	// 사용자로부터 값 입력 - 난수 두개를 더하는 값
	// 메시지 출력 - 맞춘 정답이 몇개냐

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//GameDummy p1 = new GameDummy(); // 임시 테스트 용도
		PlusGame p1 = new PlusGame();

		int exam = 5; // 문제 개수
		int count = 3; // 틀린 횟수 0이 되면 다음 문제
		int complete = 0; // 맞춘 횟수

		for (int i = 0; i < 5; i++) {
			p1.makeRandom();
			for (int j = 0; j < 3; j++) {
				System.out.print(p1.getQuizMsg());
				int answer = sc.nextInt();
				if (p1.checkAnswer(answer)) {
					complete++;
					break;
				} else {
					System.out.println("오답입니다~");
				}
			}
		}
		System.out.println("정답의 개수는" + count + "개 입니다.");
		sc.close();
		
//		while (true) {
//			count = 3;
//			if (exam == 0) {
//				System.out.println("게임이 종료 되었습니다");
//				break;
//			} else {
//				p1.makeRandom(); // 랜덤수 부여
//				System.out.print(p1.getQuizMsg());// 문제 출력
//				int answer = sc.nextInt(); // 출력된 문제의 합을 입력할 스캐너
//				boolean check = p1.checkAnswer(answer); // answer의 값을 정의
//				if (check == true) {
//					complete++;
//				} else if (check == false) {
//					while (count > 0) {
//						System.out.println("정답을 다시 입력 해 보세요");
//						System.out.print(p1.getQuizMsg());
//						answer = sc.nextInt();
//						count--;
//					}
//				}
//				exam--;
//			}
//		}
//		sc.close();
//		System.out.println("맞춘 갯수 : " + complete);

	}

}
