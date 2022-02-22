import React, { useState } from "react";
import axios from "axios";
import "./RestAPI.css";

function RestAPI() {
  const [text, setText] = useState([]);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  return (
    <div className="App">
      <h1>장고 리액트 연동 연습</h1>
      <input value={title} onChange={e => setTitle(e.target.value)} />
      <br />
      <input value={content} onChange={e => setContent(e.target.value)} />
      <br />
      <button
        onClick={() => {
          axios
            .post("http://127.0.0.1:8000/review/", {
              title: title,
              content: content,
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
      {text.map(e => (
        <div>
          <div className="list">
            <span>
              #{e.id} {e.title} {e.content} {e.date}
            </span>
            <button
              className="btn-delete"
              onClick={() => {
                axios.delete(`http://127.0.0.1:8000/review/${e.id}`);
                setText(text.filter(text => text.id !== e.id));
              }}
            >
              DELETE
            </button>
          </div>
        </div>
      ))}
    </div>
  );
}

export default RestAPI;
