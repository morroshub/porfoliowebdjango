// pages/index.tsx (o cualquier otra página)
import Navbar from '../components/navbar';

const Home: React.FC = () => {
  return (
    <div>
      <Navbar />
      <h1>Home Page</h1>
      {/* Contenido de la página */}
    </div>
  );
};

export default Home;
