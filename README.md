# Academy-Projects
- Spring ( basic.jsp )
  * 스프링 MVC 패턴으로 만든 동적 웹 게시판
  - 2가지의 컨트롤러가 존재
   1. @Controller // 리턴이 2가지 foward -> jsp // redirect -> controller // json
   2. @RestController ( json 전용 annotation)// 리턴 : json
   3. ![image](https://user-images.githubusercontent.com/91230329/150886384-b05574f3-37b4-4254-97af-6a19b4562dd7.png)
  - 스프링 DB연결을 위한 Dependency
  1. DBCP HikariCP

  2. MySQL Driver
    
  3. SqlSessionFactoryBean API(mybatis-spring)
     
  4. MyBatis(SqlSession..) API(mybatis)

  5. spring-jdbc API
     
- Python
  * 웹 크롤링 코드
  * Naver API 활용하여 텍스트 추출 및 영상 합친 뒤 송출
- Project

      OTT 정보제공 및 추천 사이트
      
  1. 웹에 보여주기 위한 정보 웹 크롤링
  2. 로그인 및 회원가입 구현
  3. 더보기 버튼 구현
 
      청각장애인들을 위한 코딩교육 번역 서비스 
      
    유튜브링크를 입력받은 후 영상 다운로드
   -> 영상 오디오 추출   
   -> 오디오 텍스트화 (구글 speech api / kako REST api / naver 는 유료)   
   -> 텍스트 konlpy 자연어 처리 및 토큰화    
   -> Json 파일 수어영상 매칭 후 view 

  
  1. 다양한 단어에 대한 수어 영상 크롤링
  2. 영상 음성 번역 후 수어 영상 제작
  3. 제작 완료된 영상 플라스크 서버를 이용해서 웹 으로 전송
