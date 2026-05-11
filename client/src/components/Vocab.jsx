import { useState } from 'react'
import { getVocabList } from '../utilities/vocabUtilities';

export default function Vocab() {
  const [vocabList, setVocabList] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setVocabList(null);
    console.log(e.target.lecture_url.value);
    try {
      const vocab = await getVocabList(e.target.lecture_url.value)
      setVocabList(vocab);
    } catch (error) {
      alert(error.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="flex items-center justify-center py-[2.5vmin] px-[1.5vmin] text-left">
      <div className="bg-[#1e5a7a] rounded-3xl px-[3.5vmin] py-[3vmin] w-[90%] max-w-4xl">

        <p className="text-[#fcf3f3] text-[2.5vmin] font-normal tracking-wide mb-[2vmin]">
          VOCAB LOOKUP
        </p>

        <form onSubmit={handleSubmit} className="flex gap-[1vmin] mb-[0.8vmin]">
          <input
            type="text"
            name="lecture_url"
            placeholder="Please enter the link for the lesson you would like vocab for....."
            className="bg-[#0f3147] border border-[#0f3147] text-white text-[1.8vmin] rounded-lg flex-1 px-[1.5vmin] py-[1vmin] placeholder-white/50 outline-none"
          />
          <button
            type="submit"
            className="bg-[#e7771e] border border-black text-white text-[2.1vmin] rounded-lg px-[2vmin] py-[0.8vmin] whitespace-nowrap"
          >
            Let's vocab!
          </button>
        </form>

        <div className="flex items-stretch gap-[1vmin] mb-[1.5vmin]">
          <div className="w-px bg-white/50 shrink-0" />
          <p className="text-white text-[2vmin] py-[0.5vmin]">
            A quick and easy way to get vocab for a lecture from the Code Platoon curriculum
          </p>
        </div>

        <div className="bg-[#0f3147] rounded-lg h-[18vmin] overflow-y-auto">
          {loading && (
            <div className="h-full flex items-center justify-center">
              <p className="text-[#bcacac] text-[2.5vmin]">Loading...</p>
            </div>
          )}
          {!loading && vocabList && (
            <ul className="divide-y divide-white/30 border border-white/30 rounded-lg">
              {vocabList.map((item, index) => (
                <li key={index} className="grid grid-cols-[22vmin_1fr] text-white text-[1.8vmin]">
                  <span className="px-[1.5vmin] py-[1vmin] border-r border-white/30">{item.term}</span>
                  <span className="px-[1.5vmin] py-[1vmin]">{item.definition}</span>
                </li>
              ))}
            </ul>
          )}
          {!loading && !vocabList && (
            <div className="h-full flex items-center justify-center">
              <p className="text-[#c7b1b1] text-[1.9vmin]">enter lecture url..</p>
            </div>
          )}
        </div>

      </div>
    </div>
  )
}
