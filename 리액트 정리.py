# ================================================================
## 기본 react 프로젝트 생성 및 실행 방법
# 1.cmd창 관리자 권한으로 실행
# 2. npx create-react-app spjt1 로 프로젝트 생성
# 3. cd spjt1 로 프로젝트 폴더 이동
# 3-1 npm install axios 설치
# 3-2 npm install react-router-dom 설치
# 4. npx start 명령어로 리액트 개발 서버 실행
#=================================================================

#=================================================================
## 수업 시작 시 프로젝트 생성 방법
# 1.cmd창 관리자 권한으로 실행
# 2. npx create-react-app spjt10 로 프로젝트 생성
# 3. cd spjt10 로 프로젝트 폴더 이동
# 3-1 npm install axios 설치
# 3-2 npm install react-router-dom 설치
# 4. npx start 명령어로 리액트 개발 서버 실행
# 5. public폴더에 images폴더 생성
# 6. src폴더에 comp,css폴더 생성
# 6-1 css폴더에 Style.css파일 생성, comp폴더는 컴포넌트 저장할때 알아서.
# 7. public/index.html에서 Bootstrap 링크 복사 후 적용
# 8. src/index.js에서 BrowserRouter로 App컴포넌트 감싸기 
# 8-1 import { BrowserRouter } from 'react-router-dom'; 상단 추가 후 
# 8-2 root.render( <BrowserRouter> <App /> </BrowserRouter> ); 형식으로 변경
# 9. src/App.js에서 css/Style.css 불러오기
# 10. 지울부분 지우기
#=================================================================

#=================================================================
## console 창에서 로그 2번출력 삭제
# index.js 파일에서 </React.StrictMode> 태그 지우기

#=================================================================
## 리액트에서 Bootstrap적용 방법
# 1. public폴더의 index.html에서
#    <head>태그 상단에 viewport메타태그 위에
#    https://www.bootstrapcdn.com/에서 복사한 주소 붙여넣기
# 2. 리액트 컴포넌트에서 Bootstrap클래스 사용
#    https://getbootstrap.com/ 에서 원하는 js파일에 코드 복사 후 붙여넣기
#=================================================================

#=================================================================
## App.js 가 메인페이지 ex) base.html 역할
# <br> 태그는 <br /> 형식으로 만들어야함
# jsx문법에서는 className,onClick 등 카멜표기법 사용
# 카멜표기법 : 단어 첫글자는 소문자, 이후 단어 첫글자는 대문자
#=================================================================

#=================================================================
## 리액트에서 image적용 방법
# 1-1.public에 images폴더 생성 후 이미지 저장
# 1-2<img src='/images/dog1.jpg'/> 형식으로 사용
# 2-1 src폴더에 이미지 저장
# 2-2 import i500 from './500.png' 형식으로 불러오기
# 2-3 <img src={i500} /> 형식으로 사용

# cmd 창에서 img elements must have an alt prop 이런 오류 뜨는 상황
# 구글은 이미지를 “보지 못함”
# 👉 alt를 읽어서 이미지가 뭔지 판단
# 따라서 이미지에 대한 설명을 alt 속성에 넣어줘야 함
# <img src="/images/banner.png" alt="메인 페이지 배너 이미지" /> 처럼 넣으면 페이지 검색 시 접근성 up
# <img src="/images/decor.png" alt="" /> 설명필요 없는 사진이면 이런식으로 넣으면 됌.
# 키워드는 아님, 단지 이미지 설명용으로 사용하면 SEO에 도움됨.
#=================================================================

#=================================================================
## 리액트에서 css적용 방법
# 1.src폴더에 css폴더 생성 후 css저장
# 2.App.js에서 import './css/style.css'; 형식으로 불러오기
#=================================================================

#================================================================
## 리액트에서 변수선언 및 값 변경 방법
# 1.일반 변수선언 및 값 변경 방법
#   let id = 'aaa';
#   id = 'bbb'; //값 변경
#   console.log("aaa 변수 값 변경 :", id);

# 값 변경 후 화면에 바로 출력이 안되기 때문에 값 변경 후 변경된 값을 화면에 출력하려면 
# 화면이 다시 렌더링 된 후 사용해야 함.
# useState변수는 값 변경 시 화면이 다시 렌더링되기 때문에 바로 변경된 값을 화면에 출력할 수 있음.

# 2.useState변수선언 및 값 변경 방법
#   //상단에 import문에 추가
#   import { useState } from 'react';
#   //변수선언
#   const [userId, setUserId] = useState('aaa'); 
#   //값 변경
#   setUserId('bbb');
#   //값 출력
#   console.log("aaa useState변수 :", userId);
# 다만 console.log로 출력할 때는 값 변경 후 바로 출력하면 변경 전 값이 출력됨.

