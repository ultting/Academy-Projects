package �������̽�����;

import java.util.Scanner;

public class Main {

	// ui & play
	// ����Ƚ��üũ - 5����
	// �����ȸ Ƚ��üũ - �� ������ ��ȸ�� 3��
	// ����ڷκ��� �� �Է� - ���� �ΰ��� ���ϴ� ��
	// �޽��� ��� - ���� ������ ���

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//GameDummy p1 = new GameDummy(); // �ӽ� �׽�Ʈ �뵵
		PlusGame p1 = new PlusGame();

		int exam = 5; // ���� ����
		int count = 3; // Ʋ�� Ƚ�� 0�� �Ǹ� ���� ����
		int complete = 0; // ���� Ƚ��

		for (int i = 0; i < 5; i++) {
			p1.makeRandom();
			for (int j = 0; j < 3; j++) {
				System.out.print(p1.getQuizMsg());
				int answer = sc.nextInt();
				if (p1.checkAnswer(answer)) {
					complete++;
					break;
				} else {
					System.out.println("�����Դϴ�~");
				}
			}
		}
		System.out.println("������ ������" + count + "�� �Դϴ�.");
		sc.close();
		
//		while (true) {
//			count = 3;
//			if (exam == 0) {
//				System.out.println("������ ���� �Ǿ����ϴ�");
//				break;
//			} else {
//				p1.makeRandom(); // ������ �ο�
//				System.out.print(p1.getQuizMsg());// ���� ���
//				int answer = sc.nextInt(); // ��µ� ������ ���� �Է��� ��ĳ��
//				boolean check = p1.checkAnswer(answer); // answer�� ���� ����
//				if (check == true) {
//					complete++;
//				} else if (check == false) {
//					while (count > 0) {
//						System.out.println("������ �ٽ� �Է� �� ������");
//						System.out.print(p1.getQuizMsg());
//						answer = sc.nextInt();
//						count--;
//					}
//				}
//				exam--;
//			}
//		}
//		sc.close();
//		System.out.println("���� ���� : " + complete);

	}

}
