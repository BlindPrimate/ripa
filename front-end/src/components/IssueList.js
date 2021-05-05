import { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchIssues } from "../redux/actions";

const IssueList = () => {
    useEffect(() => {
        fetchIssues()
    })
    return (
        <div className="issue-list">
            <ul>
            </ul>
        </div>
    )
}

export default IssueList