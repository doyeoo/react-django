import React, { useState } from "react";
import axios from "axios";
import "./RestAPI.css";

function RestAPI() {
  const [text, setText] = useState([]);
  return (
    <div className="App">
      <h1>장고 리액트 연동 연습</h1>
      <button
        onClick={() => {
          axios
            .post("http://127.0.0.1:8000/review/", {
              title: "제목",
              content: "내용",
            })
            .then(function (response) {
              console.log(response);
            })
            .catch(function (error) {
              console.log(error);
            });
        }}
      >
        POST
      </button>
      <button
        onClick={() => {
          axios
            .get("http://127.0.0.1:8000/review/")
            .then(response => {
              setText([...response.data]);
              console.log(response.data);
            })
            .catch(function (error) {
              console.log(error);
            });
        }}
      >
        GET
      </button>
    </div>
  );
}

export default RestAPI;
