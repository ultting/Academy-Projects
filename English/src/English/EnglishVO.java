package English;

public class EnglishVO {
	private String id;
	private String pw;
	private String nick;
	private int score;
	private String number;
	
	@Override
	public String toString() {
		return "EnglishDAO [id=" + id + ", pw=" + pw + ", nick=" + nick + ", score=" + score + "]";
	}

	public EnglishVO(String id, String pw, String nick) {
		this.id = id;
		this.pw = pw;
		this.nick = nick;
	}
	

	public EnglishVO(String id, String pw) {
		this.id = id;
		this.pw = pw;
	}
	

	public EnglishVO() {
	}
	

	public String getNumber() {
		return number;
	}

	public void setNumber(String number) {
		this.number = number;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getPw() {
		return pw;
	}

	public void setPw(String pw) {
		this.pw = pw;
	}

	public String getNick() {
		return nick;
	}

	public void setNick(String nick) {
		this.nick = nick;
	}

	public int getScore() {
		return score;
	}

	public void setScore(int score) {
		this.score = score;
	}
	

}
