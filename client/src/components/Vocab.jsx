import { useState } from 'react'
import { getVocabList } from '../utilities/vocabUtilities';

export default function Vocab() {
  const [vocabList, setVocabList] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("Submitting form with lecture_url:", e.target.lecture_url.value);
    const vocab = await getVocabList(e.target.lecture_url.value);
    if (!vocab) {
      alert("Failed to fetch vocab list. Please try again.");
      return;
    }
    else{
        setVocabList(vocab);
    }
  }

  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center" }}>
        <h1>Vocab loookup</h1>
        <form onSubmit={handleSubmit}>
            <input type="text" name="lecture_url" placeholder=' Please enter the link for the lesson you would like vocab for..' />
            <button type='submit' >Let's Vocab!</button> 
        </form>
        <div style={{ maxHeight: "30vmin", overflow: "auto" , maxWidth: "80vmin" }}>
            {
                vocabList ? (
                    <ul>
                        {vocabList.map((item, index) => (
                            <li key={index}>
                                <h6><strong>{item.term}:</strong> {item.definition}</h6>
                            </li>
                        ))}
                    </ul>
                ) : null
            }
        </div>    
    </div>
  )

}
