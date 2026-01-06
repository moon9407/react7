import logo from './logo.svg';
import React,{useState,useEffect,useRef} from 'react';
import './App.css';
import './css/Style.css';

function App() {

  // useState변수 - 특징 : 값이 변경되면 화면이 다시렌더링(갱신)된다.
  const [cnt,setCnt] = useState(0); 
  const [id,setId] = useState('aaa'); 
  // useRef변수 - 특징 : 값이 변경되어도 화면이 다시렌더링(갱신)되지 않는다. 렌더링 되더라도 값이 유지됨.
  // useRef : current 키에 값을 저장. cntRef.current
  const cntRef = useRef(10);

  // useEffect : 화면이 렌더링(처음로딩 및 갱신)될 때 특정코드를 실행시키는 함수
  useEffect(
    ()=>{
      console.log("최초 실행 시 실행.");
    },[cnt]
  );
  // 최초 1회만 실행됨.
  useEffect(
    ()=>{
      console.log("1회만 실행.");
    },[]
  );


  let count = 0; // 일반변수 - 특징 : 값이 변경되어도 화면이 다시렌더링(갱신)되지 않는다. 렌더링 되면 값이 초기화된다.

  // useState 변수 값 출력방식
  const cntBtn = () => {
    // alert('확인');
    setCnt(cnt + 1);
    // useState변수값 출력
    console.log("cnt : ",cnt);
    // 일반변수값 출력
    console.log("count : ",count);
    // useRef변수값 출력
    console.log("refcount : ",cntRef.current);
  }

  // 일반변수 변수 값 출력방식
  const countBtn = () => {
    count += 1;
    console.log("count : ",count);
    // useState변수 - rendering
    setId('bbb'+count);
    console.log("id",id);
  }

  // useRef 변수 값 출력방식
  const refBtn = () => {
    cntRef.current += 1;
    console.log("refcount : ",cntRef.current);
  }

  return (
    <div className="root">
      <div className='txt' id='main'>{cnt}</div>
      <button onClick={cntBtn}>useState확인</button>
      <button onClick={countBtn}>일반변수확인</button>
      <button onClick={refBtn}>useRef확인</button>
    </div>
  );
}

export default App;
