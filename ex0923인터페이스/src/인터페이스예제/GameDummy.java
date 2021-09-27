package 인터페이스예제;

import java.util.Random;

public class GameDummy implements IGame {
	Random r = new Random();
	int a = 0;
	int b = 0;

	@Override
	public void makeRandom() {
		a = r.nextInt(9) + 1;
		b = r.nextInt(9) + 1;
	}

	@Override
	public String getQuizMsg() {

		return a + "+" + b + "=";
	}

	@Override
	public boolean checkAnswer(int answer) {
		//answer = a + b;
		if (answer == a + b) {
			return true;
		} else {

			return false;
		}
	}
}
