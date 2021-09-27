package 인터페이스기초;

public interface Codable {
	// 인터페이스 특징
	// 1. 객체 생성이 불가능하다.
	// 2. 추상메소드만 가질 수 있다. (abstract)
	// 자바8버전 -> default or static 키워드를 추가하면 일반 메소드도 가지고 있을 수 있다.
	// 3. 필드 안에 반드시 상수(final)만 가질 수 있다.

	public void coding(); // abstract 키워드 생략 가능

}
