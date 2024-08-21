import './App.css'
import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from 'react';
import getNewsFromServer from './store/article-action';
import Article from './components/Article';
import { Container, Row, Col } from 'react-bootstrap';

function App() {

  const news =  useSelector((state) => state.data);
  const dispatch = useDispatch();

  console.log(news);

  useEffect(() =>{
    dispatch(getNewsFromServer());
  },[dispatch]);

  return (
    <Container>
      <Row>
        {news.map((item) => 
        
        (
          <Col xl={3} lg={4} md={6} sm={12} className='py-2'>
          <Article title={item.title} image={item.image} description={item.description} />
          </Col>
        )
        )}
      </Row> 
    </Container>
  )
}

export default App
