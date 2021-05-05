
import { GET_ISSUES } from "../actionTypes";

const initialState = {
    issues: {}
}

const getIssuesReducer = (state = initialState, action) => {
    switch(action.type) {
        case GET_ISSUES: {
            return {
                ...state, issues: action.payload
            }
        }
        default:
            return state
    }
}

export default getIssuesReducer