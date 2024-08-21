import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';

function Article({title, image, description}) {
  return (
    <Card>
    <Card.Img variant="top" src={`http://127.0.0.1:8000${image}`} />
    <Card.Body>
      <Card.Title>{title.slice(0,40)}</Card.Title>
      <Card.Text>
        {description.slice(0,60)}
      </Card.Text>
      <Button variant="primary">Go somewhere</Button>
    </Card.Body>
  </Card>
  )
}

export default Article