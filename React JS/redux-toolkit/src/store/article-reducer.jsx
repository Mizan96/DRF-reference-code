import { createSlice } from "@reduxjs/toolkit";

const initialState = {data: []};

const articleSlice = createSlice({
    name: 'article',
    initialState,
    reducers:
    {
        getArticles(state, action){
            state.data = action.payload;
        }
    }
});

export const articleActions = articleSlice.actions;

export default articleSlice;

