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
    <div className="px-6 py-4">
      <div className="bg-white border border-gray-200 rounded-xl overflow-hidden">

        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-gray-200">
          <span className="text-[#e7771e] text-xs font-semibold tracking-widest uppercase">
            Curriculum Vocab Generator
          </span>
          <span className="text-gray-400 text-xs">AI-powered · Paste a curriculum URL</span>
        </div>

        {/* Input + Button */}
        <div className="px-6 py-4">
          <form onSubmit={handleSubmit} className="flex gap-3">
            <input
              type="text"
              name="lecture_url"
              placeholder="https://github.com/CodePlatoon/curriculum/..."
              className="flex-1 border border-gray-300 rounded-lg px-4 py-2 text-sm text-gray-700 placeholder-gray-400 outline-none focus:border-gray-400"
            />
            <button
              type="submit"
              className="bg-[#e7771e] text-white text-sm font-semibold tracking-widest uppercase px-6 py-2 rounded-lg whitespace-nowrap hover:bg-[#d06a18]"
            >
              Generate
            </button>
          </form>
        </div>

        {/* Results area */}
        <div className="px-6 pb-6">
          <div className="border-l-4 border-[#e7771e] pl-4 h-[150px] overflow-y-auto flex items-start">
            {loading && (
              <p className="text-gray-400 text-sm italic mt-2">Loading...</p>
            )}
            {!loading && vocabList && (
              <ul className="divide-y divide-gray-200 w-full">
                {vocabList.map((item, index) => (
                  <li key={index} className="grid grid-cols-[180px_1fr] text-sm py-2">
                    <span className="font-medium text-gray-800 pr-4">{item.term}</span>
                    <span className="text-gray-600">{item.definition}</span>
                  </li>
                ))}
              </ul>
            )}
            {!loading && !vocabList && (
              <p className="text-gray-400 text-sm italic mt-2">
                Paste a curriculum URL above and click Generate to see relevant vocab terms.
              </p>
            )}
          </div>
        </div>

      </div>
    </div>
  )
}
