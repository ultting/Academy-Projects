package 인터페이스예제;

import java.util.Random;

public class PlusGame implements IGame {
	// 알고리즘쪽 코드

	// 필드
	private Random ran;
	private int num1;
	private int num2;

	@Override
	public void makeRandom() {
		// 난수 생성하는 기능
		ran = new Random();
		num1 = ran.nextInt(9) + 1;
		num2 = ran.nextInt(9) + 1;
	}

	@Override
	public String getQuizMsg() {
		// 생성한 난수를 문자열 형태로 되돌려 주기
		// 난수1 + 난수2 =
		String result = num1 + "+" + num2 + "=";
		return result;
	}

	@Override
	public boolean checkAnswer(int answer) {
		// 매개변수로 받아온 숫자와 실제 난수1+난수2 값이 일치하는지 비교
		
		return num1+num2==answer;
	}

}
