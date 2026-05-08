import CheckIn from "../components/widgets/CheckIn";
import Vocab from "../components/Vocab";
import { useOutletContext } from 'react-router-dom';
import AuthForm from '../components/AuthForm';

const HomePage = () => {
    const { user, setUser } = useOutletContext();

    return (
        <>
            <h1>hi i'm the homepage</h1>
            <Vocab /> 
            <CheckIn url="https://example.com" />
            {user ? <p>Signed in as {user.email}</p> : null}
            <AuthForm setUser={setUser} />
        </>
    );
}

export default HomePage;
