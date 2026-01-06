import logo from './logo.svg';
import React,{useState,useEffect} from 'react';
import './App.css';
import './css/Style.css';

function App() {

  // useState변수
  const [cnt,setCnt] = useState(0); 

  let count = 0; // 일반변수

  const cntBtn = () => {
    // alert('확인');
    // useState 변수 값 출력방식
    setCnt(cnt + 1);
    console.log("cnt : ",cnt);
    // 일반변수값 출력
    console.log("count : ",count);
  }

  const countBtn = () => {
    // 일반변수 변수 값 출력방식
    count += 1;
    console.log("count : ",count);
  }

  return (
    <div className="root">
      <div className='txt' id='main'>{cnt}</div>
      <button onClick={cntBtn}>useState확인</button>
      <button onClick={countBtn}>일반변수확인</button>
    </div>
  );
}

export default App;
