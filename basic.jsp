<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix='c' %>

<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=de70eff6b393d87ce3675c11af0a13ff"></script>
  <script type="text/javascript">
  	
  	$(document).ready(()=> {
  		// 게시판 리스트 가져오기
  		loadList()
  	})
  	
  	function loadList(){
  		//Controller 에게 게시판리스트를 요청하기(boardAjaxList.do)
  		$.ajax({
  			url : "boardAjaxList.do", // -> 요청 -> 받는데이터 : json
  			type: "get",
  			dataType: "json",
  			success:resultHtml,
  			error:function(){
  				alert("erroriouoiu")
  			}
  		})
  	}
  	
  	function resultHtml(jsonList){ // jsonList -> 
  		let view = "<table class='table table-hover table-bordered'>"
  		view+="<tr>"
  		view+="<td>번호</td>"
  		view+="<td>제목</td>"
  		view+="<td>작성자</td>"
  		view+="<td>작성일</td>"
  		view+="<td>조회수</td>"
  		view+="<td>수정</td>"
  		view+="<td>삭제</td>"
  		view+="</tr>"
  		$.each(jsonList,(index, obj)=>{
  			view+="<tr>"
  		  	view+="<td id='i"+index+"'>"+obj.idx+"</td>"
  		  	view+="<td id='t"+obj.idx+"'><a href='javascript:goView("+index+")'>"+obj.title+"</a></td>"
  		  	view+="<td id='w"+obj.idx+"'>"+obj.writer+"</td>"
  		  	view+="<td>"+obj.indate.split(" ")[0]+"</td>"
  		  	view+="<td id='c"+index+"'>"+obj.count+"</td>"
  		  	if(${!empty userInfo}){
  		  		if("${userInfo.userId}"==obj.userId){ // 더블쿼테이션...........
  		  			view+="<td id = 'u"+obj.idx+"'><button class='btn btn-primary btn-sm' onclick='goUpdate2("+obj.idx+")'>수정</button></td>"
  		  			view+="<td><button class='btn btn-danger btn-sm' onclick='goDel("+obj.idx+")'>삭제</button></td>"
  		  		}else{
	  		  		view+="<td id = 'u"+obj.idx+"'><button disabled class='btn btn-primary btn-sm' onclick='goUpdate2("+obj.idx+")'>수정</button></td>"
  			  		view+="<td><button disabled class='btn btn-danger btn-sm' onclick='goDel("+obj.idx+")'>삭제</button></td>"
  		  		}
  		  	}else{
  		  		view+="<td id = 'u"+obj.idx+"'><button disabled class='btn btn-primary btn-sm' onclick='goUpdate2("+obj.idx+")'>수정</button></td>"
  		  		view+="<td><button disabled class='btn btn-danger btn-sm' onclick='goDel("+obj.idx+")'>삭제</button></td>"
  		  	}
  		  	
  		  	
  		  	view+="</tr>"
  		  	view+="<tr id='cv"+index+"' style='display:none'>"
  		  	view+="<td>내용</td>"
  		  	view+="<td colspan='4'><textarea rows='7' id='c"+obj.idx+"' class='form-control'>"+obj.contents+"</textarea>"
  		  	view+="<br>"
  		  	if(${!empty userInfo}){
  		  		if("${userInfo.userId}"==obj.userId){
  		  			view+="<button class='btn btn-primary btn-sm' onclick='goUpdate("+obj.idx+")'>수정</button>&nbsp;&nbsp;"
  		  		}else{
  		  		view+="<button disabled class='btn btn-primary btn-sm' onclick='goUpdate("+obj.idx+")'>수정</button>&nbsp;&nbsp;"
  		  		}
  		  	}else{
  		  		view+="<button disabled class='btn btn-primary btn-sm' onclick='goUpdate("+obj.idx+")'>수정</button>&nbsp;&nbsp;"
  		  	}
  		  	view+="<button class='btn btn-info btn-sm' onclick='winClose("+index+")'>닫기</button>"
  		  	
  		  	view+="</td>"
  		  	view+="<td colspan='2'>";
  		  	view+="<div id='map"+index+"' style='width:500px;height:400px;'></div>"
            view+="</td>";
  		  	view+="</tr>"
  		})
  		if(${!empty userInfo}){
  			view+="<tr>"
  			view+="<td colspan='7'>"
  			view+="<button class='btn btn-primary btn-sm' onclick='goWrite()'>글쓰기</button>"
  			view+="</td>"
  			view+="</tr>"
  			view+="</table>"
  		}
  		
        
  		$('#list').html(view)
  	}
  	

  	function updateFn(idx){
  		let title = $('#nt'+idx).val()
  		let writer = $('#nw'+idx).val()
  		$.ajax({
  			url:'boardAjaxTitleWriterUpdate.do',
  			type:'post',
  			data:{'idx':idx,'title':title,'writer':writer},
  			success:loadList,
  			error:()=> {
  				alert('error55')
  			}
  		})
  	}
  	
  	function goUpdate2(idx){
  		let oldTitle=$('#t'+idx).text()
  		let oldWriter = $('#w'+idx).text()
  		
  		let newTitle = "<input type='text' id='nt"+idx+"' class='form=control' value='"+oldTitle+"'>"
  		$('#t'+idx).html(newTitle)
  		
  		let newWriter = "<input type='text' id='nw"+idx+"' class='form=control' value='"+oldWriter+"'>"
  		$('#w'+idx).html(newWriter)
  		  		
  		let newUpdate = "<button class='btn btn-primary btn-sm' onclick='updateFn("+idx+")'>수정하기</button>"
  		$('#u'+idx).html(newUpdate)
  	}
  	
  	function goDel(idx){
  		$.ajax({
  			url : 'boardAjaxDelete.do',
  			type: 'get',
  			data: {"idx":idx},
  			success:loadList,
  			error: ()=> {
  				alert('error44')
  			}
  		})	
  	}
  	
  	function goUpdate(idx){ // 내용수정
  		let contents = $('#c'+idx).val()
  		$.ajax({
  			url : 'boardAjaxContentUpdate.do',
  			type : 'post',
  			data : {"idx":idx,"contents":contents},
  			success:loadList,
  			error:function(){
  				alert('error33')
  			}
  		})
  	}
  	
  	function winClose(index){
  		$("#cv"+index).css('display','none')
  	}
  	
  	function goView(index){
  		let idx = $("#i"+index).text()
  		

  		if($("#cv"+index).css('display')=='none'){ // div에 걸린게 아닌 table태그에 걸렸을 시 table-row 사용 
	  			$('#cv'+index).css('display','table-row')
				var container = document.getElementById('map'+index);
         		var options = {
            		center: new kakao.maps.LatLng(33.450701, 126.570667),
            		level: 3
         		};

         		var map = new kakao.maps.Map(container, options);

	  			$.ajax({
	  				url : "boardAjaxCount.do",
	  				type : 'get',
	  				data : {"idx": idx},
	  				success : (data)=> {  				
	  					let count = $("#c"+index).text(data.count)
	  				},
	  				error : ()=> {
	  					alert("error22")
	  				}
	  			})
	  	}else{
	  		$('#cv'+index).css('display','none')  			
	  	}
  	}
  	
  	function goWrite(){
  		$('#list').css('display','none')
  		$('#write').css('display','block')
  	}
  	
  	function goInsert(){
  		//let frm = $('#frm').serialize()
  		$.ajax({
  			url : 'boardAjaxInsert.do',
  			type : 'post',
  			data : $('#frm').serialize(),
  			success:loadList,
  			error:function(){
  				alert("error11")
  			}
  		})
  		$('#cancle').trigger("click")
  		$('#list').css('display','block')
  		$('#write').css('display','none')
  	}
  	
  	function goList(){
  		if($('#write').css('display') == 'block'){
  			$('#list').css('display','block')
  	  		$('#write').css('display','none')  			
  		}else if ($('#write').css('display')=='none'){
  			$('#list').css('display','none')
  	  		$('#write').css('display','block')
  		}
  		
  	}
  	
  	function loginFn(){
  		let id = $("#userId").val()
  		let pw = $("#userPwd").val()
  		if(id==""){
  			alert("아이디를 입력하세요")
  			$("#userId").focus()
  			return false;
  		}
  		
  		if(pw==""){
  			alert("패스워드를 입력하세요")
  			$("#userPwd").focus()
  			return false;
  		}
  		$("#frm").submit()
  	}
  </script>
