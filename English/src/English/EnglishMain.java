package English;

import java.util.Scanner;

public class EnglishMain {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		EnglishDAO dao = new EnglishDAO();
		// 1. ȸ������ �α��� ����
		System.out.println("����ܾ� ���߱� ������ �����մϴ�");

		while (true) {
			System.out.print("1.ȸ������ 2.�α��� 3. ���� : ");
			int input = sc.nextInt();
			if (input == 1) { // ȸ������
				System.out.print("���̵� �Է� : ");
				String id = sc.next();
				System.out.print("��й�ȣ �Է� : ");
				String pw = sc.next();
				System.out.print("�г��� �Է� : ");
				String nick = sc.next();

				EnglishVO vo = new EnglishVO(id, pw, nick);
				int cnt = dao.memship(vo);
				if (cnt > 0) {
					System.out.println(id + "�� ȯ���մϴ�");
				} else {
					System.out.println("ȸ�����Կ� �����߽��ϴ�");
				}
			} else if (input == 2) { // �α���
				System.out.print("���̵� �Է� : ");
				String id = sc.next();
				System.out.print("��й�ȣ �Է� : ");
				String pw = sc.next();
				
				EnglishVO vo = new EnglishVO(id, pw);
				EnglishVO info = dao.login(vo);
				
				if (info != null) {
					System.out.println(info.getNick()+"�� ȯ���մϴ�");
					System.out.println("���� ������ ������ �ʾҽ��ϴ� \n�׸� Ǯ�� ������ Stop �� �Է��ϼ���");					
					System.out.println("����ϴ� ���̵��� ��ȣ�� �Է��ϼ���");
					while(true) {
					System.out.print("1.�� 2.�� 3.�� : ");
					int choice = sc.nextInt();
					if(choice == 1) {
						for(int i = 0; i<10; i++) {
							System.out.println(dao.high(vo));
							String answer = sc.next();
						}
					}else if(choice == 2) {
						
					}else if(choice == 3) {
						
					}else {
						System.out.println("�߸��� ���̵��� �Է� �Ͽ����ϴ� �ٽ� �������ּ���");
					}
					}
				}else {
					System.out.println("�α��� ���� !");
				}
			} else if (input == 3) {
				System.out.println("�����ϼ˽��ϴ� ~!");
				sc.close();
				break;
			} else {
				System.out.println("�߸� �Է��ϼ̽��ϴ� �ٽ� �Է����ּ���");
			}
		}
	}
}
