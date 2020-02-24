import React from "react";
import "./app.css";

const Response = props => {
  return (
    <section className="circle is-paddingless">
      <section className="text section has-text-centered is-paddingless">
        <section className="sigla">
          <h1>{props.sigla}</h1>
        </section>
        <section className="name">
          <h2>{props.nome}</h2>
        </section>
        <section className="description">
          <h2>{props.familia}</h2>
          <h2>{props.atomico}</h2>
          <h2>{props.m_molar}</h2>
        </section>
      </section>
    </section>
  );
};

export default Response;
