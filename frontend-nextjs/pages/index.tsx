import Link from 'next/link';

const Home = () => {
    return (
        <>
            <h1>Bienvenido a Morrospace</h1>
            <Link href="/Morrospace">
                <a>Ir a Morrospace</a>
            </Link>
            {/* Otro contenido de tu página de inicio aquí */}
        </>
    );
};

export default Home;