# 3.useRef변수선언 및 값 변경 방법
#   import { useRef } from 'react'; 상단에 추가
#   const userIdRef = useRef('aaa'); //변수선언
#   userIdRef.current = 'bbb'; //값 변경
#   console.log("aaa useRef변수 :", userIdRef.current); //값 출력
# 다만 console.log로 출력할 때는 값 변경 후 바로 출력하면 변경 전 값이 출력됨.
# useRef변수는 값 변경 시 화면이 다시 렌더링되지 않기 때문에 값 변경 후 변경된 값을 
# 화면에 출력하려면 화면이 다시 렌더링 된 후 사용해야 함.

# 4.useEffect함수 사용 방법
#   import { useEffect } from 'react'; 상단에 추가
#   useEffect( () => {
#       //화면이 렌더링(처음로딩 및 갱신)될 때 실행할 코드 작성
#   } );
# 다만 useEffect함수는 화면이 렌더링(처음로딩 및 갱신)될 때마다 실행되기 때문에 
# 특정 변수값이 변경될 때만 실행되도록 하려면 두번째 인수로 배열을 전달.
#   useEffect( () => {
#       //특정변수값이 변경될 때 실행할 코드 작성
#   }, [특정변수] );
#================================================================

#================================================================
## 리엑트에서 axios사용 방법
# 1.cmd창에서 npm install axios 명령어로 axios설치 (프로젝트 만들때마다 설치해야함 최초 1회)
# 2.리액트 컴포넌트 상단에 import axios from 'axios'; 작성
# 3.axios.get/post/put/delete 메서드로 비동기 통신 처리
# axios.get('url주소')
#   .then( (response) => {
#       //통신 성공 시 처리할 코드 작성
#   } )
#   .catch( (error) => {
#       //통신 실패 시 처리할 코드 작성
#   } );
#================================================================

#================================================================
## 리엑트에서 라우터 사용 방법
# 1.cmd창에서 npm install react-router-dom 명령어로 라우터설치 (프로젝트 만들때마다 설치해야함 최초 1회)
# 2.리액트 컴포넌트 상단에 import { BrowserRouter , Route, Routes } from 'react-router-dom'; 작성
# 2-1 BrowserRouter : 라우터 기능을 사용하기 위한 태그
# index.js 에 import { BrowserRouter } from 'react-router-dom'; 상단에 추가
# root.render(
#   <BrowserRouter>
#     <App />
#   </BrowserRouter>
# );
# 이렇게 아니면 app.js에서 감싸도 됨.
# 
# 2-2 Route : 경로별 컴포넌트를 연결하기 위한 태그
# <Route>태그로 경로별 컴포넌트 연결하기
#    한개일때
#    ex) 
#    <>
#       <Route path="/BList" element={<BList />} />
#    </>
# 2-3 Routes : 라우터로 처리할 컴포넌트를 감싸기 위한 태그
#    여러개일때
#    ex)
#    <>
#       <Routes>
#           <Route path="/BList" element={<BList />} />
#           <Route path="/BWrite" element={<BWrite />} />
#           <Route path="/BView" element={<BView />} />
#       </Routes>
#    </>
#================================================================

#================================================================
## 리엑트에서 링크 사용 방법
# 1.리액트 컴포넌트 상단에 import { Link } from 'react-router-dom'; 작성
# 2.<a>태그 대신 <Link>태그로 링크 작성
#    ex) <Link to="/BList">게시판리스트</Link>
#    ex) <Link className="navbar-brand" to="/">HOME</Link> 클래스명 사용 시 
#================================================================

#================================================================
## 리엑트에서 컴포넌트 처리 방법
# 1.src폴더에 comp폴더 생성
# 2.comp폴더에 js파일 생성 후 컴포넌트 작성 (항상 마지막에 export default 파일이름; 형식으로 작성)
# 3.App.js에서 상단에 import문으로 불러오기 ex) import Nav from './comp/Nav';
# 4.App.js에서 컴포넌트 태그로 사용하기 ex) <Nav />

## 컴포넌트에서 props값 전달 방법
# 1.App.js에서 컴퍼넌트 태그에 속성으로 값 전달 ex) <Number btnName={"확인"} />
# 2.컴포넌트에서 전달된 props값 받기
#   방법1: const Number = (props) => { ... props.btnName ... }
#   방법2: const Number = ({btnName}) => { ... btnName ... }
# 3.컴포넌트에서 props값 사용하기
#    ex) <button>{props.btnName}</button> 또는 <button>{btnName}</button>
# 4.컴포넌트에서 props값 여러개 전달받기
#    방법1: const Number = (props) => { ... props.btnName, props.number ... }
#    방법2: const Number = ({btnName, number}) => { ... btnName, number ... }
# 5.컴포넌트에서 props값으로 함수, useState변수 등도 전달 가능
#   ex) <Number btnName={btnName} number={number} />
#================================================================



