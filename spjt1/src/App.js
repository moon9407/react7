import './css/Style.css';
import i500 from './500.png'



function App() {

  // css문법을 내부링크 방식.(잘 안함)
  // 잘 안하는 이유 : 문법구조가 다름. style-{title1} 변수를 입력해서 적용시켜야함
  // 권장하는 방법 : 외부링크 방식(css파일로 분리)
  // var : 예전버전의 변수선언
  // let : 최근버전의 변수선언
  // const : 최근버전의 상수(변하지 않는 값)선언
  const title1 = {
    // textAlign : 'center',
    // backgroundColor : 'yellow',
    // fontSize : '40px'
  }

  return (
    <>
      <div className="App">
        <div></div>
        <h2 className='main'>메인페이지</h2>
        {/* src폴더에서 import사용방법 */}
        <img src={i500} />
        {/* public폴더에서 절대경로 사용방법 */}
        <img src='/images/dog1.jpg'/> 
        
      </div>
    </>
  );
}

export default App;
