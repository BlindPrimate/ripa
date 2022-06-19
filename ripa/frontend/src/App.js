import logo from './logo.svg';
import './App.css';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav'

function App() {
    return (
        <div>
            <Navbar bg="light">
                <Container>
                    <Navbar.Brand href="#home">Ripa</Navbar.Brand>
                    <Nav.Link href="#home">Projects</Nav.Link>
                    <Nav.Link href="#issues">Issues</Nav.Link>
                    <Nav.Link href="#issues">Releases</Nav.Link>
                </Container>
            </Navbar>
            <Container>
            </Container>
        </div>
    );
}

export default App;
