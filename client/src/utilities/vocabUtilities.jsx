import axios from "axios";

export const api = axios.create({
    baseURL: "/api/v1/vocab/",
});

export const getVocabList = async(lecture_url) => {
    try{
        let response = await api.post('',
            {lecture_url: lecture_url}
        )
        return response.data;
    } catch (error) {
        throw new Error(error.response?.data?.error || "Failed to get vocab list", { cause: error })
    }
}

export const deleteVocabList = async(lecture_urls) =>{
    try {
        let response = await api.delete('',
            {lecture_urls: lecture_urls}
        )
       return response.data;
    } catch (error) {
        throw new Error(error.response?.data?.error || "Failed to delete vocab list", { cause: error })
    }
   

} 