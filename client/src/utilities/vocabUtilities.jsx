/**
 * Axios-based utility functions for interacting with the vocab API.
 * All requests are routed through the shared `api` instance.
 */
import axios from "axios";

/** Shared axios instance with the vocab API base URL. */
export const api = axios.create({
    baseURL: "/api/v1/vocab/",
});

/**
 * Fetches a vocabulary list for a given lecture URL by POSTing to the vocab API.
 *
 * @param {string} lecture_url - The URL of the lecture to generate vocab for.
 * @returns {Promise<Object>} The vocab data returned by the API.
 * @throws {Error} If the request fails or the server returns an error.
 */
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

/**
 * Deletes vocab list(s) for the given lecture URLs.
 *
 * @param {string[]} lecture_urls - Array of lecture URLs whose vocab should be deleted.
 * @returns {Promise<Object>} The deletion result returned by the API.
 * @throws {Error} If the request fails or the server returns an error.
 */
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