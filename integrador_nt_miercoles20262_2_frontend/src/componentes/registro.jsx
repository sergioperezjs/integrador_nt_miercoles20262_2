import React from 'react'
import {useState} from "react";

export default function registro() {

    let [observacion , setObservacion ] = useState("");
    let [estado, setEstado] = useState("");

    console.log(
            "Observación", observacion,
            "Estado", estado
        );

    function getData(e) {
        e.preventDefault();
    }

  return (
    <form onSubmit={getData}>
    <div className="w3-row-padding" style={{"margin":"8px -16px"}}>
          <div className="w3-half w3-margin-bottom">
            <label><i className="fa fa-male"></i> Adults</label>
            <input onChange={(e) => setObservacion(e.target.value)} className="w3-input w3-border" type="number"  name="observacion" min="1" max="5" />
          </div>
          <div className="w3-half">
            <label><i className="fa fa-child"></i> Kids</label>
            <input onChange={(e) => setEstado(e.target.value)} className="w3-input w3-border" type="number"  name="estado" min="0" max="1" />
          </div>
        </div>
        <button
        className="w3-button w3-dark-grey" type="submit"><i className="fa fa-search w3-margin-right"></i> Search availability</button>
      </form>
  )
}
