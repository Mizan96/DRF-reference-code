import { articleActions } from "./article-reducer"
import axios from "axios";

const getNewsFromServer = () => {
    return async (dispatch) => {
        const getNews = async () =>{
            const response = await axios.get('http://127.0.0.1:8000/api/articles/');
            return response.data;
        }

        try{
            const data = await getNews();
            dispatch(articleActions.getArticles(data));
        }
        catch(error){
            console.log(error);
        }
    }
}

export default getNewsFromServer;