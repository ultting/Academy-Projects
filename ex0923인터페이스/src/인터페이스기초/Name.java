package 인터페이스기초;

public class Name extends Person implements Codable{
	
	//window -> show view -> git repositories
	// 내 레포지토리(개인공간) / 팀별 레포지토리
	// 레포지토리 -> 우클릭 -> import projects 
	//(repository 안에 있는 프로젝트를 가지고 올수 있는 방법)

	//commit push pull
	//충돌이 일어나지 않으려면
	//변경사항이 있다
	//commit -> pull
	
	@Override
	public void coding() {
		System.out.println("바뀌었나?");
	}

}
