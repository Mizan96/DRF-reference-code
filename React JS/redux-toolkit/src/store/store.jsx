import { configureStore } from "@reduxjs/toolkit";
import articleSlice from "./article-reducer";

const store = configureStore({
    reducer: articleSlice.reducer
})

export default store;