package English;

import java.util.Scanner;

public class EnglishMain {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		EnglishDAO dao = new EnglishDAO();
		// 1. 회원가입 로그인 종료
		System.out.println("영어단어 맞추기 게임을 시작합니다");

		while (true) {
			System.out.print("1.회원가입 2.로그인 3. 종료 : ");
			int input = sc.nextInt();
			if (input == 1) { // 회원가입
				System.out.print("아이디 입력 : ");
				String id = sc.next();
				System.out.print("비밀번호 입력 : ");
				String pw = sc.next();
				System.out.print("닉네임 입력 : ");
				String nick = sc.next();

				EnglishVO vo = new EnglishVO(id, pw, nick);
				int cnt = dao.memship(vo);
				if (cnt > 0) {
					System.out.println(id + "님 환영합니다");
				} else {
					System.out.println("회원가입에 실패했습니다");
				}
			} else if (input == 2) { // 로그인
				System.out.print("아이디 입력 : ");
				String id = sc.next();
				System.out.print("비밀번호 입력 : ");
				String pw = sc.next();
				
				EnglishVO vo = new EnglishVO(id, pw);
				EnglishVO info = dao.login(vo);
				
				if (info != null) {
					System.out.println(info.getNick()+"님 환영합니다");
					System.out.println("문제 갯수를 정하지 않았습니다 \n그만 풀고 싶으면 Stop 을 입력하세요");					
					System.out.println("희망하는 난이도의 번호를 입력하세요");
					while(true) {
					System.out.print("1.상 2.중 3.하 : ");
					int choice = sc.nextInt();
					if(choice == 1) {
						for(int i = 0; i<10; i++) {
							System.out.println(dao.high(vo));
							String answer = sc.next();
						}
					}else if(choice == 2) {
						
					}else if(choice == 3) {
						
					}else {
						System.out.println("잘못된 난이도를 입력 하였습니다 다시 선택해주세요");
					}
					}
				}else {
					System.out.println("로그인 실패 !");
				}
			} else if (input == 3) {
				System.out.println("수고하셧습니다 ~!");
				sc.close();
				break;
			} else {
				System.out.println("잘못 입력하셨습니다 다시 입력해주세요");
			}
		}
	}
}
