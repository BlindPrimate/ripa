import { ADD_ISSUE } from "./actionTypes";
import axios from "axios";

const API_ROOT = process.env["REACT_APP_AXIOS_API_BASE_URL"]

axios.defaults.baseURL = API_ROOT


export const fetchIssues = () => {
    return (dispatch) => axios.get('issues').then((data) => {
        console.log(data)
        console.log(dispatch)
        return dispatch(data)
    })
}


export const addIssue = content => ({
    type: ADD_ISSUE,
    content
})

