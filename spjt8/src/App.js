import {useState,useEffect} from 'react';
import './css/Style.css';
import Movies from './comp/Movies.js'
import MovieForm from './comp/MovieForm.js';

function App() {

  const [movies, setMovies] = useState(
    [
      {'no':3, 'title':'아바타3', 'year':2006},
      {'no':2, 'title':'아바타2', 'year':2004},
      {'no':1, 'title':'아바타1', 'year':2022},
    ]
  );

  // 2. 데이터 삭제 : filter()
  // 삭제 할 pk(primary key) - no를 받아서 전달
  const delMovie = (no) =>{
    setMovies(
      movies.filter(
        (movie)=>{
          //결과를 충족한 데이터만 전달 됨(return). 
          // != : no와 다른 데이터만 전달
          // == : no와 같은 데이터만 전달
          return(movie.no != no)}
      )
    )
  };

  // 1. 리스트 출력 : 반복문 map()
  // map()함수는 배열에 있는 데이터를 1개씩 가져와 함수를 적용시켜줌.
  const renderMovies = 
    // 삼항식 - (조건)? 맞으면 : 틀리면
    movies.length?
    // 맞을 때 조건
    movies.map( (movie)=>{
      return(<Movies key={movie.no} movie={movie} delMovie={delMovie} />)
  }):
    // 틀릴 때 조건
    <div className="card">
        <div className="card-header"></div>
        <div className="card-body">
        <h5 className="card-title">데이터가 없습니다.</h5>
        </div>
    </div>
  ;
  
  // 3. 데이터 추가 : [...movies,{no:5, 'title':'아바타5', 'year':2022}]

  return (
    <div className="root">
      <h2>영화등록</h2>
      <MovieForm movies={movies} setMovies={setMovies} />
      

      <hr />
      {/* 영화리스트 */}
      <h2>영화리스트</h2>
      {renderMovies}

    </div>
  );
}

export default App;