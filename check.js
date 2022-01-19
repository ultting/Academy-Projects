 	let email=0;
    let nick=0;
    let pw=0;   
    $('#exampleInputEmail1').focusout(function(){
			let exampleInputEmail1 = $('#exampleInputEmail1').val()
			$.ajax({
				url : "CheckId",
				type : "post",
				data : {"exampleInputEmail1":exampleInputEmail1},
				dataType: "json",
				success : function(data){
					result = data
					console.log(result)
					if(result == 0){
						$('#emailHelp').css('color','red')
						$('#emailHelp').text('이미 존재하는 아이디 입니다.')
						email = 0
					}else{
						$('#emailHelp').css('color','green')
						$('#emailHelp').text('사용가능한 아이디 입니다.')
						email = 1
					}
				},
				error:function(){
					console.log('서버요청실패')
				}
			})
		})
	
		//닉네임 중복체크
	$('#exampleInputNick1').focusout(function(){
		let exampleInputNick1 = $('#exampleInputNick1').val()
		$.ajax({
			url:"CheckNick",
			type : "post",
			data : {"exampleInputNick1":exampleInputNick1},
			dataType : "json",
			success : function(data){
				result2 = data
				if(result2 == 0){
					$('#nickHelp').css('color','red')
					$('#nickHelp').text('이미 존재하는 닉네임 입니다.')
					nick = 0
				}else{
					$('#nickHelp').css('color','green')
					$('#nickHelp').text('사용가능한 닉네임입니다')
					nick = 1;
				}
			}
		})
	})
  	//비밀번호 확인
	function check_pw(){
		let pw = document.getElementById('exampleInputPassword1').value
		let pw2 = document.getElementById('exampleCheckPassword1').value
		if(pw!=''&&pw2!=''){
			if(pw==pw2){
				document.getElementById('pwcheck').innerHTML='비밀번호가 일치합니다'
				document.getElementById('pwcheck').style.color='green'
				pw = 1;
			}else{
				document.getElementById('pwcheck').innerHTML='비밀번호가 일치하지 않습니다'
				document.getElementById('pwcheck').style.color='red'
				pw = 0;
			}
			return pw
		}
	}
    
    $("#regi").on("click",function(e){
    	
    	pw = check_pw()
    	if(email==1&&nick==1&&pw==1){
    		alert("회원가입 완료")
    	}else{
    		alert("오류 확인")
    		e.preventDefault()
    	}
    	
    });