
<%@page import="model.MemberVO"%>
<%@page import="model.MemberDAO"%>
<%@page import="model.ContentDAO"%>
<%@page import="model.ContentVO"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="description" content="">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- The above 4 meta tags *must* come first in the head; any other head content must come *after* these tags -->

    <!-- Title -->
    <title>JMTBOX - Contents is ALL in JMTBOX</title>

    <!-- Favicon -->
    <link rel="icon" href="img/core-img/favicon.ico">

    <!-- Stylesheet -->
    <link rel="stylesheet" href="style.css">
	<style type="text/css">
		 .search-container {
	    padding-top: 0px;
        margin-bottom: 2%;
    }
	    .search-title{
	    font-size: 10px;
	    font-weight:900;
	    text-align: center;
	    color:#000000;}
	    .search-input{
		position:relative;
		
		left:15%;
		width:66%;
		
		padding: 10px 10px 10px;
		margin-top: 25px;
		background-color: transparent;
        transition: transform 250ms ease-in-out;
        font-size: 20px;
        line-height: 18px;
        color: #575756;
        background-color: transparent;
        border-radius:50px;
        border: 1.5px solid #575756;
        
	    }
		.search-input::placeholder{
		text-algin:center;
		font-size:30px;
		}
		.oneMusic-albums{
		position: ;
		}
		
	</style>
</head>

<body class="dark-theme || light-theme">
	<% 
	request.setCharacterEncoding("UTF-8");
	response.setCharacterEncoding("UTF-8");
	response.setContentType("text/html;charset=UTF-8");
	MemberVO vo = (MemberVO)session.getAttribute("member");
	ArrayList<ContentVO> al = new ArrayList<ContentVO>();
	  System.out.println(al);
	  ContentDAO dao = new ContentDAO();
	  al = dao.imgShow();
	 
	 %>   
	 <!-- Preloader -->
    <div class="preloader d-flex align-items-center justify-content-center">
        <div class="lds-ellipsis">
            <div></div>
            <div></div>
            <div></div>
            <div></div>
        </div>
    </div>

    <!-- ##### Header Area Start ##### -->
    <header class="header-area">
        <!-- Navbar Area -->
        <div class="oneMusic-main-menu">
            <div class="classy-nav-container breakpoint-off">
                <div class="container">
                    <!-- Menu -->
                    <nav class="classy-navbar justify-content-between" id="oneMusicNav">

                        <!-- Nav brand -->
                        <a href="main.jsp" class="nav-brand"><img src="img/bg-img/logo.png" alt=""></a>

                        <!-- Navbar Toggler -->
                        <div class="classy-navbar-toggler">
                            <span class="navbarToggler"><span></span><span></span><span></span></span>
                        </div>

                        <!-- Menu -->
                        <div class="classy-menu">

                            <!-- Close Button -->
                            <div class="classycloseIcon">
                                <div class="cross-wrap"><span class="top"></span><span class="bottom"></span></div>
                            </div>

                            <!-- Nav Start -->
                            <div class="classynav">
                                <ul>
                                    <li><a href="main.jsp">Home</a></li>
                                    <li><a href="#">Game</a>
                                        <ul class="dropdown">
                                            <li><a href="gameAll.jsp">All game</a></li>
                                            <li><a href="gameRanPlay.jsp">Random game</a></li>
                                            <li><a href="gameMake.jsp">Make game</a></li>
                                        </ul>
                                    </li>
                                    <li><a href="albums-store.jsp">Search</a></li>
                                    <%if(vo!=null){ %>
                                    <li><a href="myPages/myPage.jsp">My</a></li>
                                    <%} %>
                                </ul>

                                <!-- Login/Register & Cart Button -->
                                <div class="login-register-cart-button d-flex align-items-center">
                                    <!-- Login/Register -->
                                    <div class="login-register-btn mr-50">
                                    <%if(vo==null){ %>
                                        <a href="login.html" id="loginBtn">Login / </a> 
                                        <a href="Register.jsp" id="loginBtn">Register</a>
                                        <%}else{ %>
                                        <a href="Logout" id="logoutBtn">Logout</a>
                                        <%} %>
                                    </div>

                                    <!-- Cart Button -->
                                    <div class="cart-btn">
                                        <p><span class="icon-shopping-cart"></span> <span class="quantity">1</span></p>
                                    </div>
                                </div>
                            </div>
                            <!-- Nav End -->

                        </div>
                    </nav>
                </div>
            </div>
        </div>
    </header>
    <!-- ##### Header Area End ##### -->

    <!-- ##### Breadcumb Area Start ##### -->
    <section class="breadcumb-area bg-img bg-overlay" style="background-image: url(img/bg-img/breadcumb3.jpg);">
        <div class="bradcumbContent">
            <p>See what’s new</p>
            <h2>New Season</h2>
        </div>
    </section>
    <!-- ##### Breadcumb Area End ##### -->
     
     
     
     
     <!-- 검색창 줄여어어어 -->
	<section class ="section-padding-100">

		<div class="search-container2">
				<div class="make-font">
					<h2>작품 검색</h2>
				</div>
				<div class="search-box-make">
					<!-- 검색 name값을 content_id로 잡아야하나?.. -->
					<input id="searchWord" class="search" type="text" placeholder="작품제목 및 태그 입력" name="search">
				</div>
		</div>
		

	</section>

	<!-- 우리작품이 뜨는 칸 (예시 latest-album에서가져와야되나? -->
	<section class="section-padding-100">
		<!-- 카테고리 -->
		<div class="content-list-container">
		
			<div id= "results" class="content-list-section">



			</div>
			
		</div>

	</section>
     
     
     
        <!-- 검색창 끝 -->
     
     
     
     
     
     
     
     
     
     
     
    <!-- ##### Album Catagory Area Start ##### -->
    <section id="flatform" class="album-catagory section-padding-100-0">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <div class="browse-by-catagories catagory-menu d-flex flex-wrap align-items-center mb-70">
                        <a href="#" data-filter="*">Browse All</a>
                        <a href="#" data-filter=".Naver" class="active">Naver</a>
                        <a href="#" data-filter=".wavve">wavve</a>
                        <a href="#" data-filter=".Netflix">Netflix</a>
                        <a href="#" data-filter=".Google">Google play Movies</a>
                        <a href="#" data-filter=".Disney">Diesney Plus</a>
                        <a href="#" data-filter=".Watcha">Watcha</a>
                        <a href="#" data-filter=".Amazon">Amazon Prime Video</a>
                        <a href="#" data-filter=".Cinema">Cinema</a>
                    </div>
                </div>
            </div>

            <div id="parent" class="row oneMusic-albums">
            	<%for(ContentVO mvo : al){ %>
            	<div class='col-12 col-sm-4 col-md-3 col-lg-2 single-album-item <%=mvo.getPlatform()%>'>
            		<div class='single-album'><img src='<%=mvo.getC_thumbnail()%>' alt=''>
            			<div class='album-info'>
            				<a href='#'>
            					<h5><%=mvo.getTitle() %></h5>
            				</a>
            				<p><%=mvo.getPlatform() %></p>
            			</div>
            		</div>
            	</div>
            	<%} %>
            </div>
            <button style="margin: auto; display: block;" id="more" class="btn oneMusic-btn">Load More</button>
        </div>
   
    </section>
    
    <!-- ##### Album Catagory Area End ##### -->

   

    <!-- ##### Footer Area Start ##### -->
    <footer class="footer-area">
        <div class="container">
            <div class="row d-flex flex-wrap align-items-center">
                <div class="col-12 col-md-6">
                    <a href="#"><img src="img/bg-img/logo.png" alt=""></a>
                    
                </div>

                <div class="col-12 col-md-6">
                    <div class="footer-nav">
                        <ul>
                            <li><a href="main.jsp">Home</a></li>
                            <li><a href="gameAll.jsp">Games</a></li>
                            <li><a href="albums-store.jsp">Search</a></li>
                        </ul>
                    </div>
                </div >
            </div>
        </div>
    </footer>
    <!-- ##### Footer Area Start ##### -->
	
    <!-- ##### All Javascript Script ##### -->
    <!-- jQuery-2.2.4 js -->
    <script src="js/jquery/jquery-2.2.4.min.js"></script>
    <!-- Popper js -->
    <script src="js/bootstrap/popper.min.js"></script>
    <!-- Bootstrap js -->
    <script src="js/bootstrap/bootstrap.min.js"></script>
    <!-- All Plugins js -->
    <script src="js/plugins/plugins.js"></script>
    <!-- Active js -->
    <script src="js/active.js"></script>
    <script type="text/javascript">
   		let rowNum=19;
   		
   		$('#more').on('click',function(){
    		console.log(rowNum);
    		$.ajax({
    			url : 'moreService',
    			type:'get',
    			data : {
    				data:rowNum
    			},
    			dataType : 'json',
    			success : function(result){
    				rowNum=rowNum+18
    				console.log(result)
    				result2 = [];
    				for(let i = 0; i < result.length; i++){
    				      result2.push(JSON.parse(result[i]));
    				   }
    				console.log(result2)
    				//$(this).attr('data-filter'); 클릭활성화 값 // 
    				for(let i = 0; i<result2.length;i++){
    					$('#parent').append("<div class='col-12 col-sm-4 col-md-3 col-lg-2 single-album-item "+result2[i].platform+"'><div class='single-album'><img src="+result2[i].c_thumbnail+" alt=''><div class='album-info'><a href='#'><h5>"+result2[i].title+"</h5></a><p>"+result2[i].platform+"</p></div></div></div>")
    					}
    				
    			},
    			error : function(){
    				console.log('실패')
    			}
    		})
    	})
    	
    	 $('.catagory-menu').on('click', 'a', function () {
                var filterValue = $(this).attr('data-filter');
                $('.oneMusic-albums').isotope({
                    filter: filterValue
                });
    	 });   
   		
   		//------검색------------------------------------------------------------------------------
 		$("#searchWord").keydown(function(key){
			if(key.keyCode == 13){
				let searchResult =[];
				$("#results").empty();
				let words = $("#searchWord").val();
				console.log(words)
			if(words != ''){
				$.ajax({
					url : 'SearchConByTitleOrTag',
					data : {searchWords : words},
					dataType : 'json',
					success : function(result){
						if(result.length>0){
							
							for(let i = 0; i < result.length; i++){
		      					searchResult.push(JSON.parse(result[i]));
		      					}
							let str = ''
							for (let i=0; i<result.length; i++){
								
								str += '<div class="single-album2"><div class="single-album-container2"><div class="img-center2"><a href="contentInfo.jsp?content_id='+searchResult[i].content_id+'"><img src="'+searchResult[i].c_thumbnail+'" alt=""></a></div></div><div class="album-info2"><p>'+searchResult[i].title+'</p></div></div>'
							
										
										
							}
							
							$('#results').append(str);
								
						}else{$("#results").append("");}
					},
					error : function(e){
						console.log('error'+e.status);
					}
				})
			}else{$("#results").html("")}
		}
	})
   		
   		
   		
   		
   		
    </script>
</body>

</html>