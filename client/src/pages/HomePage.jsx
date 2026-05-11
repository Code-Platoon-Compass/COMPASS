import CheckIn from "../components/widgets/CheckIn";
import Vocab from "../components/Vocab";
import DailyLinks from "../components/widgets/DailyLinks";


const HomePage = () => {

  return (
    <>
      <h1>hi i'm the homepage</h1>
      <Vocab /> 
      <CheckIn url="https://example.com" />
      <DailyLinks url="/api/links" />
    </>
  );
};

export default HomePage;