</head>
<body>
 
<div class="container">
  <h2>Spring Web MVC03</h2>
  <div class="panel panel-default">
    <div class="panel-heading">
    	<c:if test="${empty userInfo }">
		<form id="frm" class="form-inline" action="login.do" method="post">
  		<div class="form-group">
    		<label for="userId">ID:</label>
    		<input type="text" class="form-control" id="userId" name="userId">
  		</div>
  		<div class="form-group">
    		<label for="userPwd">Password:</label>
    		<input type="password" class="form-control" id="userPwd" name="userPwd">
  		</div>
  		<button type="button" class="btn btn-default btn-sm" onclick="loginFn()">로그인</button>
		</form>
		</c:if>
		<c:if test="${!empty userInfo }">
		<form action="logout.do" method="get">
			<div class="form-group">
				<label>${userInfo.userName } 님 방문을 환영합니다.</label>
				<button type="submit" class="btn btn-primary btn-sm">로그아웃</button>
			</div>
		</form>
		</c:if>
	</div>
   	
    <div class="panel-body" id="list" style="display:block"></div>
    <div class="panel-body" id="write" style="display:none">
    	<form class="form-horizontal" id="frm">
    		<input type="hidden" name="userId" value="${userInfo.userId }">
  			<div class="form-group">
    			<label class="control-label col-sm-2" for="title">제목</label>
    			<div class="col-sm-10">
      				<input type="text" class="form-control" id="title" name="title" placeholder="제목을 입력하세요">
    			</div>
  			</div>
  			<div class="form-group">
    			<label class="control-label col-sm-2" for="writer">작성자:</label>
    		<div class="col-sm-10">
      			<input type="text" class="form-control" id="writer" name="writer" value="${userInfo.userName }" readonly="readonly"> 
    		</div>
  			</div>
  			<div class="form-group">
    			<label class="control-label col-sm-2" for="pwd">내용</label>
    		<div class="col-sm-10">
      			<textarea rows="7" class="form-control" id="contents" name="contents"></textarea>
    		</div>
    		</div>
  			<div class="form-group">
    		<div class="col-sm-offset-2 col-sm-10">
      		<button type="button" class="btn btn-default" onclick="goInsert()">글쓰기</button>
      		<button type="reset" class="btn btn=default" id="cancle">취소</button>
      		<button type="button" class="btn btn-default" onclick="goList()">뒤로가기</button>
    		</div>
  			</div>
		</form>
    </div>
    <div class="panel-footer">빅데이터 분석서비스 개발자과정(꿀벌)</div>
  </div>
</div>

</body>
</html>