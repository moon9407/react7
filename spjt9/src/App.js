import './App.css';
import './css/Style.css';
import axios from 'axios'  //ajax
import { useState,useEffect } from 'react';

function App() {

  //자바스크립트 일반변수 - 변수값을 변경할 수 있지만 ,. html에 반영이 안됨. 리로드 되면 값이 리셋됨.
  // const uuuser = 'aaa';

  //useState() : 데이터가 변경이 되면 html페이지에 반영해주는 변수
  const [users, setUsers] = useState([]);

  //useEffect() : 리로딩이 되면 실행되는 함수, 최초 1번만 실행
  //axios 사용해서 서버에 있는 데이터를 호출
  useEffect(
    ()=>{
      axios.get('http://localhost:8000/member/userAll/',{params:{id:'aaa',name:'홍길자'}})
      .then(res => {
        console.log("json 데이터 : ",res)
        setUsers(res.data.arr);
      })
    },[]
  )

  // useEffect(
  //   axios({
  //     method : 'get',
  //     url : 'https://jsonplaceholder.typicode.com/users',
  //     data : {},
  //   }).then( (data)=>{console.log("성공");
  //     }).catch((error) =>{
  //       console.log("실패");
  //     })
  // );//useEffect


  const user_list = users.map((user)=>{
    return (
      <div className="card" key={user.id}>
        <div className="card-header">번호 : {user.id}</div>
        <div className="card-body">
          <h5 className="card-title">이름 : {user.name}</h5>
          <p className="card-text">번호 : {user.phone}</p>
          <button className="btn btn-primary">수정</button>
          <button className="btn btn-primary">삭제</button>
        </div>
      </div>
    )
  });



  return (
    <div className="root">
      <h2>회원리스트</h2>
      {user_list}
    </div>
  );
}

export default App;
